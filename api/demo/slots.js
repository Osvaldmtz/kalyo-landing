const { buildAvailability } = require('../../lib/demo-slots')
const { getBookedSlotKeys } = require('../../lib/demo-supabase')
const { getCalendarBusyRanges } = require('../../lib/demo-calendar-busy')

module.exports = async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', 'https://kalyo.io')
  res.setHeader('Access-Control-Allow-Methods', 'GET, OPTIONS')
  res.setHeader('Cache-Control', 'no-store')

  if (req.method === 'OPTIONS') {
    return res.status(204).end()
  }

  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' })
  }

  try {
    const [bookedKeys, busyRanges] = await Promise.all([
      getBookedSlotKeys(),
      getCalendarBusyRanges(),
    ])
    const availability = buildAvailability({ bookedKeys, busyRanges })
    return res.status(200).json(availability)
  } catch (err) {
    console.error('[demo/slots]', err)
    return res.status(500).json({ error: 'No se pudieron cargar los horarios' })
  }
}
