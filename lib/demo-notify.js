const { MEET_LINK, formatTimeLabel, TZ } = require('./demo-slots')

function formatDemoDateTime(scheduledAt) {
  const dt = new Date(scheduledAt)
  const dateFmt = new Intl.DateTimeFormat('es-CO', {
    timeZone: TZ,
    weekday: 'long',
    day: 'numeric',
    month: 'long',
    year: 'numeric',
  })
  const timeFmt = new Intl.DateTimeFormat('es-CO', {
    timeZone: TZ,
    hour: 'numeric',
    minute: '2-digit',
    hour12: true,
  })
  return {
    dateLabel: dateFmt.format(dt),
    timeLabel: timeFmt.format(dt),
  }
}

async function sendConfirmationEmail({ name, email, scheduledAt }) {
  const apiKey = process.env.RESEND_API_KEY
  if (!apiKey) {
    console.warn('[demo] RESEND_API_KEY not set — skipping email')
    return false
  }

  const { dateLabel, timeLabel } = formatDemoDateTime(scheduledAt)
  const from = process.env.EMAIL_FROM || 'Kalyo <hola@kalyo.io>'

  const res = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${apiKey}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      from,
      to: email,
      subject: 'Tu demo de Kalyo está confirmada',
      html: `
        <div style="font-family:sans-serif;max-width:520px;margin:auto;padding:24px">
          <h2 style="color:#7C3DE3">¡Demo confirmada!</h2>
          <p>Hola <strong>${escapeHtml(name)}</strong>,</p>
          <p>Tu demo de Kalyo quedó agendada para:</p>
          <p style="font-size:18px"><strong>${escapeHtml(dateLabel)}</strong><br>${escapeHtml(timeLabel)} (hora Colombia)</p>
          <p>Únete a la videollamada aquí:</p>
          <a href="${MEET_LINK}" style="display:inline-block;background:#7C3DE3;color:#fff;padding:12px 24px;border-radius:8px;text-decoration:none;margin:12px 0">
            Entrar a Google Meet →
          </a>
          <p style="color:#666;font-size:14px">También te enviaremos recordatorios por WhatsApp 24 horas y 1 hora antes.</p>
          <p style="color:#888;font-size:12px;margin-top:24px">Kalyo — Plataforma para psicólogos</p>
        </div>
      `,
    }),
  })

  if (!res.ok) {
    const text = await res.text()
    throw new Error(`Resend error ${res.status}: ${text}`)
  }
  return true
}

async function sendWhatsAppReminder({ whatsapp, name, scheduledAt, type }) {
  const accountSid = process.env.TWILIO_ACCOUNT_SID
  const authToken = process.env.TWILIO_AUTH_TOKEN
  const fromRaw = process.env.TWILIO_WHATSAPP_FROM

  if (!accountSid || !authToken || !fromRaw) {
    console.warn('[demo] Twilio not configured — skipping WhatsApp')
    return false
  }

  const { timeLabel } = formatDemoDateTime(scheduledAt)
  const firstName = name.split(' ')[0] || name

  let body
  if (type === '24h') {
    body = `Hola ${firstName}, te recordamos que mañana tienes una demo de Kalyo a las ${timeLabel}. Link: ${MEET_LINK}`
  } else {
    body = `Hola ${firstName}, en 1 hora tienes tu demo de Kalyo. Link: ${MEET_LINK} ¡Nos vemos pronto!`
  }

  const from = fromRaw.startsWith('whatsapp:') ? fromRaw : `whatsapp:${fromRaw}`
  const to = whatsapp.startsWith('whatsapp:') ? whatsapp : `whatsapp:${whatsapp}`

  const params = new URLSearchParams({ From: from, To: to, Body: body })
  const res = await fetch(
    `https://api.twilio.com/2010-04-01/Accounts/${accountSid}/Messages.json`,
    {
      method: 'POST',
      headers: {
        Authorization: `Basic ${Buffer.from(`${accountSid}:${authToken}`).toString('base64')}`,
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: params,
    },
  )

  if (!res.ok) {
    const text = await res.text()
    throw new Error(`Twilio error ${res.status}: ${text}`)
  }
  return true
}

function escapeHtml(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
}

module.exports = {
  sendConfirmationEmail,
  sendWhatsAppReminder,
  formatDemoDateTime,
}
