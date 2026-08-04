import { createHmac, randomBytes, timingSafeEqual } from 'crypto'

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
