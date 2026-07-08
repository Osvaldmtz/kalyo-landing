const TZ = 'America/Bogota'
const MEET_LINK = 'https://meet.google.com/pgd-dxmb-sfk'

const MORNING_SLOTS = ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00']
const AFTERNOON_SLOTS = ['14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00']
const ALL_SLOT_TIMES = [...MORNING_SLOTS, ...AFTERNOON_SLOTS]

function mulberry32(seed) {
  return function next() {
    seed |= 0
    seed = (seed + 0x6d2b79f5) | 0
    let t = Math.imul(seed ^ (seed >>> 15), 1 | seed)
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296
  }
}

function seedFromDate(dateStr) {
  let h = 0
  for (let i = 0; i < dateStr.length; i++) {
    h = Math.imul(31, h) + dateStr.charCodeAt(i) | 0
  }
  return h
}

function getArtificiallyOccupiedSlots(dateStr) {
  const rng = mulberry32(seedFromDate(dateStr))
  const indices = ALL_SLOT_TIMES.map((_, i) => i)
  for (let i = indices.length - 1; i > 0; i--) {
    const j = Math.floor(rng() * (i + 1))
    ;[indices[i], indices[j]] = [indices[j], indices[i]]
  }
  const occupiedCount = Math.floor(ALL_SLOT_TIMES.length / 2)
  const occupied = new Set()
  for (let i = 0; i < occupiedCount; i++) {
    occupied.add(ALL_SLOT_TIMES[indices[i]])
  }
  return occupied
}

function bogotaParts(date = new Date()) {
  const fmt = new Intl.DateTimeFormat('en-CA', {
    timeZone: TZ,
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    hour12: false,
    weekday: 'short',
  })
  const parts = Object.fromEntries(fmt.formatToParts(date).map((p) => [p.type, p.value]))
  return {
    date: `${parts.year}-${parts.month}-${parts.day}`,
    time: `${parts.hour}:${parts.minute}`,
    weekday: parts.weekday,
  }
}

function parseWeekdayIndex(weekday) {
  const map = { Sun: 0, Mon: 1, Tue: 2, Wed: 3, Thu: 4, Fri: 5, Sat: 6 }
  return map[weekday] ?? 0
}

function addDaysToIsoDate(isoDate, days) {
  const [y, m, d] = isoDate.split('-').map(Number)
  const dt = new Date(Date.UTC(y, m - 1, d + days))
  return dt.toISOString().slice(0, 10)
}

function isWeekdayIsoDate(isoDate) {
  const [y, m, d] = isoDate.split('-').map(Number)
  const day = new Date(Date.UTC(y, m - 1, d)).getUTCDay()
  return day >= 1 && day <= 5
}

function formatTimeLabel(time24) {
  const [h, m] = time24.split(':').map(Number)
  const suffix = h >= 12 ? 'p. m.' : 'a. m.'
  const hour12 = h % 12 || 12
  return `${hour12}:${String(m).padStart(2, '0')} ${suffix}`
}

function toScheduledIso(dateStr, timeStr) {
  return `${dateStr}T${timeStr}:00-05:00`
}

function slotKey(dateStr, timeStr) {
  return `${dateStr}|${timeStr}`
}

function getBusinessDates(daysAhead = 14) {
  const today = bogotaParts().date
  const dates = []
  for (let i = 0; i < daysAhead; i++) {
    const date = addDaysToIsoDate(today, i)
    if (isWeekdayIsoDate(date)) dates.push(date)
  }
  return dates
}

function buildSlotsForDate(dateStr, bookedKeys, nowParts) {
  const artificial = getArtificiallyOccupiedSlots(dateStr)
  const isToday = dateStr === nowParts.date

  return ALL_SLOT_TIMES.map((time) => {
    const key = slotKey(dateStr, time)
    const past = isToday && time <= nowParts.time
    const booked = bookedKeys.has(key)
    const fakeBusy = artificial.has(time)
    const available = !past && !booked && !fakeBusy
    return {
      time,
      label: formatTimeLabel(time),
      available,
      reason: past ? 'past' : booked ? 'booked' : fakeBusy ? 'busy' : 'open',
    }
  })
}

function buildAvailability(bookedKeys = new Set()) {
  const nowParts = bogotaParts()
  const dates = getBusinessDates(14)
  const days = dates.map((date) => {
    const slots = buildSlotsForDate(date, bookedKeys, nowParts)
    return {
      date,
      slots,
      availableCount: slots.filter((s) => s.available).length,
    }
  })
  return {
    timezone: TZ,
    meetLink: MEET_LINK,
    today: nowParts.date,
    days,
  }
}

function isSlotAvailable(dateStr, timeStr, bookedKeys) {
  const nowParts = bogotaParts()
  const slots = buildSlotsForDate(dateStr, bookedKeys, nowParts)
  const slot = slots.find((s) => s.time === timeStr)
  return Boolean(slot?.available)
}

module.exports = {
  TZ,
  MEET_LINK,
  ALL_SLOT_TIMES,
  bogotaParts,
  formatTimeLabel,
  toScheduledIso,
  slotKey,
  buildAvailability,
  isSlotAvailable,
  getBusinessDates,
}
