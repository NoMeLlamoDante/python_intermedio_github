import csv


with open('console_games.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Name'], row['Platform'])


# id,Rank,Name,Platform,Year,Genre,Publisher,NA_Sales,EU_Sales,JP_Sales,Other_Sales

# Estructura de directorios
 
# Plataform / Year / archivo.txt

# En el archivo debe ir el contenido de la plataforma y el año