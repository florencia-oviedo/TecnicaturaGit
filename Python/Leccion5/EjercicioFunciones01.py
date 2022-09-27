# Ejercicio 01: Crear una función para sumar los valores recibidos de tipo
# númericos, utilizando argumentos variables *args como parámetro de la
# función y agregar como resultado la suma de todos los valores pasados
# como argumentos.

# Mi forma de hacerlo
def sumar_Numeros(*args):
    suma=0
    for number in args:
        suma += number
    return suma

print(f'La suma de todos los números es: {sumar_Numeros(3,5,9,2,1)}')

# Forma del profe
def sumar_valor(*args): #Recibimos una cantidad de parámetros indefinidos
    resultado = 0
    # Iteramos cada elemento
    for valor in args:
        resultado += valor
    return resultado
# Llamamos a la función
print(sumar_valor(3,5,9,2,1))