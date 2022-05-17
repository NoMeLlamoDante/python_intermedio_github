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
    creada = False
    iteracion = 0
    while not creada:
        TemporaryDirectory = path
        try:
            if iteracion>0:
                TemporaryDirectory = f"{path}({iteracion})"
            os.mkdir(TemporaryDirectory)
            creada = True
        except FileExistsError as err:
            iteracion+=1
    return(TemporaryDirectory)


print(crearCarpeta("carpeta"))
#recorre directorio hasta encontrar iteración
##while carpeta_existe:
#    contenido = os.listdir("C:\\Users\\EOZM2\\Documents\\python_intermedio_github")
#    # Recorre la lista 
#    for carpeta_existente in contenido:
#        #busca coincidencias
#        if carpeta_existente == carpeta_nueva:
#            iteracion+=1
#            break
#        #si no encuentra ninguna carpeta trata de crearla
#        try:
#            if iteracion == 0:
#                os.mkdir(carpeta_nueva)
#                print("carpeta creada con éxito")
#                carpeta_creada = FALSE;
#            else:
#                os.mkdir(f"{carpeta_nueva}({iteracion})")
#
#        except Exception as ex:
#            print("Error al crear carpeta => ",ex)
#            break
#        
#    
#
#
##print(contenido)