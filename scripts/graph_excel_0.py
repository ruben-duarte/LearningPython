def read_file():
    with open("F:\\archivos pruebs ANDres\\1._10724ccipschipiron consolidado gd.csv") as file:
        content = file.read()
    return content

text  = read_file()
print(print(text))

# Usar un estilo moderno con modo oscuro
# plt.style.use('dark_background')

# Graficar los datos de "On Voltage"
# plt.figure(figsize=(10, 6))
# plt.plot(on_voltage, marker='o', linestyle='-')
# plt.title('On Voltage', fontsize=14, color='#FFFF67')
# plt.xlabel('distance',fontsize=12, color='#FFFFFF')
# plt.ylabel('Voltage',fontsize=12, color='#FFFFFF')
# plt.grid(True)
# plt.show()