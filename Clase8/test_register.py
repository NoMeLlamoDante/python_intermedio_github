from auth.register import singIn
import os

os.system('cls')


#print(is_authenticated("usuari", "contrase"))
#print(is_authenticated("raughtonm", "rSIoQQYc"))
consec = 20
if singIn(f"test{consec}",  f"pass{consec}", f'test{consec}@mail.com', 0):
    print("Usuario Registrado correctamente")
else:
    print("falla al registrar")


consec+=1;
singIn(f"test{consec}",  f"pass{consec}", f'test{consec}@mail.com', 0)
consec+=1;
singIn(f"test{consec}",  f"pass{consec}", f'test{consec}@mail.com', 0)
consec+=1;
singIn(f"test{consec}",  f"pass{consec}", f'test{consec}@mail.com', 0)