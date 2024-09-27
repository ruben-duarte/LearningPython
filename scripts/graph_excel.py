import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import numpy as np

# Cargar el archivo CSV
# Si tu archivo está guardado localmente, cambia 'ruta_del_archivo.csv' por la ruta correcta
df = pd.read_csv('F:\\archivos pruebs ANDres\\1._10724ccipschipiron consolidado gd.csv', delimiter=';', skipinitialspace=True)

# Seleccionar la columna "On Voltage"
on_voltage = df['On Voltage']
# off_voltage = df['Off Voltage']


# Parámetros del filtro =======
window_size = 7  # Tamaño de la ventana (debe ser un número impar)
poly_degree = 3  # Grado del polinomio para el ajuste
error_rate_threshold = 0.05  # Tasa de error para resaltar las diferencias

# Aplicar el filtro Savitzky-Golay a la columna "On Voltage"
smoothed_on_voltage = savgol_filter(on_voltage, window_length=window_size, polyorder=poly_degree)

# Calcular el error entre los datos originales y suavizados ======
error = np.abs(on_voltage - smoothed_on_voltage)



#better styling
# Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(10, 6))

# Establecer el color de fondo azul oscuro para la figura y los ejes
fig.patch.set_facecolor('#0A1F44')  # Fondo de la figura
ax.set_facecolor('#0A1F44')         # Fondo del área de la gráfica

# Personalizar la línea de la gráfica
ax.plot(on_voltage, marker='o', linestyle='-', color='#07A7F2', linewidth=1, markersize=2,  markerfacecolor='#FFEB6B', markeredgecolor='#FFEB6B')

# Graficar "Off Voltage"
# ax.plot(off_voltage, marker='s', linestyle='-', color='#FFD700', linewidth=1, 
#         markersize=2, markerfacecolor='#FF8C00', markeredgecolor='#FFFFFF', label='Off Voltage')


# Graficar "On Voltage" suavizado ======
ax.plot(smoothed_on_voltage, marker='', linestyle='-', color='#FFD700', linewidth=3, 
        label='On Voltage Smoothed')

# Invertir el eje y
#plt.gca().invert_yaxis()

# Resaltar los puntos con error significativo (diferencia entre original y suavizado)
anomalous_points = error > error_rate_threshold
ax.plot(np.where(anomalous_points)[0], on_voltage[anomalous_points], 'ro', label='Error Points')

# Añadir una leyenda para identificar las series =========
ax.legend(loc='upper right', fontsize=12, facecolor='#0A1F44', edgecolor='white')


# Personalizar el título y las etiquetas con colores claros para contraste
ax.set_title('On Voltage Over Time', fontsize=18, color='#FFFF67')
ax.set_xlabel('Distance', fontsize=14, color='#FFFF67')
ax.set_ylabel('Frequency (V)', fontsize=14, color='#FFFF67')

# Añadir una cuadrícula personalizada para mejorar la visibilidad en el fondo oscuro
ax.grid(color='#4A4A4A', linestyle='--', linewidth=0.5)

# Personalizar los ticks (números del eje) para que sean visibles
ax.tick_params(axis='x', colors='white')
ax.tick_params(axis='y', colors='white')

# Mostrar la gráfica
plt.show()
