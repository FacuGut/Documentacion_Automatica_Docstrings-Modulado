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
2. Instalar la dependencia python-docx en este proyecto 
3. Abrir el proyecto a documentar 
4. Poner en la consola del proyecto a documentar el siguiente comando y reemplazar "PATH" por la ruta de la raiz de DocuRunner (este proyecto)
```bash
powershell -ExecutionPolicy Bypass -File "PATH\docurunner.ps1"
```
Ejemplo: powershell -ExecutionPolicy Bypass -File "C:\Users\jmartinez\Desktop\Proyectos\Automatizacion\docurunner.ps1"
