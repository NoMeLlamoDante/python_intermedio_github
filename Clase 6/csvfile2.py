import csv
from genericpath import exists
import os
from platform import platform
from site import makepath

ruta = "clase 6\\practica\\"

with open('console_games.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(f"platforma => {row['Platform']} año => {row['Year']}")

        try:
            if row['Platform']:
                os.makedirs(f"{ruta}{row['Platform']}\\{row['Year']}")
        except FileExistsError as ex:
                pass
        if row['Platform']:
            ruta_archivo = f"{ruta}{row['Platform']}\\{row['Year']}\\archivo.txt"
            cadena = ""
            for key, value in row.items():
                cadena += value + ","
            cadena+="\n"
            with open(ruta_archivo, 'a') as archivo:
                archivo.write(cadena)


        ##print(row['Name'], row['Platform'])
        #pathFile = f"{row['Platform']}\\{row['Year']}\\videogames.txt"
        #exist_txt = os.path.isfile(pathFile)
        ## Revisa el archivo
        #if not exist_txt:
        #    # revisa Ruta Plataforma
        #    PathPlatform = f"{row['Platform']}"
        #    makepath(PathPlatform)
        #    
        #    # revisa ruta año
        #    PathYear = f"{row['Platform']}\\{row['Year']}"
        #    makepath(PathYear)
        #    
        #with open(pathFile, "a") as archivo: 
        #    text = f"{row},"
        #    archivo.write(text)
        ## id,Rank,Name,Platform,Year,Genre,Publisher,NA_Sales,EU_Sales,JP_Sales,Other_Sales
    
def makePath(path):
    exist = os.path.isdir(path)
    if not exist:
        #Crear ruta Plataforma
        os.mkdir(path)
#path = f"{os.getcwd()}\\{'nintendo'}"
# print(os.path.isfile(path) )
#print(os.path.isdir('nintendo'))

# Estructura de directorios
# Plataform / Year / archivo.txt

# En el archivo debe ir el contenido de la plataforma y el año