# Ejercicio 7: Adivina el número
# Realizar un juego para adivinar un número. Para ello se
# debe generar un número aleatorio del 1 al 100, y luego ir pidiendo
# números indicando "es mayor" o "es menor" según sea mayor o menor
# con respecto a N. El proceso termina cuando el usuario acierta
# y allí se debe mostrar el número de intentos

import random
print("\t.: Juego Adivina el número:. ")
aleatorio = random.randint(0,100) #Toma de 0-100 literal, generamos un número aleatorio
# Mi forma de hacerlo
#num = int(input("Digite un número: "))
# conteo = 1
# while num != aleatorio:
#     if num > aleatorio:
#         print("Es menor")
#     else:
#         print("Es mayor")
#     conteo +=1
#     num = int(input("Digite un número: "))
#
# print(f"¡¡¡FELICIDADES!!! Acertaste el número {aleatorio] con {conteo} intentos")
# Solución del profe
contador = 0
while True:
    num = int(input("Digite un número: "))
    contador += 1
    if num > aleatorio:
        print("\tNo es el número, digite un número menor")
    elif num < aleatorio:
        print("\tNo es el número, digite un número mayor")
    else:
        print(f"¡¡¡FELICIDADES!!!, acabas de adivinar el número {aleatorio}")
        break # rompe el ciclo y el bucle
print(f"\n Número de intentos: {contador}")

