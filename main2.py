import os
# importing sys  
from modulos.auth.register import singIn
from modulos.auth.login import is_authenticated
from modulos.auth.delete import delete_user
from modulos.auth.read import read_user, read_users
from modulos.auth.update import update_user
mensajes = {}

mensajes['unlogedOptions'] = """
Bienvenid@ al sistema CRUD de usuarios
Selecciona una opcion
1 - Login
2 - Registro
3 - Salir
-> """ 
mensajes['signInInfo'] = """
Par registrar un usuario necesistas proporcionar
- Nombre de usuario
- Contraseña
- Correo electronico
"""
mensajes['signInWait'] = "\nRegistrando el usuario, espere por favor..."
mensajes['signInMsg'] = "\nUsuario %s registrado con exito"
mensajes['logInInfo'] = "Para iniciar sesion ingreas tu usuario y contraseña"
mensajes['loged'] = "\nBienvid@ %s al CRUD de usuarios"
mensajes['logedOptions'] = """
Elige una opcion
1- Mostrar informacion del usuario
2- Modificar usuario
3- Borrar usuario
4- Salir
-> """
mensajes['userInfo'] = """\nTu informacion %s es la siguiente:
ID:%s
Usuario: %s
Contraseña: %s
Email: %s
Status: %s
"""
mensajes['editOptions']= """
Elige un dato a modicar 
1- Usuario
2- Contraseña
3- Email
4- Status
-> """

#Logged
def logged():
    while True:
        selected_option = int(input(mensajes['logedOptions']))
        os.system('cls')
        # Search User
        if selected_option == 1:
            search = input('Ingrese Parametro de busqueda: ')

            try:
                search = read_user(int(search))
            except : 
                search = read_user(search)

            # If user Exist
            if search:
                print(mensajes['userInfo']%("",search[0],search[1],search[2],search[3],search[4]))
            else:
                print("Usuario no encontrado")

        # Update User
        if selected_option == 2:
            # User to update
            search = input('Ingrese Parametro de busqueda para edición: ')

            try:
                search = read_user(int(search))
            except : 
                search = read_user(search)

            #if User Exist
            if search:
                print(mensajes['userInfo']%("actual",search[0],search[1],search[2],search[3],search[4]))
            else:
                print("Usuario no encontrado")

            update_option = int(input(mensajes['editOptions']))

            os.system('cls')

            if update_option == 1:
                update_info = input('Inserte Usuario: ')
                update_user(search[0], username=update_info)

            if update_option == 2:
                update_info = input('Inserte Contraseña: ')
                update_user(search[0], password=update_info)

            if update_option == 3:
                update_info = input('Inserte Email: ')
                update_user(search[0], email=update_info)

            if update_option == 4:
                update_info = int(input('Inserte Status: '))
                update_user(search[0], status=update_info)

            # Read Update Data
            search = read_user(search[0])
            print(mensajes['userInfo']%("actualizado",search[0],search[1],search[2],search[3],search[4]))

        # Delete User
        if selected_option == 3:
            search = input('Ingrese Parametro de busqueda: ')

            try:
                search = delete_user(int(search))
            except : 
                search = delete_user(search)

            # If Deleted
            if search:
                print('usuario eliminado con éxito')
            else:
                print("Usuario no encontrado")
        
        if selected_option == 4:
            break;
        input("="*20)


#Login
while True:
    os.system('cls')
    selected_option = int(input(mensajes['unlogedOptions']))
    # Log In
    if selected_option == 1:
        os.system('cls')

        print(mensajes['logInInfo'])
        #read Data Login
        usuario = input("Usuario: ")
        password = input("Contraseña: ")

        if is_authenticated(usuario, password):
            print(mensajes['loged']%usuario)
            logged()
        else:
            print("Usuario Invalido")
        input("="*20)

    # Sign Up
    if selected_option == 2:
        os.system('cls')

        print(mensajes['signInInfo'])
        # Read Data Sign In
        usuario = input("Usuario: ")
        password = input("Contraseña: ")
        email = input("Email: ")

        print(mensajes['signInWait'])

        if singIn(usuario, password, email):
            print(mensajes['signInMsg']%usuario)
            input("==> regresar <==")
    
    # Exit
    if selected_option == 3:
        break

