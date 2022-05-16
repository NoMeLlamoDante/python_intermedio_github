# Practica de manipulación de archivos con python
# Open

archivo = open("texto.txt", "w")

archivo.write("hola\n")
archivo.write("mundo")

archivo.close()

xlsx = open("texto.xlsx", "w")

xlsx.write("hola\n")
xlsx.write("mundo")

xlsx.close()
print("Termino la manipulación de archivos")