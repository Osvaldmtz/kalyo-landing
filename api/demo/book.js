const {
  isSlotAvailable,
  toScheduledIso,
  MEET_LINK,
  formatTimeLabel,
  TZ,
} = require('../../lib/demo-slots')
const { getSupabase, getBookedSlotKeys } = require('../../lib/demo-supabase')
const { sendConfirmationEmail, formatDemoDateTime } = require('../../lib/demo-notify')

function normalizeWhatsApp(countryCode, phone) {
  const digits = String(phone).replace(/\D/g, '')
  const code = String(countryCode).replace(/\D/g, '')
  if (!digits || !code) return null
  return `+${code}${digits}`
}

function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)
}

module.exports = async function handler(req, res) {
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

    try {
      await sendConfirmationEmail({ name, email, scheduledAt })
    } catch (emailErr) {
      console.error('[demo/book] email failed', emailErr)
    }

    const { dateLabel, timeLabel } = formatDemoDateTime(scheduledAt)

    return res.status(201).json({
      ok: true,
      id: data.id,
      meetLink: data.meet_link,
      scheduledAt: data.scheduled_at,
      dateLabel,
      timeLabel,
      timeLabelShort: formatTimeLabel(time),
      timezone: TZ,
    })
  } catch (err) {
    console.error('[demo/book]', err)
    return res.status(500).json({ error: 'Error interno al agendar' })
  }
}
