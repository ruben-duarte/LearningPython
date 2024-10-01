from PIL import Image, ImageFilter
import tkinter as tk

img = Image.open('./images/engine.jpg')
print(img.format)
print(img.size)
print(img.mode)

# puedo usar dir(img) ver que metodos tiene

# root = tk.Tk()
# # Obtiene el tamaño de la pantalla
# ancho_pantalla = root.winfo_screenwidth()
# alto_pantalla = root.winfo_screenheight()

# print(f"Tamaño de la pantalla: {ancho_pantalla}x{alto_pantalla}")
# root.destroy() 
# Tamaño de la pantalla: 1366x768


filtered_image = img.filter(ImageFilter.BLUR)
filtered_image.save("blur.png", 'png')

img_engine = Image.open('./images/engine.jpg')
# Crear el color de fondo azul oscuro y el color amarillo para las líneas
fondo_azul_oscuro = (10, 30, 60)
linea_amarilla = (255, 255, 0)

# Definir rangos de colores (umbral)
umbral_blanco = 200  # Valores superiores a este se considerarán blancos
umbral_azul_claro = (100, 100, 255)  # Aproximación para azul claro
umbral_azul_oscuro = (0, 0, 150)     # Aproximación para azul oscuro

# Obtener las dimensiones de la imagen
ancho, alto = img.size

# Crear una nueva imagen de fondo azul oscuro
img_modificada = Image.new("RGB", (ancho, alto), fondo_azul_oscuro)

# Función para verificar si un color es "casi blanco"
def es_casi_blanco(pixel):
    return all(val >= umbral_blanco for val in pixel)

# Función para verificar si un color es "azul claro"
def es_azul_claro(pixel):
    r, g, b = pixel
    return r < umbral_azul_claro[0] and g < umbral_azul_claro[1] and b > umbral_azul_claro[2]

# Función para verificar si un color es "azul oscuro"
def es_azul_oscuro(pixel):
    r, g, b = pixel
    return r < umbral_azul_oscuro[0] and g < umbral_azul_oscuro[1] and b > umbral_azul_oscuro[2]

# Recorremos los píxeles para modificar el fondo blanco y las líneas azules
for x in range(ancho):
    for y in range(alto):
        pixel = img.getpixel((x, y))
        
        # Si el pixel es casi blanco, lo cambiamos al color del fondo azul oscuro
        if es_casi_blanco(pixel):
            img_modificada.putpixel((x, y), fondo_azul_oscuro)
        
        # Si el pixel es azul claro, lo cambiamos a amarillo
        elif es_azul_claro(pixel):
            img_modificada.putpixel((x, y), linea_amarilla)
        
        # Si el pixel es azul oscuro, lo dejamos tal cual o podemos modificarlo
        elif es_azul_oscuro(pixel):
            img_modificada.putpixel((x, y), linea_amarilla)  # Cambiar a amarillo si quieres

        # Mantenemos los demás píxeles tal como están
        else:
            img_modificada.putpixel((x, y), pixel)

# Guardar la imagen con el fondo modificado y las líneas cambiadas
img_modificada.save("imagen_motor_modificada.png")