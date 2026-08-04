import { google } from 'googleapis'

const CALENDAR_EVENTS_SCOPE = 'https://www.googleapis.com/auth/calendar.events'
const EMAIL_SCOPE = 'https://www.googleapis.com/auth/userinfo.email'
export const OWNER_GOOGLE_SCOPES = [CALENDAR_EVENTS_SCOPE, EMAIL_SCOPE]

export function getGoogleOAuthRedirectUri(): string {
  if (process.env.GOOGLE_OAUTH_REDIRECT_URI) {
    return process.env.GOOGLE_OAUTH_REDIRECT_URI
  }
  const vercelUrl = process.env.VERCEL_URL
  const base = vercelUrl ? `https://${vercelUrl}` : 'https://kalyo.io'
  return `${base}/api/admin/connect-google-calendar/callback`
}

export function getGoogleOAuthClient() {
  const clientId = process.env.GOOGLE_CLIENT_ID
  const clientSecret = process.env.GOOGLE_CLIENT_SECRET
  const redirectUri = getGoogleOAuthRedirectUri()

  if (!clientId || !clientSecret) {
    throw new Error('GOOGLE_CLIENT_ID o GOOGLE_CLIENT_SECRET no configurados')
  }

  return new google.auth.OAuth2(clientId, clientSecret, redirectUri)
}

export function generateOwnerGoogleAuthUrl(state: string): string {
  const client = getGoogleOAuthClient()
  return client.generateAuthUrl({
    access_type: 'offline',
    prompt: 'consent',
    scope: OWNER_GOOGLE_SCOPES,
    state,
    include_granted_scopes: true,
    login_hint: process.env.OWNER_GOOGLE_ALLOWED_EMAIL || 'Osvaldo@coloris.mx',
  })
}

export async function exchangeGoogleCodeForTokens(code: string) {
  const client = getGoogleOAuthClient()
  const { tokens } = await client.getToken(code)

  if (!tokens.access_token) {
    throw new Error('Google no devolvió access_token')
  }
  if (!tokens.refresh_token) {
    throw new Error(
      'Google no devolvió refresh_token. Revoca el acceso en myaccount.google.com/permissions y vuelve a conectar.',
    )
  }

  return tokens
}

export async function fetchGoogleUserEmail(accessToken: string): Promise<string> {
  const client = getGoogleOAuthClient()
  client.setCredentials({ access_token: accessToken })
  const oauth2 = google.oauth2({ version: 'v2', auth: client })
  const { data } = await oauth2.userinfo.get()
  if (!data.email) {
    throw new Error('No se pudo obtener el email de Google')
  }
  return data.email
}
