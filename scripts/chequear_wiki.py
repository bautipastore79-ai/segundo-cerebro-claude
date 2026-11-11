#!/usr/bin/env python3
"""Chequea la salud de WIKI/: frontmatter, enlaces rotos, fuentes inexistentes,
notas huérfanas (fuera del índice) y notas demasiado largas.

Uso:  python3 scripts/chequear_wiki.py [carpeta-del-cerebro]
Sale con código 1 si encuentra problemas, así sirve también en CI.
"""
import re
import sys
from pathlib import Path

LIMITE_LINEAS = 300
CAMPOS = ("tema", "actualizado", "fuentes")
ENLACE = re.compile(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]")
FECHA = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def leer_frontmatter(texto):
    if not texto.startswith("---\n"):
        return None
    fin = texto.find("\n---", 4)
    if fin == -1:
        return None
    datos = {}
    for linea in texto[4:fin].splitlines():
        if ":" in linea:
            clave, valor = linea.split(":", 1)
            datos[clave.strip()] = valor.strip()
    return datos


def fuentes_de(valor):
    valor = valor.strip().strip("[]")
    return [f.strip().strip("'\"") for f in valor.split(",") if f.strip()]


def main():
    raiz = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    wiki = raiz / "WIKI"
    if not wiki.is_dir():
        print(f"No encuentro {wiki}")
        return 1

    notas = {p.stem: p for p in sorted(wiki.rglob("*.md"))}
    indice = notas.get("index")
    enlazadas_desde_indice = set()
    if indice:
        enlazadas_desde_indice = set(ENLACE.findall(indice.read_text(encoding="utf-8")))

    problemas = []
    for nombre, ruta in notas.items():
        rel = ruta.relative_to(raiz)
        texto = ruta.read_text(encoding="utf-8")

        if nombre != "index":
            fm = leer_frontmatter(texto)
            if fm is None:
                problemas.append(f"{rel}: no tiene frontmatter")
            else:
                for campo in CAMPOS:
                    if campo not in fm:
                        problemas.append(f"{rel}: falta '{campo}' en el frontmatter")
                if "actualizado" in fm and not FECHA.match(fm["actualizado"]):
                    problemas.append(f"{rel}: 'actualizado' no es YYYY-MM-DD ({fm['actualizado']})")
                for fuente in fuentes_de(fm.get("fuentes", "")):
                    if not (raiz / fuente).exists():
                        problemas.append(f"{rel}: la fuente {fuente} no existe")
            if nombre not in enlazadas_desde_indice:
                problemas.append(f"{rel}: no está enlazada desde WIKI/index.md")

        for destino in set(ENLACE.findall(texto)):
            if destino.strip() not in notas:
                problemas.append(f"{rel}: enlace roto [[{destino}]]")

        lineas = texto.count("\n") + 1
        if lineas > LIMITE_LINEAS:
            problemas.append(f"{rel}: tiene {lineas} líneas (máx. {LIMITE_LINEAS}), conviene partirla")

    if problemas:
        print(f"{len(problemas)} problema(s):")
        for p in problemas:
            print(f"  - {p}")
        return 1
    print(f"WIKI en orden: {len(notas)} notas revisadas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
