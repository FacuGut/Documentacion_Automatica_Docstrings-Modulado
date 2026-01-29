"""
Módulo de configuración de la app.
- Cargar y validar la configuración de la app desde `config/appsettings.json`.
- Permitir overrides por variables de entorno y por CLI (aplicados en app/main.py).
- Expone una dataclass `Config` usada por el orquestador.
"""
import json
import os
from dataclasses import dataclass, field
from typing import List, Tuple

@dataclass
class Colores:
    con_doc: Tuple[int, int, int] = (0, 102, 204)
    sin_doc: Tuple[int, int, int] = (255, 0, 0)

@dataclass
class Config:
    ruta_proyecto: str = "."
    archivo_salida: str = "documentacion.docx"
    excluir_dirs: List[str] = field(default_factory=list)
    colores: Colores = field(default_factory=Colores)
    incluir_paquete_propio: bool = False

def _leer_json(ruta: str) -> dict:
    if not os.path.exists(ruta):
        return {}
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

def cargar_config(ruta_base: str, ruta_json: str | None = None) -> Config:
    """
    Carga configuración desde appsettings.json y aplica overrides por variables de entorno.
    """
    if ruta_json is None:
        ruta_json = os.path.join(ruta_base, "config", "appsettings.json")

    data = _leer_json(ruta_json)

    # Overrides por ENV (opcionales), todo se configura en el .json 
    ruta_proyecto = os.getenv("DOCU_RUTA_PROYECTO", data.get("ruta_proyecto", "."))
    archivo_salida = os.getenv("DOCU_ARCHIVO_SALIDA", data.get("archivo_salida", "documentacion.docx"))
    incluir_paquete_propio = os.getenv("DOCU_INCLUIR_PAQUETE", str(data.get("incluir_paquete_propio", False))).lower() == "true"
    excluir_dirs = data.get("excluir_dirs", [])
    colores_data = data.get("colores", {})
    colores = Colores(
        con_doc=tuple(colores_data.get("con_doc", [0, 102, 204])),
        sin_doc=tuple(colores_data.get("sin_doc", [255, 0, 0])),
    )

    return Config(
        ruta_proyecto=ruta_proyecto,
        archivo_salida=archivo_salida,
        excluir_dirs=excluir_dirs,
        colores=colores,
        incluir_paquete_propio=incluir_paquete_propio,
    )