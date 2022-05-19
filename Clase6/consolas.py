import csv
import os
ruta = 'D:\\Escuela Documentos\\Python\\Python_Intermedio_Repositorio\\'


with open('console_games.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
       
        try:
            if row ['Platform']:
                carpeta_platform = os.mkdir(row['Platform'])
        except FileExistsError as ex:
            pass

        try:
            if row['Year']:
                carpeta_year = os.mkdir(row['Platform'] + '/' + row['Year'])
        except FileExistsError as ex:
            pass

        if row['Platform']:
            texto_videogames = f"{ruta}{row['Platform']}\\{row['Year']}\\archivo.txt"
            string = ''
            
            for key, value in row.items():
                string += value + ','
            
            string += "\n"
        with open(texto_videogames, 'a') as file_games:
            file_games.write(string)
        


            
