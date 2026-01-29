"""
Módulo de extracción de docstrings.
- LÓGICA PURA de negocio: extraer docstrings desde el texto (string) de un archivo Python.
- Recibe código fuente como `str` y devuelve una lista de `DocItem` en orden de aparición.
- NO lee archivos del disco: eso es trabajo de `infra/fs.py`.
- NO escribe el .docx: eso es trabajo de `infra/writer_docx.py`.
"""

import ast
import textwrap
from typing import List, Optional
from .modelos import DocItem

class _Visitante(ast.NodeVisitor):
    def __init__(self) -> None:
        self.items: List[DocItem] = []
        self._stack_clases: List[str] = []

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        doc = ast.get_docstring(node)
        if doc:
            doc = textwrap.dedent(doc).strip()

        nombre = node.name
        self.items.append(DocItem("class", nombre, doc, nombre))

        self._stack_clases.append(nombre)
        self.generic_visit(node)
        self._stack_clases.pop()

    def _agregar_funcion(self, node: ast.AST) -> None:
        doc = ast.get_docstring(node)
        if doc:
            doc = textwrap.dedent(doc).strip()

        clase = self._stack_clases[-1] if self._stack_clases else None
        nombre_mostrado = f"{clase}.{node.name}" if clase else node.name
        self.items.append(DocItem("function", nombre_mostrado, doc, clase))

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self._agregar_funcion(node)
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
        self._agregar_funcion(node)
        self.generic_visit(node)

def extraer_docstrings_desde_codigo(source: str) -> List[DocItem]:
    """
    Recibe el texto de un archivo Python y devuelve los DocItem en orden de aparición.
    """
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return []
    v = _Visitante()
    v.visit(tree)
    return v.items