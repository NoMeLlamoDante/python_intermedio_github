#Manejo de excepciones cuando creamos un directorio
import os

try: 
    os.mkdir("carpeta prueba")
except FileExistsError as ex:
    print("ya existe ese directorio, intenta con otro nombre")
except FileNotFoundError as ex:
    print("no se encontró el directorio proporcionado")
except Exception as ex:
    print("oops ocurrió un error")

print("Fin del script")