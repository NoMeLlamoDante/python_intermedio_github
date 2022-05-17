# manejo de excepciones con python


try:   
    respuesta = int(input("please enter a number: "))
except ValueError as ex:
    print("hubo un error de valor => ", ex)
except Exception as ex:
    print("hubo una excepcion => ",ex)

print("este codigo se ejecuta siempre")