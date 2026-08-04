import { createHmac, randomBytes, timingSafeEqual } from 'crypto'
import { generateOwnerGoogleAuthUrl } from '../../utils/googleOAuth'

type Req = { method?: string; query?: Record<string, string | string[] | undefined>; headers?: Record<string, string | string[] | undefined> }
type Res = { status: (code: number) => Res; json: (body: unknown) => void; setHeader: (k: string, v: string) => void; redirect: (code: number, url: string) => void }

function getAdminSecret(): string | null {
  const secret = process.env.ADMIN_SECRET?.trim()
  return secret || null
}

function isAuthorized(req: Req): boolean {
  const secret = getAdminSecret()
  if (!secret) return false
  const provided = String(req.query.secret || req.headers['x-admin-secret'] || '').trim()
  if (!provided) return false
  try {
    const a = Buffer.from(provided)
    const b = Buffer.from(secret)
    if (a.length !== b.length) return false
    return timingSafeEqual(a, b)
  } catch {
    return provided === secret
  }
}

function signState(payload: string): string {
  const secret = getAdminSecret()
  if (!secret) throw new Error('ADMIN_SECRET no configurado')
  const sig = createHmac('sha256', secret).update(payload).digest('hex')
  return `${payload}.${sig}`
}

export default function handler(req: Req, res: Res) {
  if (req.method !== 'GET') {
    return res.status(405).json({ error: 'Method not allowed' })
  }

  if (!isAuthorized(req)) {
    return res.status(401).json({
      error: 'No autorizado. Usa ?secret=ADMIN_SECRET',
    })
  }

  try {
    const nonce = randomBytes(16).toString('hex')
    const state = signState(nonce)
    const authUrl = generateOwnerGoogleAuthUrl(state)
    res.setHeader('Cache-Control', 'no-store')
    return res.redirect(302, authUrl)
  } catch (err) {
    console.error('[admin/connect-google-calendar]', err)
    const message = err instanceof Error ? err.message : 'Error al iniciar OAuth'
    return res.status(500).json({ error: message })
  }
}