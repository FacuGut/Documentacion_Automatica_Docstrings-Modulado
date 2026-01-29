"""
Módulo de modelos de dominio.
- Definir los modelos de dominio (dataclasses) que representan la información interna.
- En este proyecto: `DocItem`, que describe clases/funciones y sus docstrings.
"""

from dataclasses import dataclass
from typing import Optional, Literal

TipoItem = Literal["class", "function"]

@dataclass(frozen=True)
class DocItem:
    tipo: TipoItem
    nombre: str
    docstring: Optional[str]
    clase: Optional[str]