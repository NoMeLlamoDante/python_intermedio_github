# pasar todo lo del monitor 1 a un archivo de texto
# crear una carpeta donde se almacenaran los logs 
# crear un archivo con X nombre 
# insertar la informacion recabada en el archivo


# Imports
import psutil
import os

#datos del CPU
cpu_nucleos = psutil.cpu_count()
cpu_frecuencia = psutil.cpu_freq()

#Memoria
memoria_virtual = psutil.virtual_memory()

#Disco Duro
disco_uso = psutil.disk_usage('/')


#crear Carpeta
os.mkdir(f"logs")

with open("logs/log.txt", "w") as archivo: 
    archivo.write(f"Datos de PC\n cantida de nucleos: {cpu_nucleos} \nfrecuencia: {cpu_frecuencia} \n memoria Virtual: {memoria_virtual}\n Disco duro: \n")