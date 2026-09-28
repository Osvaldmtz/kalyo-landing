const assert = require('node:assert/strict')
const test = require('node:test')
const { buildDemoCalendarEventBody } = require('./demoCalendarEventBody')

test('demo calendar event includes lead, email, country, Meet and Bogota time', () => {
  const body = buildDemoCalendarEventBody({
    name: 'Javier Chaguaro',
    email: 'javier_chaguaro@hotmail.com',
    country: 'Ecuador',
    scheduledAt: '2026-09-28T14:00:00.000Z',
    meetLink: 'https://meet.google.com/pgd-dxmb-sfk',
  })

  assert.equal(body.summary, 'Demo Kalyo — Javier Chaguaro')
  assert.match(body.description, /Nombre: Javier Chaguaro/)
  assert.match(body.description, /Email: javier_chaguaro@hotmail.com/)
  assert.match(body.description, /País: Ecuador/)
  assert.match(body.description, /Meet: https:\/\/meet\.google\.com\/pgd-dxmb-sfk/)
  assert.match(body.description, /America\/Bogota/)
  assert.equal(body.location, 'https://meet.google.com/pgd-dxmb-sfk')
  assert.equal(body.start.timeZone, 'America/Bogota')
  assert.equal(body.end.timeZone, 'America/Bogota')
  assert.equal(body.start.dateTime, '2026-09-28T09:00:00')
  assert.equal(body.end.dateTime, '2026-09-28T09:30:00')
  assert.deepEqual(body.attendees, [{ email: 'javier_chaguaro@hotmail.com' }])
})
