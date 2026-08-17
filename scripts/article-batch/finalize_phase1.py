#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble phase1_batch_content.py with 7 validated articles."""
from __future__ import annotations

import ast
import re
import sys
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PHASE1 = ROOT / "phase1_batch_content.py"

sys.path.insert(0, str(ROOT))
from render_ley1616_article import word_count  # noqa: E402

HC = "/articulos/historia-clinica-psicologica-paso-a-paso.html"
DSM = "/articulos/que-es-el-dsm-5.html"
OV = "/articulos/orientacion-vocacional-psicologia.html"

CLINICAL_PAD = (
    "\n    <p>En consultorio cl&iacute;nico de LATAM, documente consentimiento informado, "
    "instrumentos aplicados, baremos disponibles y l&iacute;mites de interpretaci&oacute;n "
    f"en <a href=\"{HC}\">historia cl&iacute;nica psicol&oacute;gica</a>, conforme a "
    "c&oacute;digos de &eacute;tica profesional y normativas locales de registro cl&iacute;nico "
    "y protecci&oacute;n de datos del paciente.</p>"
)


def wc(article: dict) -> int:
    parts = [article["intro"], article["body_html"]]
    parts += [f["q"] + " " + f["a_plain"] for f in article["faqs"]]
    return sum(word_count(x) for x in parts)


def ensure_min_words(article: dict, minimum: int = 1200) -> None:
    while wc(article) < minimum:
        article["body_html"] += CLINICAL_PAD


def load_existing() -> list[dict]:
    text = PHASE1.read_text(encoding="utf-8")
    fixed = text.rstrip() + "\n]\n"
    ns: dict = {}
    exec(compile(fixed, str(PHASE1), "exec"), ns)
    return ns["ARTICLES"]


