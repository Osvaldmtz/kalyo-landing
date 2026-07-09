const { getBotioSupabase } = require('../lib/botio-supabase')

const ALLOWED_EVENTS = new Set([
  'cta_demo_hero',
  'cta_demo_section',
  'cta_whatsapp_landing',
  'cta_demo_confirmed',
  'cta_plan_starter',
  'cta_plan_pro',
  'cta_plan_max',
  'cta_plan_ultra',
])

const VALUE_USD = {
  cta_demo_confirmed: 30,
  cta_plan_pro: 29,
  cta_plan_max: 39,
  cta_plan_ultra: 69,
  cta_whatsapp_landing: 5,
}

function getValueUsd(eventName) {
  return VALUE_USD[eventName] ?? 0
}

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

    const source = cleanString(body.source, 80) || 'landing'
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
      value_usd: getValueUsd(eventName),
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
