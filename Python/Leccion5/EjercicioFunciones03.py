# Ejercicio 3: Función Recursiva
# Imprimir números de 5 a 1 de manera descendente usando funciones recursivas
# Puede ser cualquier valor positivo, por ejemplo, si pasamos el
# valor de 5, debe imprimir:
#5
#4
#3
#2
#1
# En caso de ser el número 3 debe imprimir:
#3
#2
#1
# Si se ingresa numeros negativos no imprime nada

def imprimir_numeros_recursivos(numero):
    if numero >= 1: #Caso Base
        print(numero)
        imprimir_numeros_recursivos(numero-1) #Caso Recursivo
    elif numero == 0:
        return
    elif numero <= 0:
        print("Valor ingresado incorrecto...")

imprimir_numeros_recursivos(5) #Tarea : que el numero lo ingrese el usuario
numero = int(input("Digite un número: "))
imprimir_numeros_recursivos(numero)