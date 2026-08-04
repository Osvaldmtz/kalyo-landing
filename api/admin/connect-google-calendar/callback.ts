import { createHmac, timingSafeEqual } from 'crypto'
import {
  exchangeGoogleCodeForTokens,
  fetchGoogleUserEmail,
} from '../../utils/googleOAuth'

type Req = {
  method?: string
  url?: string
}

type Res = {
  statusCode: number
  setHeader: (key: string, value: string) => void
  end: (body?: string) => void
}

function getAdminSecret(): string | null {
  return process.env.ADMIN_SECRET?.trim() || null
}

function verifyState(state: string): boolean {
  const secret = getAdminSecret()
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

function escapeHtml(str: string): string {
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
}

function sendHtml(res: Res, status: number, html: string) {
  res.statusCode = status
  res.setHeader('Content-Type', 'text/html; charset=utf-8')
  res.setHeader('Cache-Control', 'no-store')
  res.end(html)
}

export default async function handler(req: Req, res: Res) {
  if (req.method !== 'GET') {
    return sendHtml(res, 405, '<h1>Method not allowed</h1>')
  }

  const url = new URL(req.url || '', 'https://kalyo.io')
  const oauthError = url.searchParams.get('error')
  const code = url.searchParams.get('code')
  const state = url.searchParams.get('state')

  if (oauthError) {
    return sendHtml(res, 400, `<h1>OAuth cancelado</h1><p>${escapeHtml(oauthError)}</p>`)
  }

  if (!code || !state || !verifyState(state)) {
    return sendHtml(
      res,
      400,
      '<h1>Estado OAuth inválido</h1><p>Vuelve a iniciar desde /api/admin/connect-google-calendar</p>',
    )
  }

  try {
    const tokens = await exchangeGoogleCodeForTokens(code)
    const email = await fetchGoogleUserEmail(tokens.access_token)
    const allowed = (process.env.OWNER_GOOGLE_ALLOWED_EMAIL || 'osvamtz@gmail.com').toLowerCase()

    if (email.toLowerCase() !== allowed) {
      return sendHtml(
        res,
        403,
        `<h1>Cuenta no autorizada</h1><p>Conectaste ${escapeHtml(email)} pero se esperaba ${escapeHtml(allowed)}.</p>`,
      )
    }

    const refreshToken = tokens.refresh_token || ''

    return sendHtml(
      res,
      200,
      `<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>Google Calendar conectado</title>
  <style>
    body { font-family: system-ui, sans-serif; max-width: 720px; margin: 40px auto; padding: 0 16px; color: #1a1612; }
    code, pre { background: #f4f4f5; padding: 12px; border-radius: 8px; display: block; overflow-x: auto; word-break: break-all; }
    h1 { color: #7c3de3; }
  </style>
</head>
<body>
  <h1>Google Calendar conectado</h1>
  <p>Cuenta: <strong>${escapeHtml(email)}</strong></p>
  <p>Copia este valor en Vercel → Environment Variables como <code>OWNER_GOOGLE_REFRESH_TOKEN</code>:</p>
  <pre id="token">${escapeHtml(refreshToken)}</pre>
  <p>También puedes añadirlo a <code>.env.local</code> para pruebas locales.</p>
  <p style="color:#666;font-size:14px">No compartas este token. Si se filtra, revócalo en Google Account → Seguridad → Acceso de terceros.</p>
</body>
</html>`,
    )
  } catch (err) {
    console.error('[admin/connect-google-calendar/callback]', err)
    const message = err instanceof Error ? err.message : 'Error en callback OAuth'
    return sendHtml(res, 500, `<h1>Error</h1><p>${escapeHtml(message)}</p>`)
  }
}
