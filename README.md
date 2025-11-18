**Img to PDF**

- **Descripción**: Conversor simple que toma las imágenes dentro de la carpeta `img/` y las concatena en un PDF.
- **Salida**: El PDF se guarda en la carpeta `output/`.

**Requisitos**

- **Python**: 3.x
- **Paquete**: `img2pdf` (instalar con `pip install img2pdf` o `py -m install img2pdf`)

**Estructura mínima**

- `img_to_pdf.py`: script principal.
- `img/`: carpeta donde deben colocarse las imágenes (`.jpg`, `.jpeg`, `.png`). Debe ser creada manualmente.
- `output/`: carpeta donde se almacenan los PDFs generados (el script crea esta carpeta si no existe).

**Uso básico**

- Ejecutar sin argumentos (genera `salida.pdf` dentro de `output/` si no se pasa nombre):

```powershell
py img_to_pdf.py
```

- Especificar el nombre del archivo de salida (puede pasarse con o sin la extensión `.pdf`):

```powershell
py img_to_pdf.py miarchivo
# o
py img_to_pdf.py miarchivo.pdf
```

- Si el nombre ya existe en `output/`, el script generará una variante libre, por ejemplo `miarchivo(1).pdf`, `miarchivo(2).pdf`, etc.

**Formatos soportados**

- `.jpg`, `.jpeg`, `.png` (el script toma todos los archivos en `img/` con estas extensiones, ordenados por nombre).

**Comportamiento y notas**

- Si no hay imágenes en `img/`, el script imprime `No se encontraron imágenes en la carpeta.` y termina.
- El script por defecto asegura que la salida esté en `output/` y crea el directorio si hace falta.
- Pase sólo el nombre del archivo (o nombre + `.pdf`). Evite pasar rutas complejas como argumento; si quiere otra ruta, edite la variable `carpeta_output` dentro de `img_to_pdf.py`.

**Ejemplo rápido**

- Colocar `001.jpg`, `002.jpg` en `img/` y ejecutar:

```powershell
py img_to_pdf.py informe_final
# Resultado: output/informe_final.pdf (o informe_final(n).pdf si ya existía)
```

**Contacto / Contribuir**

- Abrir un issue o enviar un pull request si querés mejoras (por ejemplo: soporte para orden natural, más formatos, o flags CLI).

