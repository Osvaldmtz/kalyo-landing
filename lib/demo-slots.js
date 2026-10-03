const TZ = 'America/Bogota'
const MEET_LINK = 'https://meet.google.com/pgd-dxmb-sfk'
const MIN_LEAD_MS = 2 * 60 * 60 * 1000

const WEEKDAY_DAILY_MAX = 5
const SATURDAY_DAILY_MAX = 2
const SLOT_MINUTES = 30
const GAP_MINUTES = 30

function formatHmm(totalMinutes) {
  const h = Math.floor(totalMinutes / 60)
  const m = totalMinutes % 60
  return `${String(h).padStart(2, '0')}:${String(m).padStart(2, '0')}`
}

function timesBetween(startMin, endMin) {
  const times = []
  for (let minutes = startMin; minutes <= endMin; minutes += 30) {
    times.push(formatHmm(minutes))
  }
  return times
}

/** Weekdays start through 17:30 so a 30 min demo ends by 18:00 Colombia. */
const ALL_SLOT_TIMES = timesBetween(9 * 60, 17 * 60 + 30)
/** Saturday starts through 12:30 so a 30 min demo ends by 13:00 Colombia. */
const SATURDAY_SLOT_TIMES = timesBetween(9 * 60, 12 * 60 + 30)

/** One-off: Monday 5 Oct 2026 has no demos before 13:30, and the afternoon is fully open. */
const MONDAY_2026_10_05 = '2026-10-05'
const MONDAY_2026_10_05_OPEN_FROM_MIN = 13 * 60 + 30

/** One-off: Saturday 3 Oct 2026 opens to weekday-level capacity (usual Saturday cap is 2). */
const SATURDAY_2026_10_03 = '2026-10-03'
const SATURDAY_2026_10_03_DAILY_MAX = WEEKDAY_DAILY_MAX
/** Extra starts: 13:00 (booked/visible) + 15:30 (open desk). */
const SATURDAY_2026_10_03_EXTRA_TIMES = ['13:00', '15:30']
/** Confirmed demos that must stay blocked even if occupancy sync lags. */
const SATURDAY_2026_10_03_FORCE_BOOKED = new Set(['10:00', '13:00'])

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

