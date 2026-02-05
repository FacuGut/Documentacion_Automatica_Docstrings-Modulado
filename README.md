<div align="center">

# ** Documentación Automática de Docstrings – DocuRunner**

*Generador automático de documentación .docx para proyectos Python*

</div>

---

##  **Propósito**

Este proyecto permite **recopilar de forma automática todos los docstrings** de un proyecto en Python y generar un archivo **.docx** con la documentación formateada de manera uniforme.  
Su objetivo es facilitar el mantenimiento documental sin necesidad de editar manualmente cada archivo.

---

##  **Requisitos**

- **Python 3.10 o superior**
- Librería **python-docx**

Instalación:

```bash
pip install python-docx
```

---


## **Ejecucion**
1. Clonar el repositorio en tu equipo
2. Instalar dependencia python-docx
3. Abrir Visual Studio Code y presionar Ctrl + Shift + P dentro para crear una task 
4. Seleccionar la opción "Open User Tasks", esto abrirá el archivo tasks.json
5. Pegar el siguiente contenido dentro de tasks.json y reemplazar solo los valores PATH en "cwd" y "PYTHONPATH" por la ruta de la carpeta donde tengas este script clonado y los workspaceFolder por la ruta de el proyecto a documentar
```bash
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Documentar proyecto (DocuRunner)",
      "type": "shell",
      "command": "python",
      "args": [
        "-m",
        "app.main",
        "${workspaceFolder}",
        "-o",
        "${workspaceFolder}/documentacion.docx"
      ],
      "options": {
        "cwd": "PATH",
        "env": {
          "PYTHONPATH": "PATH"
        }
      },
      "presentation": {
        "echo": true,
        "reveal": "always",
        "panel": "shared"
      },
      "problemMatcher": []
    }
  ]
}
```
7. En el proyecto a documentar ejecutar la task presionando Ctrl + Shift + P → Tasks: Run Task → Documentar proyecto (DocuRunner)

---

