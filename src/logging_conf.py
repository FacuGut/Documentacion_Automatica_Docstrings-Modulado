"""
Módulo de configuración de logging.
- Configurar el sistema de logging (formato, nivel).
- Centraliza la configuración para que `app/main.py` la aplique.
- No mezcla logs con otros comportamientos.
"""
import logging
import sys

def configurar_logging(nivel: str = "INFO") -> None:
    logging.basicConfig(
        level=getattr(logging, nivel.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )