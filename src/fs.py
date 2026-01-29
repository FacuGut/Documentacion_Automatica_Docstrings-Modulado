"""
Módulo de sistema de archivos.
- Acceso a sistema de archivos.
- Recorrer el proyecto, filtrar carpetas excluidas y leer el contenido de archivos `.py`.
"""

import os
from typing import List, Set

def normalizar_ruta(p: str) -> str:
    return os.path.normcase(os.path.realpath(os.path.abspath(p)))

def leer_codigo(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except UnicodeDecodeError:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()

def buscar_archivos_python(
    ruta_raiz: str,
    excluir_dirs: Set[str],
    excluir_paths_absolutos: Set[str] | None = None,
) -> List[str]:
    if excluir_paths_absolutos is None:
        excluir_paths_absolutos = set()
    excluir_paths_norm = {normalizar_ruta(p) for p in excluir_paths_absolutos}

    archivos: List[str] = []
    for root, dirs, files in os.walk(ruta_raiz):
        dirs[:] = [d for d in dirs if d not in excluir_dirs]
        for fname in files:
            if not fname.endswith(".py"):
                continue
            candidate = os.path.join(root, fname)
            cand_norm = normalizar_ruta(candidate)
            if cand_norm in excluir_paths_norm:
                continue
            archivos.append(cand_norm)
    return sorted(archivos)