# Actividad excepciones
# Replicar el comportamiento de creacion de carpetas con Windows

# al crear un directorio si ya existe agregarle entre parentesis el consecutivo
# carpeta
# carpeta(1)
# carpeta(2)
import os

loop = '1'
def crear_carpetas(sufijo, cantidad):
    
    for i in range(cantidad):
        os.mkdir(f"{sufijo}{i}")
        print(f"Creando carpeta {sufijo}{i}")
sufijo = input ('Cual es el nombre de tu carpeta? ')

while loop == '1':
    try:
        cantidad = int(input ('Cuantas carpetas quieres crear? '))
        if cantidad >= 0:
            loop = '3' 
    except ValueError as ex:
        print('Debe ser numero entero y entre 0 e infinito...') 

cantidad_clon = cantidad - (cantidad- 1)
try:
    crear_carpetas(sufijo, cantidad)
except FileExistsError as ex2:
    crear_carpetas( f'{sufijo} '+ f'({str(cantidad_clon)})', cantidad)



