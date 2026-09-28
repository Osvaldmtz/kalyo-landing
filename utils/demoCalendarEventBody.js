const DEFAULT_TZ = 'America/Bogota'
const DEFAULT_DURATION_MINUTES = 30

function toLocalDateTime(iso, timeZone) {
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

  const get = (type) => parts.find((p) => p.type === type)?.value ?? '00'
  const hour = get('hour') === '24' ? '00' : get('hour')
  return `${get('year')}-${get('month')}-${get('day')}T${hour}:${get('minute')}:${get('second')}`
}

function addMinutesIso(iso, minutes) {
  return new Date(new Date(iso).getTime() + minutes * 60 * 1000).toISOString()
}

function formatBogotaWhen(iso, timeZone) {
  const dateFmt = new Intl.DateTimeFormat('es-CO', {
    timeZone,
    weekday: 'long',
    day: 'numeric',
    month: 'long',
    year: 'numeric',
  })
  const timeFmt = new Intl.DateTimeFormat('es-CO', {
    timeZone,
    hour: 'numeric',
    minute: '2-digit',
    hour12: true,
  })
  const date = new Date(iso)
  return `${dateFmt.format(date)}, ${timeFmt.format(date)} (${timeZone})`
}

function buildDemoCalendarEventBody(booking, timeZone = DEFAULT_TZ) {
  const meetLink = booking.meetLink
  const lines = [
    `Nombre: ${booking.name}`,
    `Email: ${booking.email}`,
  ]
  if (booking.country) lines.push(`País: ${booking.country}`)
  if (booking.whatsapp) lines.push(`Teléfono: ${booking.whatsapp}`)
  if (booking.interest) lines.push(`Notas: ${booking.interest}`)
  if (meetLink) lines.push(`Meet: ${meetLink}`)
  lines.push(`Hora: ${formatBogotaWhen(booking.scheduledAt, timeZone)}`)

  return {
    summary: `Demo Kalyo — ${booking.name}`,
    description: lines.join('\n'),
    location: meetLink || undefined,
    start: {
      dateTime: toLocalDateTime(booking.scheduledAt, timeZone),
      timeZone,
    },
    end: {
      dateTime: toLocalDateTime(addMinutesIso(booking.scheduledAt, DEFAULT_DURATION_MINUTES), timeZone),
      timeZone,
    },
    attendees: booking.email ? [{ email: booking.email }] : undefined,
  }
}

module.exports = {
  DEFAULT_TZ,
  DEFAULT_DURATION_MINUTES,
  buildDemoCalendarEventBody,
  toLocalDateTime,
}
