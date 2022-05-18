# Actividad excepciones
# Replicar el comportamiento de creacion de carpetas con Windows

# al crear un directorio si ya existe agregarle entre parentesis el consecutivo
# carpeta
# carpeta(1)
# carpeta(2)
import os

loop = '1'
loop2 = '2'
def crear_carpetas(sufijo, cantidad):
    
    for i in range(cantidad):
        os.mkdir(f"{sufijo}{i}")
        print(f"Creando carpeta {sufijo}{i}")
sufijo = input ('Cual es el nombre de tu carpeta? ')

while loop == '1':
    try:
        cantidad = int(input ('Cuantas carpetas quieres crear? '))
        if cantidad == int:
            loop = '3' 
    except ValueError as ex:
        print('Debe ser numero entero...') 

try:
    crear_carpetas(sufijo, cantidad)
except FileExistsError as ex2:
    crear_carpetas(sufijo,f'({cantidad})'  )



