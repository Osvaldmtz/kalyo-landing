import { google } from 'googleapis'
// eslint-disable-next-line @typescript-eslint/no-require-imports
const { MEET_LINK, TZ } = require('../lib/demo-slots') as {
  MEET_LINK: string
  TZ: string
}
import { getGoogleOAuthClient } from './googleOAuth'

export interface DemoBooking {
  name: string
  email: string
  whatsapp: string
  country?: string | null
  interest?: string | null
  scheduledAt: string
  meetLink?: string | null
}

function toLocalDateTime(iso: string, timeZone: string): string {
  const date = new Date(iso)
  const parts = new Intl.DateTimeFormat('en-CA', {
    timeZone,
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
    hour12: false,
  }).formatToParts(date)

  const get = (type: string) => parts.find((p) => p.type === type)?.value ?? '00'
  return `${get('year')}-${get('month')}-${get('day')}T${get('hour')}:${get('minute')}:${get('second')}`
}

function addMinutesIso(iso: string, minutes: number): string {
  return new Date(new Date(iso).getTime() + minutes * 60 * 1000).toISOString()
}

function buildDescription(booking: DemoBooking): string {
  const lines = [
    `Nombre: ${booking.name}`,
    `Email: ${booking.email}`,
    `Teléfono: ${booking.whatsapp}`,
  ]
  if (booking.country) lines.push(`País: ${booking.country}`)
  if (booking.interest) lines.push(`Notas: ${booking.interest}`)
  return lines.join('\n')
}

export async function createDemoCalendarEvent(
  booking: DemoBooking,
): Promise<{ ok: boolean; eventId?: string; error?: string }> {
  const refreshToken = process.env.OWNER_GOOGLE_REFRESH_TOKEN
  if (!refreshToken) {
    console.warn('[ownerCalendar] OWNER_GOOGLE_REFRESH_TOKEN not set — skipping')
    return { ok: false, error: 'missing_refresh_token' }
  }

  try {
    const auth = getGoogleOAuthClient()
    auth.setCredentials({ refresh_token: refreshToken })

    const calendar = google.calendar({ version: 'v3', auth })
    const startLocal = toLocalDateTime(booking.scheduledAt, TZ)
    const endLocal = toLocalDateTime(addMinutesIso(booking.scheduledAt, 30), TZ)

    const { data } = await calendar.events.insert({
      calendarId: 'primary',
      sendUpdates: 'all',
      requestBody: {
        summary: `Demo Kalyo — ${booking.name}`,
        description: buildDescription(booking),
        location: booking.meetLink || MEET_LINK,
        start: {
          dateTime: startLocal,
          timeZone: TZ,
        },
        end: {
          dateTime: endLocal,
          timeZone: TZ,
        },
        attendees: [{ email: booking.email }],
      },
    })

    return { ok: true, eventId: data.id ?? undefined }
  } catch (err) {
    const message = err instanceof Error ? err.message : 'Error al crear evento'
    console.error('[ownerCalendar] create event failed', err)
    return { ok: false, error: message }
  }
}
