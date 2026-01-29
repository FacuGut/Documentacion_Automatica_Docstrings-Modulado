"""
Módulo orquestador.
- Orquestar el flujo end-to-end:
  1) Leer config
  2) Buscar archivos .py (infra/fs.py)
  3) Leer su contenido (infra/fs.py)
  4) Extraer docstrings del texto (core/leer_docstrings.py)
  5) Escribir el .docx (infra/writer_docx.py)
- Registrar logs y devolver la ruta del archivo generado.
- Punto central de coordinación de la aplicación.
"""
import logging
import os
from typing import Dict, List
from config.settings import Config
from src.fs import buscar_archivos_python, leer_codigo, normalizar_ruta
from src.writer_docx import escribir_docx_por_archivo
from core.leer_docstrings import extraer_docstrings_desde_codigo

log = logging.getLogger(__name__)

def generar_documentacion(cfg: Config) -> str:
    """
    Orquesta el flujo:
    - Buscar .py
    - Leer código y extraer docstrings (core)
    - Escribir DOCX (infra)
    Retorna la ruta absoluta del archivo generado.
    """
    ruta_proyecto = os.path.abspath(cfg.ruta_proyecto)
    log.info("Analizando proyecto: %s", ruta_proyecto)

    excluir_paths = set()
    if not cfg.incluir_paquete_propio:
        # excluye este propio paquete (directorio 'tu_proyecto' o el paquete donde está app/orquestador.py)
        paquete_dir = os.path.dirname(os.path.dirname(__file__))  # .../tu_proyecto
        excluir_paths.add(paquete_dir)

    archivos = buscar_archivos_python(
        ruta_raiz=ruta_proyecto,
        excluir_dirs=set(cfg.excluir_dirs),
        excluir_paths_absolutos=excluir_paths,
    )
    log.info("Archivos .py encontrados: %d", len(archivos))

    resultados: Dict[str, List] = {}
    for path in archivos:
        source = leer_codigo(path)
        resultados[path] = extraer_docstrings_desde_codigo(source)

    escribir_docx_por_archivo(
        resultados=resultados,
        ruta_raiz=ruta_proyecto,
        salida_docx=cfg.archivo_salida,
        color_con_doc=cfg.colores.con_doc,
        color_sin_doc=cfg.colores.sin_doc,
    )

    salida_abs = os.path.abspath(cfg.archivo_salida)
    log.info("Documento generado: %s", salida_abs)
    return salida_abs