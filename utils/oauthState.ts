import { createHmac, randomBytes, timingSafeEqual } from 'crypto'

export const OAUTH_STATE_COOKIE = 'google_oauth_state'
const COOKIE_MAX_AGE_SEC = 600

function getAdminSecret(): string {
  const secret = process.env.ADMIN_SECRET?.trim()
  if (!secret) throw new Error('ADMIN_SECRET no configurado')
  return secret
}

export function createSignedOAuthState(): string {
  const nonce = randomBytes(16).toString('hex')
  const sig = createHmac('sha256', getAdminSecret()).update(nonce).digest('hex')
  return `${nonce}.${sig}`
}

export function verifySignedOAuthState(state: string): boolean {
  if (!state) return false
  const secret = process.env.ADMIN_SECRET?.trim()
  if (!secret) return false

  const dot = state.lastIndexOf('.')
  if (dot <= 0) return false

  const payload = state.slice(0, dot)
  const sig = state.slice(dot + 1)
  const expected = createHmac('sha256', secret).update(payload).digest('hex')

  try {
    const a = Buffer.from(sig)
    const b = Buffer.from(expected)
    if (a.length !== b.length) return false
    return timingSafeEqual(a, b)
  } catch {
    return sig === expected
  }
}

export function buildOAuthStateCookie(state: string): string {
  const secure = process.env.NODE_ENV === 'production' || process.env.VERCEL === '1'
  const flags = [
    `${OAUTH_STATE_COOKIE}=${encodeURIComponent(state)}`,
    'HttpOnly',
    secure ? 'Secure' : '',
    'SameSite=Lax',
    'Path=/',
    `Max-Age=${COOKIE_MAX_AGE_SEC}`,
  ].filter(Boolean)
  return flags.join('; ')
}

export function buildClearOAuthStateCookie(): string {
  const secure = process.env.NODE_ENV === 'production' || process.env.VERCEL === '1'
  const flags = [
    `${OAUTH_STATE_COOKIE}=`,
    'HttpOnly',
    secure ? 'Secure' : '',
    'SameSite=Lax',
    'Path=/',
    'Max-Age=0',
  ].filter(Boolean)
  return flags.join('; ')
}

export function parseCookies(header: string | undefined): Record<string, string> {
  if (!header) return {}
  const cookies: Record<string, string> = {}
  for (const part of header.split(';')) {
    const trimmed = part.trim()
    if (!trimmed) continue
    const eq = trimmed.indexOf('=')
    if (eq <= 0) continue
    const key = trimmed.slice(0, eq)
    const value = trimmed.slice(eq + 1)
    cookies[key] = decodeURIComponent(value)
  }
  return cookies
}

export function validateOAuthState(returnedState: string | null, cookieHeader: string | undefined): boolean {
  if (!returnedState) return false
  if (!verifySignedOAuthState(returnedState)) return false

  const cookieState = parseCookies(cookieHeader)[OAUTH_STATE_COOKIE]
  if (!cookieState) return false

  try {
    const a = Buffer.from(returnedState)
    const b = Buffer.from(cookieState)
    if (a.length !== b.length) return false
    return timingSafeEqual(a, b)
  } catch {
    return returnedState === cookieState
  }
}

export function getQueryParam(
  query: Record<string, string | string[] | undefined> | undefined,
  url: string | undefined,
  key: string,
): string | null {
  const fromQuery = query?.[key]
  if (typeof fromQuery === 'string') return fromQuery
  if (Array.isArray(fromQuery) && fromQuery[0]) return fromQuery[0]

  if (url) {
    try {
      const parsed = url.startsWith('http') ? new URL(url) : new URL(url, 'https://kalyo.io')
      return parsed.searchParams.get(key)
    } catch {
      return null
    }
  }

  return null
}