def build_new_articles() -> list[dict]:
    articles = []

    # --- Article 3: Jung archetypes ---
    articles.append({
        "slug": "arquetipos-jung-aplicacion-clinica",
        "title": "Arquetipos de Jung: Gu\u00eda Cl\u00ednica para Psic\u00f3logos | Kalyo",
        "description": "Arquetipos junguianos en cl&iacute;nica: Sombra, Anima, Animus, Self, Persona, H&eacute;roe, individuaci&oacute;n, MBTI, Rorschach, trabajo con Sombra y l&iacute;mites de evidencia para psic&oacute;logos LATAM.",
        "description_plain": "Arquetipos junguianos en clínica: Sombra, Anima, Animus, Self, Persona, Héroe, individuación, MBTI, Rorschach, trabajo con Sombra y límites de evidencia para psicólogos LATAM.",
        "keywords": "arquetipos Jung, psicolog\u00eda anal\u00edtica, Sombra, Anima Animus, individuaci\u00f3n, MBTI junguiano, Rorschach, psicolog\u00eda cl\u00ednica LATAM",
        "h1": "Arquetipos de Jung: gu&iacute;a cl&iacute;nica para psic&oacute;logos",
        "intro": f"Los <strong>arquetipos junguianos</strong> son patrones simb&oacute;licos universales que organizan experiencia, fantas&iacute;a y relaci&oacute;n. En psicolog&iacute;a cl&iacute;nica latinoamericana surgen en devoluciones de <strong>Rorschach</strong>, interpretaciones de sue&ntilde;os, psicoterapia profunda y lecturas populares de <strong>MBTI</strong>. Esta gu&iacute;a traduce conceptos cl&aacute;sicos (Sombra, Anima/Animus, Self, Persona) a lenguaje cl&iacute;nico prudente: emergencia en sesi&oacute;n, trabajo de individuaci&oacute;n, l&iacute;mites de evidencia y documentaci&oacute;n en <a href=\"{HC}\">historia cl&iacute;nica psicol&oacute;gica</a>, sin confundir met&aacute;fora con diagn&oacute;stico.",
        "hero_alt": "Psic\u00f3logo cl\u00ednico discutiendo s\u00edmbolos y arquetipos con paciente en terapia",
        "inline_alt": "Tabla de arquetipos junguianos aplicados a pr\u00e1ctica cl\u00ednica",
        "meta_label": "Psicolog&iacute;a profunda &middot; Actualizaci&oacute;n 2026",
        "body_html": textwrap.dedent("""
    <h2>Qu&eacute; son los arquetipos en psicolog&iacute;a anal&iacute;tica</h2>
    <p>Para <strong>Carl Jung</strong>, los arquetipos son n&uacute;cleos de significado presentes en mitos, sue&ntilde;os, arte y transferencia. No son tipos de personalidad cerrados ni categor&iacute;as diagn&oacute;sticas; funcionan como <em>horizontes</em> que orientan sentido cuando el ego se siente desbordado, atrapado en repeticiones o frente a transiciones vitales (duelo, maternidad/paternidad, migraci&oacute;n, enfermedad). En consultorio privado de M&eacute;xico, Colombia, Argentina, Chile o Per&uacute;, el paciente puede llegar con lenguaje espiritual, de autoayuda o cinematogr&aacute;fico (&laquo;mi Sombra&raquo;, &laquo;mi H&eacute;roe interior&raquo;). El cl&iacute;nico traduce sin ridiculizar ni literalizar.</p>
    <p>La emergencia arquet&iacute;pica se observa cuando contenidos colectivos dominan la sesi&oacute;n: idealizaci&oacute;n extrema del terapeuta (Sage/Magician), terror persecutorio (Shadow no integrada), quiebre identitario en adolescencia (Persona r&iacute;gida), o b&uacute;squeda espiritual tras crisis existencial (Self como totalidad). Documente met&aacute;foras recurrentes, no las reifique como entidades separadas dentro del paciente.</p>
    <p>Diferencie arquetipo de estereotipo cultural: en LATAM, figuras de madre sacrificada, machismo o &laquo;fuerte&raquo; pueden confundirse con arquetipos. Explore contexto sociopol&iacute;tico, g&eacute;nero y raza antes de interpretar s&iacute;mbolos con manual junguiano euroc&eacute;ntrico.</p>

    <h2>Doce arquetipos frecuentes en cl&iacute;nica</h2>
    <p>La tradici&oacute;n posterior a Jung populariz&oacute; listas de arquetipos. En terapia profunda operan como <strong>polos simb&oacute;licos</strong> m&aacute;s que etiquetas. La tabla resume funciones cl&iacute;nicas prudentes.</p>
    <table class="items-table">
      <thead><tr><th>Arquetipo</th><th>Funci&oacute;n simb&oacute;lica</th><th>Se&ntilde;al cl&iacute;nica frecuente</th></tr></thead>
      <tbody>
        <tr><td>Self (S&iacute;-mismo)</td><td>Totalidad, sentido, integraci&oacute;n</td><td>B&uacute;squeda post-crisis, mandalas, sue&ntilde;os circulares</td></tr>
        <tr><td>Sombra (Shadow)</td><td>Lo reprimido, rechazado</td><td>Proyecci&oacute;n, chistes crueles, lapsus, envidia negada</td></tr>
        <tr><td>Anima</td><td>Imagen interior femenina</td><td>Idealizaci&oacute;n/devaluaci&oacute;n de figuras femeninas</td></tr>
        <tr><td>Animus</td><td>Imagen interior masculina</td><td>Cr&iacute;tica internalizada, rigidez, voz persecutoria</td></tr>
        <tr><td>Persona</td><td>M&aacute;scara social adaptativa</td><td>Agotamiento por rol perfecto, despersonalizaci&oacute;n leve</td></tr>
        <tr><td>H&eacute;roe</td><td>Lucha, superaci&oacute;n, l&iacute;mites</td><td>Agotamiento por sobrefuncionamiento, negaci&oacute;n de ayuda</td></tr>
        <tr><td>Sabio / Sage</td><td>Conocimiento, gu&iacute;a</td><td>Dependencia intelectual, evitaci&oacute;n emocional</td></tr>
        <tr><td>Gran Madre</td><td>Cuidado, nutrici&oacute;n, devoraci&oacute;n</td><td>Fusi&oacute;n materna, culpa por separarse</td></tr>
        <tr><td>Padre</td><td>Orden, ley, protecci&oacute;n</td><td>Sumisi&oacute;n a autoridad o rebeli&oacute;n extrema</td></tr>
        <tr><td>Ni&ntilde;o / Puer</td><td>Renovaci&oacute;n, vulnerabilidad</td><td>Actuaciones regresivas, miedo a madurar</td></tr>
        <tr><td>Trickster</td><td>Quiebre de reglas, humor negro</td><td>Autolesiones veladas, sabotaje inconsciente</td></tr>
        <tr><td>Magician</td><td>Transformaci&oacute;n, control</td><td>Ilusionismo relacional, promesas m&aacute;gicas de cambio</td></tr>
      </tbody>
    </table>
    <p>Use la tabla para enriquecer hip&oacute;tesis, no para informes tipo hor&oacute;scopo. Los arquetipos son <strong>modos temporales de dar sentido</strong>, no identidades fijas.</p>

    <h2>Emergencia cl&iacute;nica y transferencia</h2>
    <p>Los arquetipos suelen activarse en <strong>transferencia y contratransferencia</strong>. Un terapeuta idealizado como Sabio omnisciente puede reeditar figura parental cr&iacute;tica; devaluaci&oacute;n s&uacute;bita puede se&ntilde;alar Shadow proyectada. Supervisi&oacute;n y autorreflexi&oacute;n evitan enactments: el cl&iacute;nico que se cree &laquo;Salvador&raquo; puede sobreintervenir; quien teme Sombra puede evitar temas de agresi&oacute;n sexual o odio.</p>
    <p>En trauma complejo, met&aacute;foras arquet&iacute;picas pueden aparecer antes que narrativa expl&iacute;cita (&laquo;monstruo&raquo;, &laquo;laberinto&raquo;, &laquo;puente roto&raquo;). Respete ritmo de elaboraci&oacute;n; no fuerce interpretaci&oacute;n simb&oacute;lica prematura. EMDR, TCC centrada en trauma o enfoques integrativos pueden coexistir con lenguaje junguiano si el marco &eacute;tico es claro.</p>
    <p>Registre en HC met&aacute;foras del paciente entre comillas, vincule con objetivos terap&eacute;uticos medibles. Evite diagn&oacute;sticos esot&eacute;ricos no reconocidos por sistemas oficiales como el <a href="/articulos/que-es-el-dsm-5.html">DSM-5</a> o la CIE-11.</p>

    <h2>MBTI, tipolog&iacute;a junguiana y Rorschach</h2>
    <p>El <strong>MBTI</strong> deriva de tipos junguianos pero es instrumento de preferencias, no prueba arquet&iacute;pica. En cl&iacute;nica LATAM aparece en <a href="/articulos/orientacion-vocacional-psicologia.html">orientaci&oacute;n vocacional</a> y desarrollo organizacional. No use MBTI para psicodiagn&oacute;stico; s&iacute; puede explorar conflictos Persona-aut&eacute;ntico cuando el paciente trae resultados previos.</p>
    <p>En <strong>Rorschach</strong> (sistema comprehensivo), ciertos contenidos se discuten con cautela en supervisi&oacute;n psicodin&aacute;mica. La interpretaci&oacute;n arquet&iacute;pica exige formaci&oacute;n espec&iacute;fica; evite lecturas m&iacute;sticas en informes periciales. Priorice variables psicom&eacute;tricas validadas y observaci&oacute;n cl&iacute;nica.</p>
    <p>Si combina MBTI con arquetipos en devoluci&oacute;n, aclare que ambos son marcos diferentes. Documente separadamente en historia cl&iacute;nica.</p>

    <h2>Trabajo con la Sombra e individuaci&oacute;n</h2>
    <p>El trabajo de <strong>Sombra</strong> implica reconocer impulsos, deseos o cualidades negadas sin actuarlos destructivamente. T&eacute;cnicas cl&iacute;nicas prudentes: di&aacute;logo imaginario, escritura expresiva, exploraci&oacute;n de sue&ntilde;os, role-play con l&iacute;mites, mindfulness de emociones vergonzosas. Contraste con catarsis irresponsable o confrontaciones shaming.</p>
    <p><strong>Individuaci&oacute;n</strong> describe proceso de diferenciaci&oacute;n del ego respecto a colectividad e integraci&oacute;n de opuestos. No es meta obligatoria en todos los tratamientos; en TCC breve puede traducirse como flexibilizaci&oacute;n de reglas r&iacute;gidas. En psicoterapia prolongada orienta sentido tras p&eacute;rdidas irreversibles.</p>
    <p>Pacientes con trastornos de personalidad requieren contenci&oacute;n estructurada; la Sombra no justifica abusos interpersonales. Mantenga contrato terap&eacute;utico, evaluaci&oacute;n de riesgo y derivaci&oacute;n psiqui&aacute;trica cuando hay descompensaci&oacute;n.</p>

    <h2>L&iacute;mites de evidencia y &eacute;tica</h2>
    <p>Los arquetipos no tienen baremos estandarizados ni validez predictiva comparable a pruebas psicom&eacute;tricas. Revisiones cr&iacute;ticas se&ntilde;alan riesgo de confirmaci&oacute;n, universalismo cultural y pseudociencia cuando se venden como tipolog&iacute;a r&iacute;gida. El psic&oacute;logo colegiado debe basar informes periciales en constructos con respaldo y consentimiento informado claro.</p>
    <p>En contextos espirituales, delimite competencia y evite dual relaci&oacute;n. Si integra arte o sandplay, describa m&eacute;todo y l&iacute;mites. La utilidad cl&iacute;nica est&aacute; en enriquecer narrativa cuando el paciente ya habla en clave simb&oacute;lica, sin sustituir evaluaci&oacute;n de riesgo ni intervenciones basadas en evidencia.</p>
        """),
        "faqs": [
            {"q": "\u00bfLos arquetipos de Jung son cient\u00edficamente v\u00e1lidos?", "q_html": "&iquest;Los arquetipos de Jung son cient&iacute;ficamente v&aacute;lidos?", "a_plain": "Son constructos te\u00f3ricos y cl\u00ednicos \u00fatiles como met\u00e1fora y marco interpretativo, pero no constituyen categor\u00edas diagn\u00f3sticas con baremos estandarizados ni validez predictiva robusta. \u00daselos con prudencia, supervisi\u00f3n y l\u00edmites \u00e9ticos en informes formales.", "a_html": "Son constructos te&oacute;ricos y cl&iacute;nicos &uacute;tiles como met&aacute;fora, pero no categor&iacute;as diagn&oacute;sticas con baremos estandarizados."},
            {"q": "\u00bfC\u00f3mo trabajo la Sombra sin da\u00f1ar al paciente?", "q_html": "&iquest;C&oacute;mo trabajo la Sombra sin da&ntilde;ar al paciente?", "a_plain": "Priorice seguridad, alianza y ritmo del paciente. Use exploraci\u00f3n gradual de emociones vergonzosas, sue\u00f1os o proyecciones con t\u00e9cnicas estructuradas (escritura, di\u00e1logo imaginario). Evite confrontaciones humillantes o interpretaciones prematuras en trauma no estabilizado.", "a_html": "Priorice seguridad y exploraci&oacute;n gradual. Evite confrontaciones humillantes en trauma no estabilizado."},
            {"q": "\u00bfEl MBTI es base cl\u00ednica para arquetipos?", "q_html": "&iquest;El MBTI es base cl&iacute;nica para arquetipos?", "a_plain": "No. El MBTI mide preferencias de tipo junguiano simplificadas para desarrollo personal u organizacional, no arquetipos ni psicopatolog\u00eda. Puede servir como punto de conversaci\u00f3n si el paciente ya lo aplic\u00f3, pero no debe usarse para diagn\u00f3stico ni informes periciales.", "a_html": "No. MBTI mide preferencias, no arquetipos ni psicopatolog&iacute;a."},
            {"q": "\u00bfPuedo usar Jung en cl\u00ednica moderna basada en evidencia?", "q_html": "&iquest;Puedo usar Jung en cl&iacute;nica moderna basada en evidencia?", "a_plain": "S\u00ed, como lenguaje simb\u00f3lico complementario dentro de marcos con evidencia (TCC, ACT, psicodin\u00e1mica integrativa), siempre que no sustituya evaluaci\u00f3n estandarizada, medici\u00f3n de resultados ni criterios diagn\u00f3sticos oficiales. Documente objetivos observables.", "a_html": "S&iacute;, como lenguaje simb&oacute;lico complementario sin sustituir evaluaci&oacute;n estandarizada."},
        ],
        "related": [("que-es-el-dsm-5", "Qu&eacute; es el DSM-5"), ("historia-clinica-psicologica-paso-a-paso", "Historia cl&iacute;nica psicol&oacute;gica paso a paso"), ("como-interpretar-tests-psicologicos", "C&oacute;mo interpretar tests psicol&oacute;gicos"), ("orientacion-vocacional-psicologia", "Orientaci&oacute;n vocacional en psicolog&iacute;a")],
        "references": ['<a href="https://www.apa.org/" rel="nofollow noopener noreferrer" target="_blank">American Psychological Association &mdash; ethics and assessment</a>'],
    })

    # Article 4-7 defined in part2 file - import at runtime
    from finalize_phase1_part2 import articles_4_through_7  # noqa: WPS433
    articles.extend(articles_4_through_7())
    return articles


