(function () {
  const form = document.getElementById('embajadores-form');
  if (!form) return;

  const submitBtn = form.querySelector('.emb-submit');
  const universidadSelect = form.querySelector('#universidad');
  const universidadEmail = form.querySelector('#universidad-email');
  const universidadId = form.querySelector('#universidad-id');
  const otroWrap = form.querySelector('#universidad-otro-wrap');
  const otroInput = form.querySelector('#universidad-otro');
  const STORAGE_KEY = 'embajador_universidad_id';
  const STORAGE_OTRO_KEY = 'embajador_universidad_otro';

  function showFieldError(input, message) {
    const field = input.closest('.emb-field');
    if (!field) return;
    const err = field.querySelector('.emb-field-error');
    input.setAttribute('aria-invalid', 'true');
    if (err) {
      err.textContent = message;
      err.classList.add('is-visible');
    }
  }

  function clearFieldErrors() {
    form.querySelectorAll('[aria-invalid]').forEach((el) => el.removeAttribute('aria-invalid'));
    form.querySelectorAll('.emb-field-error').forEach((el) => {
      el.textContent = '';
      el.classList.remove('is-visible');
    });
  }

  function validateEmail(value) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
  }

  function validatePhone(value) {
    const digits = value.replace(/\D/g, '');
    return digits.length >= 10;
  }

  function toggleOtroField() {
    if (!otroWrap || !universidadSelect) return;
    const isOtro = universidadSelect.value === 'otro';
    otroWrap.hidden = !isOtro;
    if (otroInput) {
      otroInput.required = isOtro;
      if (!isOtro) otroInput.value = '';
    }
  }

  function syncUniversidadEmail() {
    if (!universidadSelect) return;
    const otro = otroInput ? otroInput.value : '';
    const label =
      typeof getLabelUniversidad === 'function'
        ? getLabelUniversidad(universidadSelect.value, otro)
        : universidadSelect.options[universidadSelect.selectedIndex]?.text || '';
    if (universidadEmail) universidadEmail.value = label;
    if (universidadId) universidadId.value = universidadSelect.value;
  }

  function buildSheetFormData() {
    const nombre = form.querySelector('#nombre');
    const cedula = form.querySelector('#cedula');
    const telefono = form.querySelector('#telefono');
    const correo = form.querySelector('#correo');
    const carrera = form.querySelector('#carrera');
    const fd = new FormData();
    fd.append('nombre', nombre.value.trim());
    fd.append('cedula', cedula.value.trim());
    fd.append('telefono', telefono.value.trim());
    fd.append('correo', correo.value.trim());
    fd.append('carrera', carrera.value.trim());
    fd.append('universidad', universidadEmail ? universidadEmail.value : '');
    fd.append('universidad_id', universidadId ? universidadId.value : '');
    fd.append('universidad_otro', otroInput ? otroInput.value.trim() : '');
    return fd;
  }

  function sendToGoogleSheet() {
    const url = window.EMBAJADORES_CONFIG && window.EMBAJADORES_CONFIG.googleSheetScriptUrl;
    if (!url) return Promise.resolve();
    return fetch(url, { method: 'POST', mode: 'no-cors', body: buildSheetFormData() }).catch(function () {
      /* no-cors: la fila puede haberse guardado igual */
    });
  }

  if (universidadSelect) {
    universidadSelect.addEventListener('change', function () {
      universidadSelect.removeAttribute('aria-invalid');
      const err = universidadSelect.closest('.emb-field')?.querySelector('.emb-field-error');
      if (err) err.classList.remove('is-visible');
      toggleOtroField();
      syncUniversidadEmail();
    });
    toggleOtroField();
  }

  if (otroInput) {
    otroInput.addEventListener('input', function () {
      otroInput.removeAttribute('aria-invalid');
      const err = otroInput.closest('.emb-field')?.querySelector('.emb-field-error');
      if (err) err.classList.remove('is-visible');
      syncUniversidadEmail();
    });
  }

  form.addEventListener('submit', function (e) {
    clearFieldErrors();
    let valid = true;

    const nombre = form.querySelector('#nombre');
    const cedula = form.querySelector('#cedula');
    const telefono = form.querySelector('#telefono');
    const correo = form.querySelector('#correo');
    const carrera = form.querySelector('#carrera');
    const consent = form.querySelector('#consent');

    if (!nombre.value.trim()) {
      showFieldError(nombre, 'Escribe tu nombre completo.');
      valid = false;
    }
    if (!cedula.value.trim()) {
      showFieldError(cedula, 'Indica tu número de cédula o identificación.');
      valid = false;
    }
    if (!validatePhone(telefono.value)) {
      showFieldError(telefono, 'Ingresa un teléfono válido (mínimo 10 dígitos).');
      valid = false;
    }
    if (!validateEmail(correo.value.trim())) {
      showFieldError(correo, 'Ingresa un correo electrónico válido.');
      valid = false;
    }
    if (!universidadSelect || !universidadSelect.value) {
      showFieldError(universidadSelect, 'Selecciona tu universidad.');
      valid = false;
    }
    if (universidadSelect && universidadSelect.value === 'otro' && otroInput && !otroInput.value.trim()) {
      showFieldError(otroInput, 'Escribe el nombre de tu universidad.');
      valid = false;
    }
    if (!carrera.value.trim()) {
      showFieldError(carrera, 'Indica tu carrera.');
      valid = false;
    }
    if (!consent.checked) {
      e.preventDefault();
      const consentField = consent.closest('.emb-consent');
      if (consentField) {
        consentField.style.outline = '2px solid #DC2626';
        consentField.style.outlineOffset = '4px';
        consentField.style.borderRadius = '6px';
        setTimeout(() => {
          consentField.style.outline = '';
          consentField.style.outlineOffset = '';
        }, 3000);
      }
      valid = false;
    }

    if (!valid) {
      e.preventDefault();
      const firstInvalid = form.querySelector('[aria-invalid]') || consent;
      if (firstInvalid) firstInvalid.focus();
      return;
    }

    e.preventDefault();
    syncUniversidadEmail();
    var replyto = form.querySelector('#formsubmit-replyto');
    if (replyto && correo) replyto.value = correo.value.trim();
    try {
      sessionStorage.setItem(STORAGE_KEY, universidadSelect.value);
      sessionStorage.setItem(STORAGE_OTRO_KEY, otroInput ? otroInput.value.trim() : '');
    } catch (err) {
      /* sessionStorage no disponible */
    }

    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.textContent = 'Enviando…';
    }

    if (typeof gtag === 'function') {
      gtag('event', 'embajador_registro_enviado', {
        event_category: 'embajadores',
        event_label: universidadSelect.value
      });
    }

    sendToGoogleSheet().finally(function () {
      form.submit();
    });
  });

  form.querySelectorAll('input:not([type="hidden"]), select').forEach((input) => {
    input.addEventListener('input', function () {
      input.removeAttribute('aria-invalid');
      const err = input.closest('.emb-field')?.querySelector('.emb-field-error');
      if (err) err.classList.remove('is-visible');
    });
    input.addEventListener('change', function () {
      input.removeAttribute('aria-invalid');
      const err = input.closest('.emb-field')?.querySelector('.emb-field-error');
      if (err) err.classList.remove('is-visible');
    });
  });

  window.showEmbajadorSuccess = function () {
    var panel = document.getElementById('emb-success-panel');
    var msgEl = document.getElementById('emb-success-message');
    if (!panel || !msgEl) return;

    var id = '';
    var otro = '';
    try {
      id = sessionStorage.getItem(STORAGE_KEY) || '';
      otro = sessionStorage.getItem(STORAGE_OTRO_KEY) || '';
      sessionStorage.removeItem(STORAGE_KEY);
      sessionStorage.removeItem(STORAGE_OTRO_KEY);
    } catch (e) {
      /* ignore */
    }

    var mensaje =
      typeof getMensajeEmbajador === 'function' && id
        ? getMensajeEmbajador(id, otro)
        : 'Te contactaremos pronto con los detalles del evento.';

    msgEl.textContent = mensaje;

    var brand = document.querySelector('.emb-brand');
    var formEl = document.getElementById('embajadores-form');
    if (brand) {
      brand.querySelector('.emb-eyebrow').hidden = true;
      brand.querySelector('h1').hidden = true;
      brand.querySelector('.emb-lead').hidden = true;
    }
    if (formEl) formEl.hidden = true;
    panel.hidden = false;

    if (typeof gtag === 'function') {
      gtag('event', 'embajador_registro_completado', {
        event_category: 'embajadores',
        event_label: id || 'desconocido'
      });
    }
  };
})();
