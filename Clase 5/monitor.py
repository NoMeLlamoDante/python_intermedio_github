
# https://psutil.readthedocs.io/en/latest/

#nucleos del cpu
import psutil
import os

#datos del CPU
cpu_nucleos = psutil.cpu_count()
cpu_frecuencia = psutil.cpu_freq()

#Memoria
memoria_virtual = psutil.virtual_memory()

#Disco Duro
disco_uso = psutil.disk_usage('/')


os.system('clear')

print("="*50)

print("informacion del sistema")
print("Nucleos del CPU => ", cpu_nucleos)
print("Frecuencia del CPU ", cpu_frecuencia)
print("Memoria Virtual => ", memoria_virtual)
print("Uso del disco duro => ", cpu_nucleos)

print("="*50)