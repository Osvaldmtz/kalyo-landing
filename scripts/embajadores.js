(function () {
  const form = document.getElementById('embajadores-form');
  if (!form) return;

  const submitBtn = form.querySelector('.emb-submit');

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

  form.addEventListener('submit', function (e) {
    clearFieldErrors();
    let valid = true;

    const nombre = form.querySelector('#nombre');
    const cedula = form.querySelector('#cedula');
    const telefono = form.querySelector('#telefono');
    const correo = form.querySelector('#correo');
    const universidad = form.querySelector('#universidad');
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
    if (!universidad.value.trim()) {
      showFieldError(universidad, 'Indica tu universidad.');
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

    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.textContent = 'Enviando…';
    }

    if (typeof gtag === 'function') {
      gtag('event', 'embajador_registro_enviado', {
        event_category: 'embajadores',
        event_label: 'formulario_evento'
      });
    }
  });

  form.querySelectorAll('input, select').forEach((input) => {
    input.addEventListener('input', function () {
      input.removeAttribute('aria-invalid');
      const err = input.closest('.emb-field')?.querySelector('.emb-field-error');
      if (err) err.classList.remove('is-visible');
    });
  });
})();
