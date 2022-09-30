# Ejercicio 2: Función con * args para multiplicar
# Crear una función para multiplicar los valores recibidos
# de tipo númerico, utilizando argumentos variables *args
# como parámetro de la función y regresar como resultado
# la multiplicación de todos los valores pasados como argumento

# Mi forma
#def multiplicar_numeros(*args):
#    resultado = 1
#     for number in args:
#         resultado *= number
#     return resultado
#
# print(f'El resultado es: {multiplicar_numeros(3,5,15,3)}')

# Forma del profe
# Definimos la función para multiplicar
def multiplicar_valores(*args): # El más utilizado es args
    resultado = 1 #El cero no nos ayuda a multiplicar
    for numero in args:
        resultado *= numero
    return resultado
# Llamamos a la función
print(multiplicar_valores(3,5,15,3)) #Le pasamos los argumentos