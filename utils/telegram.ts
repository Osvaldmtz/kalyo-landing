export async function sendTelegramMessage(text: string): Promise<{ ok: boolean; reason?: string }> {
  const token = process.env.TELEGRAM_BOT_TOKEN
  const chatId = process.env.TELEGRAM_CHAT_ID

  if (!token || !chatId) {
    console.warn('[telegram] TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID not set — skipping')
    return { ok: false, reason: 'missing_config' }
  }

  try {
    const res = await fetch(`https://api.telegram.org/bot${token}/sendMessage`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ chat_id: chatId, text }),
    })

    if (!res.ok) {
      const body = await res.text()
      console.error('[telegram] send failed', res.status, body)
      return { ok: false, reason: `http_${res.status}` }
    }

    return { ok: true }
  } catch (err) {
    console.error('[telegram] send failed', err)
    return { ok: false, reason: 'network_error' }
  }
}

export async function sendDemoBookingTelegramAlert(params: {
  name: string
  email: string
  dateLabel: string
  phone: string
}): Promise<{ ok: boolean; reason?: string }> {
  const text = [
    '🗓 Nueva demo agendada',
    `Nombre: ${params.name}`,
    `Email: ${params.email}`,
    `Fecha: ${params.dateLabel}`,
    `Teléfono: ${params.phone}`,
  ].join('\n')

  return sendTelegramMessage(text)
}
