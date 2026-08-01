const BASE_URL = 'https://api.dataforseo.com/v3'

function getCredentials() {
  const login = process.env.DATAFORSEO_LOGIN
  const password = process.env.DATAFORSEO_PASSWORD
  if (!login || !password) {
    throw new Error('DataForSEO credentials not configured (DATAFORSEO_LOGIN, DATAFORSEO_PASSWORD)')
  }
  return { login, password }
}

function getAuthHeader() {
  const { login, password } = getCredentials()
  const token = Buffer.from(`${login}:${password}`).toString('base64')
  return `Basic ${token}`
}

async function dataForSeoRequest(path, options = {}) {
  const url = `${BASE_URL}${path.startsWith('/') ? path : `/${path}`}`
  const response = await fetch(url, {
    ...options,
    headers: {
      Authorization: getAuthHeader(),
      'Content-Type': 'application/json',
      ...options.headers,
    },
  })

  const data = await response.json().catch(() => null)
  if (!data || typeof data.status_code !== 'number') {
    throw new Error(`DataForSEO request failed (${response.status}): invalid response`)
  }

  if (response.status === 401) {
    throw new Error(`DataForSEO authentication failed: ${data.status_message || response.statusText}`)
  }

  return data
}

/** Ping DataForSEO API to verify credentials and connectivity. */
async function testConnection() {
  const data = await dataForSeoRequest('/appendix/user_data')
  if (data.status_code !== 20000) {
    throw new Error(`DataForSEO test failed (${data.status_code}): ${data.status_message}`)
  }
  return data
}

module.exports = {
  BASE_URL,
  getAuthHeader,
  dataForSeoRequest,
  testConnection,
}
