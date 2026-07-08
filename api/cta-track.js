const { getBotioSupabase } = require('../../lib/botio-supabase')

const ALLOWED_EVENTS = new Set([
  'cta_demo_hero',
  'cta_demo_section',
  'cta_whatsapp_landing',
  'cta_demo_confirmed',
])

function cleanString(value, maxLen = 200) {
  if (typeof value !== 'string') return null
  const trimmed = value.trim()
  if (!trimmed) return null
  return trimmed.slice(0, maxLen)
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
    const eventName = cleanString(body.event, 80)
    if (!eventName || !ALLOWED_EVENTS.has(eventName)) {
      return res.status(400).json({ error: 'Invalid event' })
    }

    const source = cleanString(body.source, 500) || '/'
    const sessionId = cleanString(body.session_id, 120)
    const country = cleanString(body.country, 120)
    const city = cleanString(body.city, 120)

    const supabase = getBotioSupabase()
    const { error } = await supabase.from('cta_events').insert({
      event_name: eventName,
      source,
      session_id: sessionId,
      country,
      city,
      event_timestamp: new Date().toISOString(),
    })

    if (error) {
      console.error('[cta-track] insert failed', error)
      return res.status(500).json({ error: 'Failed to store event' })
    }

    return res.status(201).json({ ok: true })
  } catch (err) {
    console.error('[cta-track]', err)
    return res.status(500).json({ error: 'Internal error' })
  }
}
