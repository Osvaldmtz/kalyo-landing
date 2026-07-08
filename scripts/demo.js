(function () {
  const WEEKDAYS = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
  const MONTHS = [
    'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
    'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre',
  ]

  const COUNTRIES = [
    { code: '57', label: '🇨🇴 Colombia (+57)', country: 'Colombia' },
    { code: '52', label: '🇲🇽 México (+52)', country: 'México' },
    { code: '54', label: '🇦🇷 Argentina (+54)', country: 'Argentina' },
    { code: '56', label: '🇨🇱 Chile (+56)', country: 'Chile' },
    { code: '51', label: '🇵🇪 Perú (+51)', country: 'Perú' },
    { code: '593', label: '🇪🇨 Ecuador (+593)', country: 'Ecuador' },
    { code: '58', label: '🇻🇪 Venezuela (+58)', country: 'Venezuela' },
    { code: '507', label: '🇵🇦 Panamá (+507)', country: 'Panamá' },
    { code: '1', label: '🇺🇸 EE.UU. (+1)', country: 'Estados Unidos' },
  ]

  const state = {
    step: 1,
    availability: null,
    viewMonth: null,
    selectedDate: null,
    selectedTime: null,
    submitting: false,
    form: {
      name: '',
      email: '',
      countryCode: '57',
      phone: '',
      country: 'Colombia',
      interest: '',
    },
    booking: null,
  }

  const els = {
    step1: document.getElementById('step-1'),
    step2: document.getElementById('step-2'),
    step3: document.getElementById('step-3'),
    indicators: document.querySelectorAll('.demo-step-indicator'),
    error: document.getElementById('demo-error'),
    calendarMonth: document.getElementById('calendar-month'),
    calendarGrid: document.getElementById('calendar-grid'),
    slotsWrap: document.getElementById('slots-wrap'),
    slotsTitle: document.getElementById('slots-title'),
    slotsGrid: document.getElementById('slots-grid'),
    btnPrevMonth: document.getElementById('btn-prev-month'),
    btnNextMonth: document.getElementById('btn-next-month'),
    btnStep1Next: document.getElementById('btn-step1-next'),
    btnStep2Back: document.getElementById('btn-step2-back'),
    btnStep2Submit: document.getElementById('btn-step2-submit'),
    confirmSummary: document.getElementById('confirm-summary'),
  }

  function showError(msg) {
    if (!msg) {
      els.error.classList.add('demo-hidden')
      els.error.textContent = ''
      return
    }
    els.error.textContent = msg
    els.error.classList.remove('demo-hidden')
  }

  function setStep(step) {
    state.step = step
    els.step1.classList.toggle('demo-hidden', step !== 1)
    els.step2.classList.toggle('demo-hidden', step !== 2)
    els.step3.classList.toggle('demo-hidden', step !== 3)
    els.indicators.forEach((el, i) => {
      el.classList.toggle('active', i + 1 === step)
      el.classList.toggle('done', i + 1 < step)
    })
    showError('')
  }

  function parseIsoDate(iso) {
    const [y, m, d] = iso.split('-').map(Number)
    return new Date(y, m - 1, d)
  }

  function monthKey(date) {
    return `${date.getFullYear()}-${date.getMonth()}`
  }

  function getMonthCells(year, month) {
    const first = new Date(year, month, 1)
    const startPad = (first.getDay() + 6) % 7
    const daysInMonth = new Date(year, month + 1, 0).getDate()
    const cells = []

    for (let i = 0; i < startPad; i++) cells.push({ empty: true })
    for (let d = 1; d <= daysInMonth; d++) {
      const mm = String(month + 1).padStart(2, '0')
      const dd = String(d).padStart(2, '0')
      cells.push({ empty: false, date: `${year}-${mm}-${dd}`, day: d })
    }
    return cells
  }

  function dayInfo(dateStr) {
    return state.availability?.days?.find((d) => d.date === dateStr)
  }

  function renderCalendar() {
    if (!state.viewMonth || !state.availability) return
    const [y, m] = state.viewMonth.split('-').map(Number)
    els.calendarMonth.textContent = `${MONTHS[m]} ${y}`

    const cells = getMonthCells(y, m)
    els.calendarGrid.innerHTML = ''

    cells.forEach((cell) => {
      const btn = document.createElement('button')
      btn.type = 'button'
      btn.className = 'demo-day'

      if (cell.empty) {
        btn.classList.add('empty')
        els.calendarGrid.appendChild(btn)
        return
      }

      const info = dayInfo(cell.date)
      const hasSlots = info && info.availableCount > 0
      btn.textContent = String(cell.day)

      if (hasSlots) {
        btn.classList.add('available')
        if (state.selectedDate === cell.date) btn.classList.add('selected')
        btn.addEventListener('click', () => selectDate(cell.date))
      } else {
        btn.classList.add('disabled')
        btn.disabled = true
      }

      els.calendarGrid.appendChild(btn)
    })

    const availableMonths = new Set(
      state.availability.days.map((d) => {
        const dt = parseIsoDate(d.date)
        return monthKey(dt)
      }),
    )
    const current = monthKey(new Date(y, m, 1))
    const months = Array.from(availableMonths).sort()
    const idx = months.indexOf(current)
    els.btnPrevMonth.disabled = idx <= 0
    els.btnNextMonth.disabled = idx < 0 || idx >= months.length - 1
  }

  function selectDate(dateStr) {
    state.selectedDate = dateStr
    state.selectedTime = null
    renderCalendar()
    renderSlots()
    updateSubmitButton()
  }

  function renderSlots() {
    if (!state.selectedDate) {
      els.slotsWrap.classList.add('demo-hidden')
      return
    }

    const info = dayInfo(state.selectedDate)
    if (!info) {
      els.slotsWrap.classList.add('demo-hidden')
      return
    }

    const dt = parseIsoDate(state.selectedDate)
    els.slotsTitle.textContent = `Horarios · ${dt.toLocaleDateString('es-CO', {
      weekday: 'long',
      day: 'numeric',
      month: 'long',
    })}`

    els.slotsGrid.innerHTML = ''
    info.slots.forEach((slot) => {
      const btn = document.createElement('button')
      btn.type = 'button'
      btn.className = 'demo-slot'
      btn.textContent = slot.label

      if (slot.available) {
        btn.classList.add('available')
        if (state.selectedTime === slot.time) btn.classList.add('selected')
        btn.addEventListener('click', () => {
          state.selectedTime = slot.time
          renderSlots()
          updateSubmitButton()
        })
      } else {
        btn.classList.add('busy')
        btn.disabled = true
      }

      els.slotsGrid.appendChild(btn)
    })

    els.slotsWrap.classList.remove('demo-hidden')
  }

  function updateSubmitButton() {
    els.btnStep2Submit.disabled = !(state.selectedDate && state.selectedTime) || state.submitting
  }

  function validateStep1() {
    const name = document.getElementById('input-name').value.trim()
    const email = document.getElementById('input-email').value.trim()
    const phone = document.getElementById('input-phone').value.trim()
    const countryCode = document.getElementById('input-country-code').value
    const countrySelect = document.getElementById('input-country')
    const interest = document.getElementById('input-interest').value.trim()

    if (name.length < 2) return 'Ingresa tu nombre completo'
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return 'Ingresa un email válido'
    if (phone.replace(/\D/g, '').length < 8) return 'Ingresa un WhatsApp válido'

    state.form = {
      name,
      email,
      countryCode,
      phone,
      country: countrySelect.value,
      interest,
    }
    return null
  }

  async function loadAvailability() {
    const res = await fetch('/api/demo/slots')
    if (!res.ok) throw new Error('No se pudieron cargar los horarios')
    state.availability = await res.json()

    if (state.availability.days.length > 0) {
      const first = parseIsoDate(state.availability.days[0].date)
      state.viewMonth = monthKey(first)
    }
    renderCalendar()
  }

  async function submitBooking() {
    if (!state.selectedDate || !state.selectedTime) return

    state.submitting = true
    updateSubmitButton()
    showError('')

    try {
      const res = await fetch('/api/demo/book', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          ...state.form,
          date: state.selectedDate,
          time: state.selectedTime,
        }),
      })

      const data = await res.json()
      if (!res.ok) {
        showError(data.error || 'No se pudo agendar')
        if (res.status === 409) await loadAvailability()
        return
      }

      state.booking = data
      els.confirmSummary.innerHTML = `
        <p><strong>${escapeHtml(state.form.name)}</strong></p>
        <p>${escapeHtml(data.dateLabel)}</p>
        <p>${escapeHtml(data.timeLabel)} (hora Colombia)</p>
      `
      setStep(3)

      if (window.kalyoTrack && typeof window.kalyoTrack.demoConfirmed === 'function') {
        window.kalyoTrack.demoConfirmed()
      }
    } catch (err) {
      showError('Error de conexión. Intenta de nuevo.')
    } finally {
      state.submitting = false
      updateSubmitButton()
    }
  }

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
  }

  function initCountrySelects() {
    const codeSelect = document.getElementById('input-country-code')
    const countrySelect = document.getElementById('input-country')

    COUNTRIES.forEach((c) => {
      const opt1 = document.createElement('option')
      opt1.value = c.code
      opt1.textContent = c.label
      codeSelect.appendChild(opt1)

      const opt2 = document.createElement('option')
      opt2.value = c.country
      opt2.textContent = c.country
      countrySelect.appendChild(opt2)
    })

    codeSelect.addEventListener('change', () => {
      const match = COUNTRIES.find((c) => c.code === codeSelect.value)
      if (match) countrySelect.value = match.country
    })

    countrySelect.addEventListener('change', () => {
      const match = COUNTRIES.find((c) => c.country === countrySelect.value)
      if (match) codeSelect.value = match.code
    })
  }

  function bindEvents() {
    els.btnStep1Next.addEventListener('click', () => {
      const err = validateStep1()
      if (err) return showError(err)
      setStep(2)
    })

    els.btnStep2Back.addEventListener('click', () => setStep(1))

    els.btnStep2Submit.addEventListener('click', submitBooking)

    els.btnPrevMonth.addEventListener('click', () => {
      const months = Array.from(
        new Set(
          state.availability.days.map((d) => monthKey(parseIsoDate(d.date))),
        ),
      ).sort()
      const idx = months.indexOf(state.viewMonth)
      if (idx > 0) {
        state.viewMonth = months[idx - 1]
        renderCalendar()
      }
    })

    els.btnNextMonth.addEventListener('click', () => {
      const months = Array.from(
        new Set(
          state.availability.days.map((d) => monthKey(parseIsoDate(d.date))),
        ),
      ).sort()
      const idx = months.indexOf(state.viewMonth)
      if (idx < months.length - 1) {
        state.viewMonth = months[idx + 1]
        renderCalendar()
      }
    })
  }

  async function init() {
    initCountrySelects()
    bindEvents()

    const weekdaysEl = document.getElementById('weekdays-row')
    WEEKDAYS.forEach((d) => {
      const span = document.createElement('span')
      span.textContent = d
      weekdaysEl.appendChild(span)
    })

    try {
      await loadAvailability()
    } catch (err) {
      showError('No se pudieron cargar los horarios. Recarga la página.')
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init)
  } else {
    init()
  }
})()
