/**
 * KALYO — Registro Embajadores → Google Sheets
 *
 * Configuración (5 min, cuenta osvamtz@gmail.com):
 * 1. sheets.google.com → Hoja nueva "Kalyo Embajadores"
 * 2. Extensiones → Apps Script → pegar este archivo
 * 3. Ejecutar setupSheet (autorizar permisos)
 * 4. Implementar → Nueva implementación → Aplicación web
 *    - Ejecutar como: Yo
 *    - Quién puede acceder: Cualquier persona
 * 5. Copiar URL de .../exec en scripts/embajadores-config.js → googleSheetScriptUrl
 */

var NOTIFY_EMAIL = 'osvamtz@gmail.com';
var SHEET_NAME = 'Inscritos';

function setupSheet() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);
  }
  sheet.clear();
  sheet
    .getRange(1, 1, 1, 9)
    .setValues([
      [
        'Fecha',
        'Nombre',
        'Cédula',
        'Teléfono',
        'Correo',
        'Universidad',
        'ID universidad',
        'Universidad (otro)',
        'Carrera'
      ]
    ]);
  sheet.getRange(1, 1, 1, 9).setFontWeight('bold');
  sheet.setFrozenRows(1);
  SpreadsheetApp.flush();
}

function doPost(e) {
  try {
    var p = e.parameter;
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss.getSheetByName(SHEET_NAME);
    if (!sheet) {
      setupSheet();
      sheet = ss.getSheetByName(SHEET_NAME);
    }
    if (sheet.getLastRow() === 0) {
      setupSheet();
    }

    sheet.appendRow([
      new Date(),
      p.nombre || '',
      p.cedula || '',
      p.telefono || '',
      p.correo || '',
      p.universidad || '',
      p.universidad_id || '',
      p.universidad_otro || '',
      p.carrera || ''
    ]);

    return ContentService.createTextOutput(
      JSON.stringify({ ok: true })
    ).setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService.createTextOutput(
      JSON.stringify({ ok: false, error: String(err) })
    ).setMimeType(ContentService.MimeType.JSON);
  }
}

function doGet() {
  return ContentService.createTextOutput('Kalyo embajadores — endpoint activo');
}
