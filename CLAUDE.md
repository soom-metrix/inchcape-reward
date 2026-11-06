# Inchcape "Rally Reward" – Revisión de traducciones (memoria del proyecto)

Lee este archivo antes de tocar nada. Usuaria: habla español; mantener lenguaje profesional y no dirigirse a ella por su nombre.

## Qué es
Curso e-learning de Inchcape (Reward / revisión salarial), 78 diapositivas, base en inglés. Se localizó a 9 idiomas
(fr, nl, el, pl, bg, lt, fi, et, lv): imágenes con texto traducido + subtítulos. La entrega es una **página de revisión**
publicada como Artifact de claude.ai (https://claude.ai/artifact/K5qaFftBVBdBcrra7WW2TQ): inglés a la izquierda,
idioma elegido a la derecha, scroll sincronizado, comentarios del cliente (texto, cita, pin, y **selección de área de imagen
con captura**), guía inicial, exportación CSV/JSON/copiar.

## Estado (nov 2026)
- 9 idiomas publicados; cada uno pasó una revisión de "estilo nativo" (editor IA por idioma). No hay revisión de nativos humanos: lo hará el cliente con los comentarios.
- Pendiente / sin decidir: unificar "Achieved"/"Met" (preguntar a la usuaria qué término); la insignia "C, C" del cuestionario sigue igual en la base inglesa (en las traducidas se corrigió a "D" con `tD.py`); UI de capturas de sistema sin localizar.
- Términos que el cliente podría tener en glosario propio: grades, benefits, merit matrix, compa-ratio, midpoint, Compensation Planner Manager.

## Estructura del repo
- `pipeline/` – genera las imágenes traducidas con PyMuPDF. `run_all.py` (usa `LANGC=<idioma>`), `build_all.py`, `replace.py`, parches por diapositiva (`t2.py`, `t10.py`, `t78.py`, `tD.py`). `uniq_en.json` = 178 textos únicos en inglés; `subtitles.json` = subtítulos EN por diapositiva.
- `translations/tr/` – **fuente de verdad de las traducciones**: `<L>_img.txt` (textos de imagen, 177 líneas ≈ 175 entradas; la línea i ↔ `uniq_en.json[i+3]`, las líneas que empiezan con `* ` continúan la anterior), `mk_<L>_sub.py` (diccionario T[n] de subtítulos → `<L>_sub.json`), `<L>_extra.json` (etiquetas: INITIAL, MARKET, FINAL, CONG, S34, MIN, MAX, KIT, S2_TITLE, S2_TEXT), `mk_map.py <L>` (genera `<L>_map.json`).
- `fonts/` – Jost / TeX Gyre Adventor. Carpetas: raíz (fr, nl, fi, et), `fnt_gr` (el, bg), `fnt_pl` (pl, lt, lv).
- `tools/` – `prep_slides.py` (docx → `slides.json` con las imágenes base), `assemble_packs.py` (jpg finales → `<L>/pack.json` + inyecta `TR` en el HTML), pruebas Playwright (`t_pack.js`, `t_drag.js`).
- `review-page/Inchcape_Reward_Review.html` – página de revisión (≈6 MB, imágenes base incrustadas). Los `pack.json` (≈6 MB c/u) NO están en git: se regeneran.

## Entradas que NO están en git (pesadas / del cliente)
`es.pdf`, `es2.pdf` (cursos en español, base del reemplazo), `en_part1/2.pdf`, `<L>_part1/2.pdf` (PDF por idioma), el .docx original con las capturas. Pedirlos a la usuaria o a Metrix si se necesita regenerar imágenes.

## Cómo cambiar una traducción
1. Editar `translations/tr/<L>_img.txt` (misma cantidad de líneas; conservar `<b>…</b>`, `\n`, `* `; **no alargar más de ~5 %**, los textos van en cajas fijas; finés/estonio/letón: no alargar) y/o `mk_<L>_sub.py` (largo libre) y `<L>_extra.json`.
2. `python3 -I tr/mk_map.py <L>`; `python3 -I tr/mk_<L>_sub.py`.
3. `LANGC=<L> python3 -I run_all.py` (desde la carpeta con `tr/`, fuentes y PDFs) → `final_<L>/s01..s78.jpg`. Revisar visualmente desbordes (informe: SMALL/UNCERTAIN/MISSING).
4. `tools/assemble_packs.py` arma `<L>/pack.json` y actualiza `const TR` del HTML.
5. Publicar el Artifact: mismo `file_path` + `url`, `files` con los `*/pack.json`. Antes, `list scope:files` (la herramienta exige haber visto los archivos publicados).

## Reglas y trampas aprendidas
- El Artifact admite 511 archivos/versión: por eso las imágenes van en un `pack.json` por idioma (data URIs, carga perezosa con `loadPack`).
- Estonio: la fuente no tiene š/ž en imágenes → evitarlos allí. Letón: forma neutra de género hacia el aprendiz.
- `build_all.py` parte la frase de la diapositiva 34 usando la etiqueta `S34` (p. ej. "Atlyginimai", "Algas") → la línea 82 de `<L>_img.txt` debe contener esa palabra en nominativo rodeada de espacios, o falla con "not enough values to unpack".
- Comentarios: `comments[]` = `{id,slide,side,lang,x,y,quote,text,author,ts,resolved,shot,rx,ry,rw,rh}`; db capability `comments` (lectura view / escritura interact) + localStorage. `shot` = recorte JPEG (dataURL) del área elegida.
- Un `<L>_part*.pdf` se genera con el texto ya traducido por bloques; no editar a mano.
- Prueba local: `python3 -m http.server 8765` en la carpeta de la página y `NODE_PATH=$(npm root -g) node tools/t_pack.js` / `t_drag.js`. El mojibake local es solo falta de charset del servidor.
- Las traducciones son de IA con revisión de estilo; no afirmar que fueron revisadas por nativos.

## Publicación en GitHub Pages
`site/` y `docs/` son la versión autónoma (index.html + `<L>/pack.json`). En GitHub: Settings → Pages → Deploy from branch → carpeta `/docs` (copia de `site/`).
Fuera de claude.ai no existe la base de datos compartida: los comentarios quedan solo en el navegador de cada revisor (localStorage) y se envían con Exportar/Copiar. Tras cambiar traducciones, regenerar con `tools/assemble_packs.py` y copiar el HTML y los pack.json a `site/` (el HTML de `site/` lleva doctype/meta añadidos).

## Comentarios en GitHub
- Fuente compartida: base de datos del Artifact (colección `comments`). Copia en el repo: `comments/comments.json` (volcar con ArtifactData `list` y subir).
- En el panel de comentarios, cada comentario tiene el enlace «Save to GitHub as an issue» (Issue prellenado en `soom-metrix/inchcape-reward`, etiqueta `review`; requiere cuenta de GitHub; sin captura).
- GitHub Pages no puede escribir en el repo (no poner tokens en una página pública).
