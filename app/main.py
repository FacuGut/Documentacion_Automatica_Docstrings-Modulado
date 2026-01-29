"""
Módulo principal de la aplicación.
- Punto de entrada (CLI) del proyecto.
- Parsear argumentos de línea de comandos.
- Cargar configuración (config/settings.py), aplicar overrides CLI y arrancar el orquestador.

Librerias a instalar:
pip install python-docx

"""
import argparse
import os
from config.settings import cargar_config
from src.logging_conf import configurar_logging
from app.orquestador import generar_documentacion


def parse_args():
    p = argparse.ArgumentParser(
        description="Genera un archivo .docx con los docstrings de un proyecto Python."
    )
    p.add_argument("ruta", nargs="?", default=".", help="Ruta del proyecto a analizar (default: .)")
    p.add_argument("-o", "--output", default=None, help="Archivo .docx de salida")
    p.add_argument("--config", default=None, help="Ruta a appsettings.json alternativo")
    p.add_argument("--log", default="INFO", help="Nivel de log (DEBUG, INFO, WARNING, ERROR)")
    p.add_argument("--incluir-paquete", action="store_true", help="Incluye el propio paquete en el análisis")
    return p.parse_args()

def main():
    args = parse_args()
    configurar_logging(args.log)

    # Carga configuración desde JSON + ENV
    cfg = cargar_config(ruta_base=os.getcwd(), ruta_json=args.config)

    # Overrides desde CLI
    if args.ruta:
        cfg.ruta_proyecto = args.ruta
    if args.output:
        cfg.archivo_salida = args.output
    if args.incluir_paquete:
        cfg.incluir_paquete_propio = True

    generar_documentacion(cfg)

if __name__ == "__main__":
    main()
