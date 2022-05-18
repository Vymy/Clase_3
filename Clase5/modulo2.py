# pasar todo lo del monitor 1 a un archivo de texto
# crear una carpeta donde se almacenaran los logs 
# crear un archivo con X nombre 
# insertar la informacion recabada en el archivo
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

info = "Informacion del sistema"
nuc = "Nucleos del CPU => ", cpu_nucleos
cpu = "Frecuenca del CPU => ", cpu_frecuencia
mem ="Memoria virutal => ", memoria_virtual
disk = "Uso de disco => ", disco_uso

print(info)
print(nuc)
print(cpu)
print(mem)
print(disk)

with open("text2.txt", "w") as archivo:
    archivo.write(info)
    archivo.write(nuc)
    archivo.write(cpu)
    archivo.write(mem)
    archivo.write(disk)