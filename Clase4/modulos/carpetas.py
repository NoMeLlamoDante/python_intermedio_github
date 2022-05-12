import os

def crear_carpetas(sufijo, cantidad):
    for i in range(cantidad):
        os.mkdir(f"{sufijo}{i}")
        print(f"Creando carpeta {sufijo}{i}")