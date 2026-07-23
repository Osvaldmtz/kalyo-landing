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
    console.warn('[demo] RESEND_API_KEY not set — skipping confirmation email')
    return { ok: false, reason: 'missing_api_key' }
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
  return { ok: true }
}

async function sendOwnerAlertEmail({
  name,
  email,
  whatsapp,
  country,
  interest,
  scheduledAt,
}) {
  const apiKey = process.env.RESEND_API_KEY
  const ownerEmail = process.env.DEMO_ALERT_EMAIL || 'osvamtz@gmail.com'
  if (!apiKey) {
    console.warn('[demo] RESEND_API_KEY not set — skipping owner alert')
    return { ok: false, reason: 'missing_api_key' }
  }

  const { dateLabel, timeLabel } = formatDemoDateTime(scheduledAt)
  const from = process.env.EMAIL_FROM || 'Kalyo <hola@kalyo.io>'
  const interestLine = interest
    ? `<tr><td style="padding:8px;color:#666">Interés</td><td style="padding:8px">${escapeHtml(interest)}</td></tr>`
    : ''

  const res = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${apiKey}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      from,
      to: ownerEmail,
      subject: `Nueva demo agendada — ${name} el ${dateLabel}`,
      html: `
        <div style="font-family:sans-serif;max-width:520px;margin:auto;padding:24px">
          <h2 style="color:#7C3DE3">Nueva demo agendada</h2>
          <table style="border-collapse:collapse;width:100%;margin:16px 0">
            <tr><td style="padding:8px;color:#666">Nombre</td><td style="padding:8px"><strong>${escapeHtml(name)}</strong></td></tr>
            <tr style="background:#f9f9f9"><td style="padding:8px;color:#666">Email</td><td style="padding:8px">${escapeHtml(email)}</td></tr>
            <tr><td style="padding:8px;color:#666">WhatsApp</td><td style="padding:8px">${escapeHtml(whatsapp)}</td></tr>
            <tr style="background:#f9f9f9"><td style="padding:8px;color:#666">País</td><td style="padding:8px">${escapeHtml(country)}</td></tr>
            ${interestLine}
            <tr><td style="padding:8px;color:#666">Fecha</td><td style="padding:8px">${escapeHtml(dateLabel)}</td></tr>
            <tr style="background:#f9f9f9"><td style="padding:8px;color:#666">Hora</td><td style="padding:8px">${escapeHtml(timeLabel)} (Colombia)</td></tr>
          </table>
          <p style="color:#888;font-size:12px">Meet: ${MEET_LINK}</p>
        </div>
      `,
    }),
  })

  if (!res.ok) {
    const text = await res.text()
    throw new Error(`Resend owner alert ${res.status}: ${text}`)
  }
  return { ok: true }
}

async function sendTwilioWhatsApp({ to, body }) {
  const accountSid = process.env.TWILIO_ACCOUNT_SID
  const authToken = process.env.TWILIO_AUTH_TOKEN
  const fromRaw = process.env.TWILIO_WHATSAPP_FROM

  if (!accountSid || !authToken || !fromRaw) {
    console.warn('[demo] Twilio not configured — skipping WhatsApp')
    return { ok: false, reason: 'missing_twilio_config' }
  }

  const from = fromRaw.startsWith('whatsapp:') ? fromRaw : `whatsapp:${fromRaw}`
  const toAddress = to.startsWith('whatsapp:') ? to : `whatsapp:${to}`

  const params = new URLSearchParams({ From: from, To: toAddress, Body: body })
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
  return { ok: true }
}

async function sendWhatsAppReminder({ whatsapp, name, scheduledAt, type }) {
  const { timeLabel } = formatDemoDateTime(scheduledAt)
  const firstName = name.split(' ')[0] || name

  let body
  if (type === '24h') {
    body = `Hola ${firstName}, te recordamos que mañana tienes una demo de Kalyo a las ${timeLabel}. Link: ${MEET_LINK}`
  } else {
    body = `Hola ${firstName}, en 1 hora tienes tu demo de Kalyo. Link: ${MEET_LINK} ¡Nos vemos pronto!`
  }

  const result = await sendTwilioWhatsApp({ to: whatsapp, body })
  return result.ok
}

async function sendOwnerAlertWhatsApp({
  name,
  email,
  whatsapp,
  country,
  interest,
  scheduledAt,
}) {
  const ownerWhatsApp = process.env.DEMO_ALERT_WHATSAPP || '+528114112000'
  const { dateLabel, timeLabel } = formatDemoDateTime(scheduledAt)
  const interestLine = interest ? `\nInterés: ${interest}` : ''

  const body = [
    'Nueva demo agendada en Kalyo',
    '',
    `Nombre: ${name}`,
    `Email: ${email}`,
    `WhatsApp: ${whatsapp}`,
    `País: ${country}${interestLine}`,
    `Fecha: ${dateLabel}`,
    `Hora: ${timeLabel} (Colombia)`,
    '',
    `Meet: ${MEET_LINK}`,
  ].join('\n')

  return sendTwilioWhatsApp({ to: ownerWhatsApp, body })
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
  sendOwnerAlertEmail,
  sendOwnerAlertWhatsApp,
  sendWhatsAppReminder,
  formatDemoDateTime,
}
