const { getSupabase } = require('../../lib/demo-supabase')
const { sendWhatsAppReminder } = require('../../lib/demo-notify')

function authorize(req) {
  const auth = req.headers.authorization || ''
  const secret = process.env.CRON_SECRET
  if (!secret) return false
  return auth === `Bearer ${secret}`
}

async function processReminders(type, windowStartMs, windowEndMs) {
  const supabase = getSupabase()
  const flag = type === '24h' ? 'reminder_24h_sent' : 'reminder_1h_sent'
  const now = Date.now()
  const from = new Date(now + windowStartMs).toISOString()
  const to = new Date(now + windowEndMs).toISOString()

  const { data, error } = await supabase
    .from('demo_bookings')
    .select('id, name, whatsapp, scheduled_at')
    .eq('status', 'confirmed')
    .eq(flag, false)
    .gte('scheduled_at', from)
    .lte('scheduled_at', to)

  if (error) throw error

  const stats = { type, candidates: data?.length || 0, sent: 0, errors: 0 }

  for (const row of data || []) {
    try {
      await sendWhatsAppReminder({
        whatsapp: row.whatsapp,
        name: row.name,
        scheduledAt: row.scheduled_at,
        type,
      })

      await supabase
        .from('demo_bookings')
        .update({ [flag]: true })
        .eq('id', row.id)

      stats.sent++
    } catch (err) {
      stats.errors++
      console.error(`[demo/reminders] ${type} failed for ${row.id}`, err)
    }
  }

  return stats
}

async function run(req, res) {
  if (!authorize(req)) {
    return res.status(401).json({ error: 'Unauthorized' })
  }

  try {
    // 24h reminder: 23h–25h ahead (±1h window, cron every 30 min)
    const stats24h = await processReminders('24h', 23 * 60 * 60 * 1000, 25 * 60 * 60 * 1000)
    // 1h reminder: 45min–75min ahead
    const stats1h = await processReminders('1h', 45 * 60 * 1000, 75 * 60 * 1000)

    return res.status(200).json({
      ok: true,
      at: new Date().toISOString(),
      reminders: [stats24h, stats1h],
    })
  } catch (err) {
    console.error('[demo/reminders]', err)
    return res.status(500).json({ error: 'Cron failed' })
  }
}

module.exports = async function handler(req, res) {
  if (req.method === 'GET' || req.method === 'POST') {
    return run(req, res)
  }
  return res.status(405).json({ error: 'Method not allowed' })
}
