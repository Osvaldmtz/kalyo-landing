import { createClient } from '@supabase/supabase-js'
import { verifySignedOAuthState } from './oauthState'

function getSupabase() {
  const url = process.env.BOTIO_SUPABASE_URL || process.env.SUPABASE_URL
  const key = process.env.BOTIO_SERVICE_ROLE_KEY || process.env.SUPABASE_SERVICE_ROLE_KEY
  if (!url || !key) {
    throw new Error('Supabase credentials not configured')
  }
  return createClient(url, key, { auth: { persistSession: false } })
}

export async function saveOAuthState(state: string): Promise<void> {
  const supabase = getSupabase()
  const { error } = await supabase.from('oauth_states').insert({ state })
  if (error) throw error
}

export async function consumeOAuthState(state: string | null): Promise<boolean> {
  if (!state || !verifySignedOAuthState(state)) return false

  const supabase = getSupabase()
  const { data, error } = await supabase
    .from('oauth_states')
    .select('state')
    .eq('state', state)
    .maybeSingle()

  if (error || !data) return false

  const { error: deleteError } = await supabase.from('oauth_states').delete().eq('state', state)
  if (deleteError) {
    console.error('[oauthStateStore] failed to delete consumed state', deleteError)
  }

  return true
}
