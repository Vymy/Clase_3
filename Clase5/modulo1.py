# Actividad excepciones
# Replicar el comportamiento de creacion de carpetas con Windows

# al crear un directorio si ya existe agregarle entre parentesis el consecutivo
# carpeta
# carpeta(1)
# carpeta(2)

import psutil
import os

# nucles del cpu
cpu_nucleos = psutil.cpu_count()
cpu_frecuencia = psutil.cpu_freq()

# memoria
memoria_virtual = psutil.virtual_memory()

# disco
disco_uso = psutil.disk_usage('/')

os.system('clear')

print("=" * 50)

print("Informacion del sistema")
print("Nucleos del CPU => ", cpu_nucleos)
print("Frecuenca del CPU => ", cpu_frecuencia)

print("Memoria virutal => ", memoria_virtual)

print("Uso de disco => ", disco_uso)

print("=" * 50)