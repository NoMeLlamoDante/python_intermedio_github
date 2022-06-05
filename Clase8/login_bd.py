import psycopg2
import os
os.system('cls')

conn = psycopg2.connect("dbname=python_intermedio_db user=postgres password=root")
cur = conn.cursor()

# inicio de sesion con un usuario de la base datos
# user = raughtonm
# password = rSIoQQYc

# fetchone() obtiene un registro
# fetchall() obtienete todos los registros
# rowcount
# rownumber

# solicitar usuario y contraseña
usuario = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")

# consulta SQL lanzar el query
#Busca el usuario en la BD
consulta = f"SELECT username, password FROM usuarios WHERE username=\'{usuario}\' AND password = \'{password}\';"

# mandar el query a la BD
cur.execute(consulta)

# mostrar el resultado de la base datos
#print(cur.fetchall()) <- retorna una lista de tuplas con los resultados
usuario_encontrado = cur.fetchone() # <- retorna una tupla con 1 solo resultado
#usuario_encontrado = cur.rowcount
print(usuario_encontrado)

# si encontramos un usuario con esos datos mandar un mensaje de bienvenida
if len(usuario_encontrado) > 0:
    print(f"Bienvenido {usuario_encontrado[0]}")
# si el resultado es incorrecto mandar mensaje de volver a ingresar usuario y contraseña
else:
    print("usuario incorrecto, intente de nuevo")

cur.close()
conn.close()

