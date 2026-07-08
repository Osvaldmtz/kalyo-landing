const { createClient } = require('@supabase/supabase-js')
const { slotKey } = require('./demo-slots')

function getSupabase() {
  const url = process.env.BOTIO_SUPABASE_URL || process.env.SUPABASE_URL
  const key = process.env.BOTIO_SERVICE_ROLE_KEY || process.env.SUPABASE_SERVICE_ROLE_KEY
  if (!url || !key) {
    throw new Error('Supabase credentials not configured')
  }
  return createClient(url, key, { auth: { persistSession: false } })
}

async function getBookedSlotKeys() {
  const supabase = getSupabase()
  const { data, error } = await supabase
    .from('demo_bookings')
    .select('scheduled_at, status')
    .in('status', ['pending', 'confirmed'])

  if (error) throw error

  const keys = new Set()
  for (const row of data || []) {
    const dt = new Date(row.scheduled_at)
    const fmt = new Intl.DateTimeFormat('en-CA', {
      timeZone: 'America/Bogota',
      year: 'numeric',
      month: '2-digit',
      day: '2-digit',
      hour: '2-digit',
      minute: '2-digit',
      hour12: false,
    })
    const parts = Object.fromEntries(fmt.formatToParts(dt).map((p) => [p.type, p.value]))
    const date = `${parts.year}-${parts.month}-${parts.day}`
    const time = `${parts.hour}:${parts.minute}`
    keys.add(slotKey(date, time))
  }
  return keys
}

module.exports = { getSupabase, getBookedSlotKeys }
