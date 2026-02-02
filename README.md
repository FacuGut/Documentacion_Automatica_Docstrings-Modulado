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
pip install python-docx```

---

## **Ejecucion**
1. Clonar el repositorio en tu equipo
2. Instalar dependencia python-docx
3. Abrir Visual Studio Code y presionar Ctrl + Shift + P dentro de la carpeta docrunner para crear una task 
4. Seleccionar la opción "Open User Tasks", esto abrirá el archivo tasks.json
5. Pegar el siguiente contenido dentro de tasks.json y reemplazar los valores PATH por la ruta donde tengas este proyecto
6. En el proyecto a documentar ejecutar la task presionando Ctrl + Shift + P → Tasks: Run Task → Documentar proyecto (DocuRunner)


