import os
from modulos.auth.login import is_authenticated
from modulos.auth.register import singIn
from modulos.auth.delete import delete_user
from modulos.auth.read import read_user, read_users
from modulos.auth.update import update_user
os.system('cls')
#auth 
# User = 'adenisoy'
# password = 'j1JT2nHX'
# email = 'llaurenceauy@pagesperso-orange.fr'
# id = '35'


# Read all users
#print(read_users())
# Search one user
# print(read_user('test3'))
# print(read_user(106))
# print(read_user('correo3@gmail.com'))

# Auth invalid
# print(is_authenticated("user", "pass"))
# Auth Valid
# print(is_authenticated('adenisoy','j1JT2nHX'))

# Sign In 
#n = 7
#print(singIn(f'test{n}', f'pass{n}', f'test{n}@gmail.com'))

# Delete User
#print(delete_user("test4"))

# Update User
print(update_user(107, username="test4", password='pass4', email="eldeprueba@gmail.com"))
# print("end")