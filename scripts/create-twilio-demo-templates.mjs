#!/usr/bin/env node
/**
 * Crea plantillas HSM de Twilio Content API para recordatorios de demo
 * y las envía a aprobación de WhatsApp (categoría UTILITY).
 *
 * Uso:
 *   TWILIO_ACCOUNT_SID=AC... TWILIO_AUTH_TOKEN=... node scripts/create-twilio-demo-templates.mjs
 *
 * También lee .env.local si existe.
 */

import { readFileSync, writeFileSync, existsSync } from 'node:fs'
import { dirname, join } from 'node:path'
import { fileURLToPath } from 'node:url'

const __dirname = dirname(fileURLToPath(import.meta.url))
const root = join(__dirname, '..')

function loadEnvFile(path) {
  if (!existsSync(path)) return
  for (const line of readFileSync(path, 'utf8').split('\n')) {
    const trimmed = line.trim()
    if (!trimmed || trimmed.startsWith('#') || !trimmed.includes('=')) continue
    const eq = trimmed.indexOf('=')
    const key = trimmed.slice(0, eq)
    let value = trimmed.slice(eq + 1).trim()
    if (
      (value.startsWith('"') && value.endsWith('"')) ||
      (value.startsWith("'") && value.endsWith("'"))
    ) {
      value = value.slice(1, -1)
    }
    if (!process.env[key]) process.env[key] = value
  }
}

loadEnvFile(join(root, '.env.local'))

const accountSid = process.env.TWILIO_ACCOUNT_SID
const authToken = process.env.TWILIO_AUTH_TOKEN

if (!accountSid || !authToken) {
  console.error('Faltan TWILIO_ACCOUNT_SID y/o TWILIO_AUTH_TOKEN.')
  process.exit(1)
}

const authHeader = `Basic ${Buffer.from(`${accountSid}:${authToken}`).toString('base64')}`

async function twilioJson(url, options = {}) {
  const res = await fetch(url, {
    ...options,
    headers: {
      Authorization: authHeader,
      'Content-Type': 'application/json',
      ...(options.headers || {}),
    },
  })
  const text = await res.text()
  const data = text ? JSON.parse(text) : {}
  if (!res.ok) {
    throw new Error(`${res.status} ${url}: ${JSON.stringify(data)}`)
  }
  return data
}

const TEMPLATES = [
  {
    key: '24h',
    envVar: 'TWILIO_TEMPLATE_DEMO_REMINDER_24H',
    payload: {
      friendly_name: 'kalyo_demo_reminder_24h',
      language: 'es',
      variables: {
        1: 'María',
        2: '10:00 a.m.',
        3: 'https://meet.google.com/pgd-dxmb-sfk',
      },
      types: {
        'twilio/text': {
          body: 'Hola {{1}}, te recordamos que mañana tienes una demo de Kalyo a las {{2}}. Únete aquí: {{3}}',
        },
      },
    },
  },
  {
    key: '1h',
    envVar: 'TWILIO_TEMPLATE_DEMO_REMINDER_1H',
    payload: {
      friendly_name: 'kalyo_demo_reminder_1h',
      language: 'es',
      variables: {
        1: 'María',
        2: 'https://meet.google.com/pgd-dxmb-sfk',
      },
      types: {
        'twilio/text': {
          body: 'Hola {{1}}, en 1 hora tienes tu demo de Kalyo. Únete aquí: {{2}} ¡Nos vemos pronto!',
        },
      },
    },
  },
]

const results = {}

for (const tpl of TEMPLATES) {
  console.log(`\nCreando plantilla ${tpl.key}...`)
  const created = await twilioJson('https://content.twilio.com/v1/Content', {
    method: 'POST',
    body: JSON.stringify(tpl.payload),
  })

  console.log(`Enviando a aprobación WhatsApp (${created.sid})...`)
  const approval = await twilioJson(
    `https://content.twilio.com/v1/Content/${created.sid}/ApprovalRequests/whatsapp`,
    {
      method: 'POST',
      body: JSON.stringify({
        name: tpl.payload.friendly_name,
        category: 'UTILITY',
      }),
    },
  )

  results[tpl.key] = {
    sid: created.sid,
    friendly_name: created.friendly_name,
    envVar: tpl.envVar,
    approval_status: approval.status,
  }

  console.log(`  SID: ${created.sid}`)
  console.log(`  Aprobación WhatsApp: ${approval.status}`)
}

const outPath = join(root, 'scripts/twilio-template-sids.json')
writeFileSync(outPath, `${JSON.stringify(results, null, 2)}\n`)

console.log('\n--- Variables para Vercel ---')
for (const tpl of TEMPLATES) {
  console.log(`${tpl.envVar}=${results[tpl.key].sid}`)
}
console.log(`\nGuardado en ${outPath}`)
