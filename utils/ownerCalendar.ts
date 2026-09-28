import { google, type calendar_v3 } from 'googleapis'
// eslint-disable-next-line @typescript-eslint/no-require-imports
const { MEET_LINK, TZ } = require('../lib/demo-slots') as {
  MEET_LINK: string
  TZ: string
}
// eslint-disable-next-line @typescript-eslint/no-require-imports
const { getSupabase } = require('../lib/demo-supabase') as {
  getSupabase: () => {
    from: (table: string) => {
      select: (columns: string) => {
        eq: (column: string, value: string) => {
          maybeSingle: () => Promise<{ data: { id?: string; refresh_token?: string } | null; error: { message: string } | null }>
        }
      }
      update: (values: Record<string, string>) => {
        eq: (column: string, value: string) => Promise<{ error: { message: string } | null }>
      }
    }
  }
}
// eslint-disable-next-line @typescript-eslint/no-require-imports
const { buildDemoCalendarEventBody } = require('./demoCalendarEventBody') as {
  buildDemoCalendarEventBody: (booking: DemoBooking, timeZone?: string) => Record<string, unknown>
}
const CALENDAR_HOST_EMAIL = 'osvamtz@gmail.com'

export interface DemoBooking {
  name: string
  email: string
  whatsapp: string
  country?: string | null
  interest?: string | null
  scheduledAt: string
  meetLink?: string | null
}

async function loadCalendarCredentialsRefreshToken(): Promise<{ id: string; refreshToken: string } | null> {
  const clientId = process.env.GOOGLE_CALENDAR_CLIENT_ID
  const clientSecret = process.env.GOOGLE_CALENDAR_CLIENT_SECRET
  if (!clientId || !clientSecret) return null

  try {
    const supabase = getSupabase()
    const { data, error } = await supabase
      .from('calendar_credentials')
      .select('id, refresh_token')
      .eq('host_email', CALENDAR_HOST_EMAIL)
      .maybeSingle()

    if (error || !data?.id || !data.refresh_token) {
      console.warn('[ownerCalendar] calendar_credentials unavailable', error?.message ?? 'missing_row')
      return null
    }
    return { id: data.id, refreshToken: data.refresh_token }
  } catch (err) {
    console.warn(
      '[ownerCalendar] could not load calendar_credentials',
      err instanceof Error ? err.message : err,
    )
    return null
  }
}

async function persistRefreshedAccessToken(
  credentialId: string,
  auth: InstanceType<typeof google.auth.OAuth2>,
): Promise<void> {
  const credentials = auth.credentials
  if (!credentials.access_token) return
  const expiresAt = new Date(credentials.expiry_date ?? Date.now() + 3600 * 1000).toISOString()
  const supabase = getSupabase()
  const { error } = await supabase
    .from('calendar_credentials')
    .update({
      access_token: credentials.access_token,
      token_expires_at: expiresAt,
      updated_at: new Date().toISOString(),
    })
    .eq('id', credentialId)
  if (error) {
    console.warn('[ownerCalendar] failed to persist refreshed access token', error.message)
  }
}

async function authorizeCalendar(): Promise<InstanceType<typeof google.auth.OAuth2>> {
  const stored = await loadCalendarCredentialsRefreshToken()
  if (stored) {
    const auth = new google.auth.OAuth2(
      process.env.GOOGLE_CALENDAR_CLIENT_ID,
      process.env.GOOGLE_CALENDAR_CLIENT_SECRET,
    )
    auth.setCredentials({ refresh_token: stored.refreshToken })
    try {
      const { token } = await auth.getAccessToken()
      if (!token) throw new Error('invalid_refresh_token')
      await persistRefreshedAccessToken(stored.id, auth)
      console.log('[ownerCalendar] authorized via calendar_credentials')
      return auth
    } catch (err) {
      const message = err instanceof Error ? err.message : 'calendar_credentials_auth_failed'
      console.error('[ownerCalendar] calendar_credentials refresh failed', message)
    }
  }

  const refreshToken = process.env.OWNER_GOOGLE_REFRESH_TOKEN?.trim()
  const clientId = process.env.GOOGLE_CLIENT_ID
  const clientSecret = process.env.GOOGLE_CLIENT_SECRET
  if (!refreshToken) {
    throw new Error('missing_refresh_token')
  }
  if (!clientId || !clientSecret) {
    throw new Error('missing_google_oauth_client')
  }

  const auth = new google.auth.OAuth2(clientId, clientSecret)
  auth.setCredentials({ refresh_token: refreshToken })
  const { token } = await auth.getAccessToken()
  if (!token) throw new Error('invalid_refresh_token')
  console.log('[ownerCalendar] authorized via OWNER_GOOGLE_REFRESH_TOKEN')
  return auth
}

export async function createDemoCalendarEvent(
  booking: DemoBooking,
): Promise<{ ok: boolean; eventId?: string; meetLink?: string; error?: string }> {
  const meetLink = booking.meetLink || MEET_LINK
  console.log('[ownerCalendar] init', {
    hasCalendarClient: !!process.env.GOOGLE_CALENDAR_CLIENT_ID,
    hasOwnerRefreshToken: !!process.env.OWNER_GOOGLE_REFRESH_TOKEN,
    scheduledAt: booking.scheduledAt,
    attendee: booking.email,
  })

  try {
    const auth = await authorizeCalendar()
    const calendar = google.calendar({ version: 'v3', auth })
    const requestBody = buildDemoCalendarEventBody(
      { ...booking, meetLink },
      TZ,
    ) as calendar_v3.Schema$Event

    console.log('[ownerCalendar] inserting event', {
      start: requestBody.start,
      timeZone: TZ,
    })

    const { data } = await calendar.events.insert({
      calendarId: 'primary',
      sendUpdates: 'all',
      requestBody,
    })

    console.log('[ownerCalendar] event created', { eventId: data.id })
    return { ok: true, eventId: data.id ?? undefined, meetLink }
  } catch (err) {
    const gaxiosErr = err as { response?: { data?: unknown }; message?: string }
    const message = err instanceof Error ? err.message : 'Error al crear evento'
    console.error('[ownerCalendar] create event failed', {
      message,
      googleError: gaxiosErr.response?.data,
    })
    return { ok: false, error: message }
  }
}
