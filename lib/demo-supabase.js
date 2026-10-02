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
  const url = process.env.BOTIO_SUPABASE_URL || process.env.SUPABASE_URL
  const key = process.env.BOTIO_SERVICE_ROLE_KEY || process.env.SUPABASE_SERVICE_ROLE_KEY
  if (!url || !key) return new Set()

  const supabase = createClient(url, key, { auth: { persistSession: false } })
  const [bookings, demos] = await Promise.all([
    supabase
      .from('demo_bookings')
      .select('scheduled_at')
      .in('status', ['pending', 'confirmed', 'rescheduled_by_admin']),
    supabase
      .from('scheduled_demos')
      .select('scheduled_at')
      .eq('status', 'scheduled'),
  ])

  if (bookings.error) throw bookings.error
  if (demos.error) throw demos.error

  const keys = new Set()
  for (const row of [...(bookings.data || []), ...(demos.data || [])]) {
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
    const hour = String(parts.hour).padStart(2, '0')
    const minute = String(parts.minute).padStart(2, '0')
    keys.add(slotKey(`${parts.year}-${parts.month}-${parts.day}`, `${hour}:${minute}`))
  }
  return keys
}

module.exports = { getSupabase, getBookedSlotKeys }
