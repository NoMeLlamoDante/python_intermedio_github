import os
from tempfile import TemporaryDirectory
# Actividad excepciones
# Replicar el comportamiento de creación de carpetas con windows

#al crear una carpeta o directorio, si ya existe, agregar entre paréntesis el consecutivo
#carpeta
#carpeta(1)
#carpeta(2)
#carpeta(3)

def crearCarpeta(path):
    iteracion = 0
    while True:
        TemporaryDirectory = path
        try:
            if iteracion>0:
                TemporaryDirectory = f"{path}({iteracion})"
            os.mkdir(TemporaryDirectory)
            break
        except FileExistsError as err:
            iteracion+=1
    return(TemporaryDirectory)

print(crearCarpeta("carpeta"))