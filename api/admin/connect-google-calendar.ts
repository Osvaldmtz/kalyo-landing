import { createHmac, randomBytes, timingSafeEqual } from 'crypto'
import { generateOwnerGoogleAuthUrl } from '../../utils/googleOAuth'

type Req = {
  method?: string
  query?: Record<string, string | string[] | undefined>
  headers?: Record<string, string | string[] | undefined>
}

type Res = {
  statusCode: number
  setHeader: (key: string, value: string) => void
  end: (body?: string) => void
}

function getAdminSecret(): string | null {
  return process.env.ADMIN_SECRET?.trim() || null
}

function isAuthorized(req: Req): boolean {
  const secret = getAdminSecret()
  if (!secret) return false
  const provided = String(req.query?.secret || req.headers?.['x-admin-secret'] || '').trim()
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

function sendJson(res: Res, status: number, body: unknown) {
  res.statusCode = status
  res.setHeader('Content-Type', 'application/json; charset=utf-8')
  res.setHeader('Cache-Control', 'no-store')
  res.end(JSON.stringify(body))
}

function redirect(res: Res, url: string) {
  res.statusCode = 302
  res.setHeader('Location', url)
  res.setHeader('Cache-Control', 'no-store')
  res.end()
}

export default function handler(req: Req, res: Res) {
  if (req.method !== 'GET') {
    return sendJson(res, 405, { error: 'Method not allowed' })
  }

  if (!isAuthorized(req)) {
    return sendJson(res, 401, { error: 'No autorizado. Usa ?secret=ADMIN_SECRET' })
  }

  try {
    const nonce = randomBytes(16).toString('hex')
    const state = signState(nonce)
    const authUrl = generateOwnerGoogleAuthUrl(state)
    console.log('[admin/connect-google-calendar] redirecting to Google OAuth')
    return redirect(res, authUrl)
  } catch (err) {
    console.error('[admin/connect-google-calendar]', err)
    const message = err instanceof Error ? err.message : 'Error al iniciar OAuth'
    return sendJson(res, 500, { error: message })
  }
}
