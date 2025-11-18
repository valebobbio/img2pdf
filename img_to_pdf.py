import img2pdf
import os
import sys
def generar_nombre_disponible(carpeta, nombre_base):
    """
    Devuelve un nombre de archivo disponible dentro de 'carpeta'.
    Si ya existe, genera nombre(1).pdf, nombre(2).pdf, etc.
    """
    base, extension = os.path.splitext(nombre_base)
    contador = 1
    nombre_final = nombre_base

    while os.path.exists(os.path.join(carpeta, nombre_final)):
        nombre_final = f"{base}({contador}){extension}"
        contador += 1

    return nombre_final


# Verificar que se pasó un nombre de archivo
if len(sys.argv) < 2:
    #print("Uso: python convertir.py nombre_salida.pdf")
    nombre_salida = "salida.pdf"
else:
    nombre_salida = sys.argv[1]
    if not nombre_salida.lower().endswith(".pdf"):
        nombre_salida += ".pdf"

# Carpeta donde están las imágenes
carpeta = "img/"

# Carpeta de salida
carpeta_output = "output/"

# Crear carpeta output si no existe
os.makedirs(carpeta_output, exist_ok=True)

# Generar un nombre disponible si ya existe el archivo
nombre_salida = generar_nombre_disponible(carpeta_output, nombre_salida)

# Ruta final del PDF
ruta_pdf = os.path.join(carpeta_output, nombre_salida)

# Obtener lista ordenada de imágenes válidas
img = sorted([
    os.path.join(carpeta, f)
    for f in os.listdir(carpeta)
    if f.lower().endswith((".jpg", ".jpeg", ".png"))
])

if not img:
    print("No se encontraron imágenes en la carpeta.")
    exit()

# Crear PDF a partir de las imágenes
with open(ruta_pdf, "wb") as pdf:
    pdf.write(img2pdf.convert(img))

print(f"PDF generado correctamente: {nombre_salida}")