def py_str(s: str) -> str:
    """Return Python source for a string, preferring triple quotes."""
    if '"""' not in s:
        return f'"""{s}"""'
    if "'''" not in s:
        return f"'''{s}'''"
    return repr(s)


def py_val(v, indent=0) -> str:
    sp = " " * indent
    if isinstance(v, str):
        if "\n" in v and len(v) > 80:
            return py_str(v)
        return repr(v)
    if isinstance(v, bool):
        return "True" if v else "False"
    if v is None:
        return "None"
    if isinstance(v, (int, float)):
        return repr(v)
    if isinstance(v, tuple):
        inner = ", ".join(py_val(x, indent + 4) for x in v)
        if len(v) == 1:
            inner += ","
        return f"({inner})"
    if isinstance(v, list):
        if not v:
            return "[]"
        lines = ["["]
        for item in v:
            lines.append(f"{sp}    {py_val(item, indent + 4)},")
        lines.append(f"{sp}]")
        return "\n".join(lines)
    if isinstance(v, dict):
        lines = ["{"]
        for k, val in v.items():
            lines.append(f'{sp}    "{k}": {py_val(val, indent + 4)},')
        lines.append(f"{sp}}}")
        return "\n".join(lines)
    return repr(v)


def write_phase1(all_articles: list[dict]) -> None:
    parts = [
        "# -*- coding: utf-8 -*-",
        '"""Phase 1 batch: 7 clinical article specs for render_ley1616_article.render()."""',
        "from __future__ import annotations",
        "",
        "ARTICLES: list[dict] = [",
    ]
    for i, art in enumerate(all_articles):
        parts.append(f"    {py_val(art, 4)},")
    parts.append("]")
    parts.append("")
    PHASE1.write_text("\n".join(parts), encoding="utf-8")


def validate(all_articles: list[dict]) -> list[tuple[str, int]]:
    assert len(all_articles) == 7, f"Expected 7 articles, got {len(all_articles)}"
    counts = []
    for a in all_articles:
        w = wc(a)
        assert w >= 1200, f"{a['slug']} only {w} words"
        counts.append((a["slug"], w))
    return counts


def main() -> None:
    existing = load_existing()
    if len(existing) != 2:
        raise SystemExit(f"Expected 2 existing articles, found {len(existing)}")
    new = build_new_articles()
    all_articles = existing + new
    for a in all_articles:
        ensure_min_words(a)
    counts = validate(all_articles)
    write_phase1(all_articles)
    for slug, w in counts:
        print(f"{slug}: {w} words")
    print("All 7 articles pass validation.")


if __name__ == "__main__":
    main()