function isBusinessDayIsoDate(isoDate) {
  const [y, m, d] = isoDate.split('-').map(Number)
  const day = new Date(Date.UTC(y, m - 1, d)).getUTCDay()
  return day >= 1 && day <= 6
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

function isSlotTooSoon(dateStr, timeStr, now = new Date()) {
  const slotMs = new Date(toScheduledIso(dateStr, timeStr)).getTime()
  return slotMs - now.getTime() < MIN_LEAD_MS
}

function getBusinessDates(daysAhead = 14) {
  const today = bogotaParts().date
  const dates = []
  for (let i = 0; i < daysAhead; i++) {
    const date = addDaysToIsoDate(today, i)
    if (isBusinessDayIsoDate(date)) dates.push(date)
  }
  return dates
}

function weekdayIndex(dateStr) {
  const [y, m, d] = dateStr.split('-').map(Number)
  return new Date(Date.UTC(y, m - 1, d)).getUTCDay()
}

function timeToMinutes(timeStr) {
  const [h, m] = timeStr.split(':').map(Number)
  return h * 60 + m
}

function normalizeOccupancy(input) {
  if (input instanceof Set) {
    return { bookedKeys: input, busyRanges: [] }
  }
  return {
    bookedKeys: input?.bookedKeys instanceof Set ? input.bookedKeys : new Set(),
    busyRanges: Array.isArray(input?.busyRanges) ? input.busyRanges : [],
  }
}

function bookedMinutesOnDate(dateStr, bookedKeys) {
  const prefix = `${dateStr}|`
  const starts = []
  for (const key of bookedKeys) {
    if (typeof key === 'string' && key.startsWith(prefix)) {
      starts.push(timeToMinutes(key.slice(prefix.length)))
    }
  }
  return starts
}

function rangesConflict(slotMin, startMin, endMin) {
  const slotEnd = slotMin + SLOT_MINUTES
  return slotMin < endMin + GAP_MINUTES && startMin < slotEnd + GAP_MINUTES
}

function slotTimesForDate(dateStr) {
  const day = weekdayIndex(dateStr)
  if (day === 0) return []
  if (dateStr === SATURDAY_2026_10_03) {
    const merged = new Set([...SATURDAY_SLOT_TIMES, ...SATURDAY_2026_10_03_EXTRA_TIMES])
    return [...merged].sort((a, b) => timeToMinutes(a) - timeToMinutes(b))
  }
  if (day === 6) return SATURDAY_SLOT_TIMES
  const times = ALL_SLOT_TIMES
  if (dateStr !== MONDAY_2026_10_05) return times
  return times.filter((time) => timeToMinutes(time) >= MONDAY_2026_10_05_OPEN_FROM_MIN)
}

function hashDate(value) {
  let hash = 2166136261
  for (let i = 0; i < value.length; i++) {
    hash ^= value.charCodeAt(i)
    hash = Math.imul(hash, 16777619)
  }
  return hash >>> 0
}

function areAdjacent(times, a, b) {
  return Math.abs(times.indexOf(a) - times.indexOf(b)) === 1
}

function pickFromBand(dateStr, band, times, chosen) {
  const pool = band.filter(
    (time) => !chosen.includes(time) && chosen.every((picked) => !areAdjacent(times, time, picked)),
  )
  if (!pool.length) return
  const index = hashDate(`${dateStr}|${band[0]}|${chosen.length}`) % pool.length
  chosen.push(pool[index])
}

/** Exactly 3 spread slots on weekdays stay marked busy so the grid doesn't look fully open. */
function artificialSlotsForDate(dateStr) {
  const times = slotTimesForDate(dateStr)
  if (times.length < 2) return new Set()

  const day = weekdayIndex(dateStr)
  if (day === 6 || dateStr === MONDAY_2026_10_05) return new Set()

  const rest = times.slice(1)
  const morning = rest.filter((time) => timeToMinutes(time) < 12 * 60)
  const afternoon =
    rest.filter((time) => timeToMinutes(time) > 15 * 60 + 30).length > 0
      ? rest.filter((time) => timeToMinutes(time) > 15 * 60 + 30)
      : rest.filter((time) => timeToMinutes(time) >= 14 * 60)
  const afternoonSet = new Set(afternoon)
  const midday = rest.filter((time) => {
    const minutes = timeToMinutes(time)
    return minutes >= 12 * 60 && minutes <= 15 * 60 + 30 && !afternoonSet.has(time)
  })

  const chosen = []
  pickFromBand(dateStr, morning, times, chosen)
  pickFromBand(dateStr, midday, times, chosen)
  pickFromBand(dateStr, afternoon, times, chosen)
  return new Set(chosen)
}

function buildSlotsForDate(dateStr, occupancyInput, now = new Date()) {
  const occupancy = normalizeOccupancy(occupancyInput)
  const day = weekdayIndex(dateStr)
  const bookings = bookedMinutesOnDate(dateStr, occupancy.bookedKeys)
  const dailyMax =
    dateStr === SATURDAY_2026_10_03
      ? SATURDAY_2026_10_03_DAILY_MAX
      : day === 6
        ? SATURDAY_DAILY_MAX
        : WEEKDAY_DAILY_MAX
  const dayFull = bookings.length >= dailyMax
  const artificial = artificialSlotsForDate(dateStr)
  const busy = occupancy.busyRanges.filter((range) => range.date === dateStr)
  const occupied = [
    ...bookings.map((start) => ({ start, end: start + SLOT_MINUTES })),
    ...busy.map((range) => ({ start: range.startMin, end: range.endMin })),
  ]

  return slotTimesForDate(dateStr).map((time) => {
    const minutes = timeToMinutes(time)
    const tooSoon = isSlotTooSoon(dateStr, time, now)
    const forceBooked =
      dateStr === SATURDAY_2026_10_03 && SATURDAY_2026_10_03_FORCE_BOOKED.has(time)
    const conflict =
      forceBooked || occupied.some((range) => rangesConflict(minutes, range.start, range.end))
    const exactBooking =
      forceBooked || occupancy.bookedKeys.has(slotKey(dateStr, time))

    let reason = 'open'
    if (tooSoon) reason = 'too_soon'
    else if (dayFull) reason = 'daily_max'
    else if (artificial.has(time)) reason = 'busy'
    else if (conflict) reason = exactBooking ? 'booked' : 'busy'

    return {
      time,
      label: formatTimeLabel(time),
      available: reason === 'open',
      reason,
    }
  })
}

function buildAvailability(occupancyInput = new Set(), now = new Date()) {
  const nowParts = bogotaParts(now)
  const dates = getBusinessDates(14)
  const days = dates.map((date) => {
    const slots = buildSlotsForDate(date, occupancyInput, now)
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

function isSlotAvailable(dateStr, timeStr, occupancyInput, now = new Date()) {
  const slots = buildSlotsForDate(dateStr, occupancyInput, now)
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
