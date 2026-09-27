const { google } = require('googleapis')

function oauthClient() {
  const clientId = process.env.GOOGLE_CALENDAR_CLIENT_ID || process.env.GOOGLE_CLIENT_ID
  const clientSecret =
    process.env.GOOGLE_CALENDAR_CLIENT_SECRET || process.env.GOOGLE_CLIENT_SECRET
  const refreshToken = process.env.OWNER_GOOGLE_REFRESH_TOKEN?.trim()
  if (!clientId || !clientSecret || !refreshToken) return null
  const auth = new google.auth.OAuth2(clientId, clientSecret)
  auth.setCredentials({ refresh_token: refreshToken })
  return auth
}

function bogotaClock(date) {
  const fmt = new Intl.DateTimeFormat('en-CA', {
    timeZone: 'America/Bogota',
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    hour12: false,
  })
  const parts = Object.fromEntries(fmt.formatToParts(date).map((part) => [part.type, part.value]))
  const hour = parts.hour === '24' ? 0 : Number(parts.hour)
  return {
    date: `${parts.year}-${parts.month}-${parts.day}`,
    minutes: hour * 60 + Number(parts.minute),
  }
}

function busyToRanges(startIso, endIso) {
  const start = bogotaClock(new Date(startIso))
  const end = bogotaClock(new Date(endIso))
  if (start.date === end.date) {
    return [{ date: start.date, startMin: start.minutes, endMin: end.minutes }]
  }
  return [
    { date: start.date, startMin: start.minutes, endMin: 24 * 60 },
    { date: end.date, startMin: 0, endMin: end.minutes },
  ]
}

async function busyFromEvents(calendar, timeMin, timeMax) {
  const listed = await calendar.events.list({
    calendarId: 'primary',
    timeMin,
    timeMax,
    singleEvents: true,
    orderBy: 'startTime',
    maxResults: 250,
  })
  const ranges = []
  for (const event of listed.data.items || []) {
    if (event.status === 'cancelled' || event.transparency === 'transparent') continue
    if (!event.start?.dateTime || !event.end?.dateTime) continue
    ranges.push(...busyToRanges(event.start.dateTime, event.end.dateTime))
  }
  return ranges
}

/** Opaque events on the primary calendar, the same set freebusy would mark busy. */
async function getCalendarBusyRanges() {
  const auth = oauthClient()
  if (!auth) return []

  const calendar = google.calendar({ version: 'v3', auth })
  const timeMin = new Date().toISOString()
  const timeMax = new Date(Date.now() + 16 * 24 * 60 * 60 * 1000).toISOString()

  try {
    const response = await calendar.freebusy.query({
      requestBody: {
        timeMin,
        timeMax,
        timeZone: 'America/Bogota',
        items: [{ id: 'primary' }],
      },
    })
    const busy = response.data.calendars?.primary?.busy || []
    return busy.flatMap((block) => {
      if (!block.start || !block.end) return []
      return busyToRanges(block.start, block.end)
    })
  } catch (err) {
    const message = err instanceof Error ? err.message : String(err)
    console.error('[demo-calendar-busy] freebusy failed, falling back to events.list', message)
    try {
      return await busyFromEvents(calendar, timeMin, timeMax)
    } catch (listErr) {
      const listMessage = listErr instanceof Error ? listErr.message : String(listErr)
      console.error('[demo-calendar-busy] events.list failed', listMessage)
      return []
    }
  }
}

module.exports = { getCalendarBusyRanges }
