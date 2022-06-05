from auth.login import is_authenticated
import os
os.system('cls')


#print(is_authenticated("usuari", "contrase"))
#print(is_authenticated("raughtonm", "rSIoQQYc"))

if is_authenticated("raughtonm", "rSIoQQYc"):
    print("bienvenido usuario")
else:
    print("credenciales incorrectas")


if  not is_authenticated("raughtonm", "rSIoQQYcx"):
    print("credenciales invalidas")