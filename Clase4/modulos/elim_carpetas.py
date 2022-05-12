import os

def del_carpetas(nombre, numero):
    for i in range(numero):
        os.mkdir(f"{nombre}{i}")
        print(f"Creando carpeta {nombre}{i}")