const { createClient } = require('@supabase/supabase-js')

function getBotioSupabase() {
  const url = process.env.BOTIO_SUPABASE_URL || process.env.SUPABASE_URL
  const key = process.env.BOTIO_SERVICE_ROLE_KEY || process.env.SUPABASE_SERVICE_ROLE_KEY
  if (!url || !key) {
    throw new Error('Botio Supabase credentials not configured')
  }
  return createClient(url, key, { auth: { persistSession: false } })
}

module.exports = { getBotioSupabase }
