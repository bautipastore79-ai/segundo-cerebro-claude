---
name: procesar-raw
description: Procesa el material nuevo de RAW/ y lo integra en WIKI/ siguiendo las reglas de CLAUDE.md. Usar cuando digan "procesá RAW", "metelo al cerebro", "ordená lo nuevo" o "actualizá la wiki".
---

# Procesar RAW

1. **Detectá lo nuevo.** Listá `RAW/` y comparalo con las fuentes ya citadas en `changelog.md`
   y en los `fuentes:` de `WIKI/`. Lo que no aparece en ningún lado es nuevo.
2. **Leelo entero.** Todos los archivos nuevos, de punta a punta. Si es un PDF o una imagen,
   abrilo; no supongas el contenido por el nombre.
3. **Mapeá a temas.** Para cada dato, decidí a qué tema pertenece. Si el tema existe, actualizá
   esa nota. Si no, creá una nueva en kebab-case.
4. **Escribí con fuente.** Cada nota nueva o tocada actualiza `actualizado:` y suma el archivo
   de RAW en `fuentes:`. Nada que no esté en RAW.
5. **Conectá.** Agregá `[[enlaces]]` entre temas relacionados y sumá los temas nuevos a `WIKI/index.md`.
6. **Chequeá.** Corré `python3 scripts/chequear_wiki.py` y arreglá cada aviso.
7. **Registrá.** Entrada nueva arriba de todo en `changelog.md`: fecha, qué se procesó, qué cambió.
8. **Huecos.** Reemplazá la sección "Huecos actuales" de `WIKI/index.md` por los 3 huecos más
   importantes, y decíselos al humano.

Si algo de RAW contradice lo que ya está en WIKI, no lo pises en silencio: dejá las dos
versiones con su fecha y fuente, y preguntá cuál vale.
