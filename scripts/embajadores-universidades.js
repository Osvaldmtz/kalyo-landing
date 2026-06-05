/**
 * Mensajes de confirmación por universidad.
 * Edita label, dia, hora y salon de cada una; ICESI ya está configurada.
 */
window.EMBAJADORES_UNIVERSIDADES = {
  icesi: {
    label: 'Universidad ICESI',
    mensaje:
      'Hola Embajador Kalyo, confirmamos tu asistencia a la reunión el próximo jueves 10 de junio a las 3:00 p.m. en la Universidad ICESI. ¡Gracias!'
  },
  del_valle: {
    label: 'Universidad del Valle',
    mensaje:
      'Hola Embajador Kalyo, confirmamos tu asistencia a la reunión el [día y fecha] a las [hora] en la Universidad del Valle, salón [nombre]. ¡Gracias!'
  },
  javeriana: {
    label: 'Universidad Javeriana — Cali',
    mensaje:
      'Hola Embajador Kalyo, confirmamos tu asistencia a la reunión el [día y fecha] a las [hora] en la Universidad Javeriana Cali, salón [nombre]. ¡Gracias!'
  },
  san_buenaventura: {
    label: 'Universidad San Buenaventura — Cali',
    mensaje:
      'Hola Embajador Kalyo, confirmamos tu asistencia a la reunión el [día y fecha] a las [hora] en la Universidad San Buenaventura Cali, salón [nombre]. ¡Gracias!'
  },
  uao: {
    label: 'Universidad Autónoma de Occidente (UAO)',
    mensaje:
      'Hola Embajador Kalyo, confirmamos tu asistencia a la reunión el [día y fecha] a las [hora] en la UAO, salón [nombre]. ¡Gracias!'
  },
  otro: {
    label: 'Otra universidad',
    mensaje:
      'Hola Embajador Kalyo, recibimos tu registro. El equipo de Kalyo te contactará pronto con la fecha, hora y lugar de tu reunión. ¡Gracias!'
  }
};

window.getMensajeEmbajador = function (id, otroTexto) {
  var data = window.EMBAJADORES_UNIVERSIDADES[id];
  if (!data) return '';
  if (id === 'otro' && otroTexto && otroTexto.trim()) {
    return (
      'Hola Embajador Kalyo, recibimos tu registro desde ' +
      otroTexto.trim() +
      '. El equipo de Kalyo te contactará pronto con la fecha, hora y lugar de tu reunión. ¡Gracias!'
    );
  }
  return data.mensaje;
};

window.getLabelUniversidad = function (id, otroTexto) {
  var data = window.EMBAJADORES_UNIVERSIDADES[id];
  if (!data) return '';
  if (id === 'otro' && otroTexto && otroTexto.trim()) {
    return 'Otra: ' + otroTexto.trim();
  }
  return data.label;
};
