// eslint-disable-next-line @typescript-eslint/no-require-imports
const {
  isSlotAvailable,
  toScheduledIso,
  MEET_LINK,
  formatTimeLabel,
  TZ,
} = require('../../lib/demo-slots')
// eslint-disable-next-line @typescript-eslint/no-require-imports
const { getSupabase, getBookedSlotKeys } = require('../../lib/demo-supabase')
// eslint-disable-next-line @typescript-eslint/no-require-imports
const {
  sendConfirmationEmail,
  sendOwnerAlertEmail,
  sendOwnerAlertWhatsApp,
  formatDemoDateTime,
  isValidTimezone,
  getTimezoneLabel,
} = require('../../lib/demo-notify')
import { sendDemoBookingTelegramAlert } from '../../utils/telegram'
import { createDemoCalendarEvent } from '../../utils/ownerCalendar'

function normalizeWhatsApp(countryCode: string, phone: string) {
  const digits = String(phone).replace(/\D/g, '')
  const code = String(countryCode).replace(/\D/g, '')
  if (!digits || !code) return null
  return `+${code}${digits}`
}

function isValidEmail(email: string) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)
}

export default async function handler(req: { method?: string; body?: Record<string, unknown> }, res: {
  setHeader: (k: string, v: string) => void
  status: (code: number) => { json: (body: unknown) => void; end: () => void }
}) {
  res.setHeader('Access-Control-Allow-Origin', 'https://kalyo.io')
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS')
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type')

  if (req.method === 'OPTIONS') {
    return res.status(204).end()
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' })
  }

  try {
    const body = req.body || {}
    const name = String(body.name || '').trim()
    const email = String(body.email || '').trim().toLowerCase()
    const countryCode = String(body.countryCode || '').trim()
    const phone = String(body.phone || '').trim()
    const country = String(body.country || '').trim()
    const interest = String(body.interest || '').trim() || null
    const date = String(body.date || '').trim()
    const time = String(body.time || '').trim()
    const clientTimezone = String(body.clientTimezone || '').trim()

    if (!name || name.length < 2) {
      return res.status(400).json({ error: 'Ingresa tu nombre completo' })
    }
    if (!isValidEmail(email)) {
      return res.status(400).json({ error: 'Ingresa un email válido' })
    }
    if (!country) {
      return res.status(400).json({ error: 'Selecciona tu país' })
    }

    const whatsapp = normalizeWhatsApp(countryCode, phone)
    if (!whatsapp || whatsapp.length < 10) {
      return res.status(400).json({ error: 'Ingresa un WhatsApp válido' })
    }

    if (!date || !time) {
      return res.status(400).json({ error: 'Selecciona fecha y hora' })
    }

    const bookedKeys = await getBookedSlotKeys()
    if (!isSlotAvailable(date, time, bookedKeys)) {
      return res.status(409).json({ error: 'Ese horario ya no está disponible. Elige otro.' })
    }

    const scheduledAt = toScheduledIso(date, time)
    const supabase = getSupabase()

    const { data, error } = await supabase
      .from('demo_bookings')
      .insert({
        name,
        email,
        whatsapp,
        country,
        interest,
        scheduled_at: scheduledAt,
        meet_link: MEET_LINK,
        status: 'confirmed',
      })
      .select('id, scheduled_at, meet_link')
      .single()

    if (error) {
      console.error('[demo/book] insert error', error)
      return res.status(500).json({ error: 'No se pudo agendar la demo' })
    }

    const ownerDateTime = formatDemoDateTime(scheduledAt, TZ)
    const ownerDateLabel = `${ownerDateTime.dateLabel}, ${ownerDateTime.timeLabel} (Colombia)`

    const notifyResults: Record<string, unknown> = {
      telegram: null,
      calendar: null,
      confirmation: null,
      owner: null,
      ownerWhatsApp: null,
    }

    try {
      notifyResults.telegram = await sendDemoBookingTelegramAlert({
        name,
        email,
        dateLabel: ownerDateLabel,
        phone: whatsapp,
      })
      console.log('[demo/book] telegram alert', { bookingId: data.id, result: notifyResults.telegram })
    } catch (telegramErr) {
      notifyResults.telegram = {
        ok: false,
        error: telegramErr instanceof Error ? telegramErr.message : 'telegram_error',
      }
      console.error('[demo/book] telegram alert failed', { bookingId: data.id, error: notifyResults.telegram })
    }

    try {
      notifyResults.calendar = await createDemoCalendarEvent({
        name,
        email,
        whatsapp,
        country,
        interest,
        scheduledAt,
        meetLink: data.meet_link,
      })
      console.log('[demo/book] calendar event', { bookingId: data.id, result: notifyResults.calendar })
    } catch (calendarErr) {
      notifyResults.calendar = {
        ok: false,
        error: calendarErr instanceof Error ? calendarErr.message : 'calendar_error',
      }
      console.error('[demo/book] calendar event failed', { bookingId: data.id, error: notifyResults.calendar })
    }

    try {
      notifyResults.confirmation = await sendConfirmationEmail({
        name,
        email,
        scheduledAt,
        clientTimezone: isValidTimezone(clientTimezone) ? clientTimezone : undefined,
      })
      console.log('[demo/book] confirmation email', { bookingId: data.id, to: email, result: notifyResults.confirmation })
    } catch (emailErr) {
      notifyResults.confirmation = {
        ok: false,
        error: emailErr instanceof Error ? emailErr.message : 'email_error',
      }
      console.error('[demo/book] confirmation email failed', { bookingId: data.id, to: email, error: notifyResults.confirmation })
    }

    try {
      notifyResults.owner = await sendOwnerAlertEmail({
        name,
        email,
        whatsapp,
        country,
        interest,
        scheduledAt,
      })
      console.log('[demo/book] owner alert', { bookingId: data.id, result: notifyResults.owner })
    } catch (ownerErr) {
      notifyResults.owner = {
        ok: false,
        error: ownerErr instanceof Error ? ownerErr.message : 'owner_email_error',
      }
      console.error('[demo/book] owner alert failed', { bookingId: data.id, error: notifyResults.owner })
    }

    try {
      notifyResults.ownerWhatsApp = await sendOwnerAlertWhatsApp({
        name,
        email,
        whatsapp,
        country,
        interest,
        scheduledAt,
      })
      console.log('[demo/book] owner WhatsApp alert', {
        bookingId: data.id,
        result: notifyResults.ownerWhatsApp,
      })
    } catch (ownerWaErr) {
      notifyResults.ownerWhatsApp = {
        ok: false,
        error: ownerWaErr instanceof Error ? ownerWaErr.message : 'owner_whatsapp_error',
      }
      console.error('[demo/book] owner WhatsApp alert failed', {
        bookingId: data.id,
        error: notifyResults.ownerWhatsApp,
      })
    }

    const displayTimezone = isValidTimezone(clientTimezone) ? clientTimezone : TZ
    const { dateLabel, timeLabel } = formatDemoDateTime(scheduledAt, displayTimezone)
    const timezoneLabel = getTimezoneLabel(displayTimezone)

    return res.status(201).json({
      ok: true,
      id: data.id,
      meetLink: data.meet_link,
      scheduledAt: data.scheduled_at,
      dateLabel,
      timeLabel,
      timezoneLabel,
      timeLabelShort: formatTimeLabel(time),
      timezone: displayTimezone,
    })
  } catch (err) {
    console.error('[demo/book]', err)
    return res.status(500).json({ error: 'Error interno al agendar' })
  }
}
