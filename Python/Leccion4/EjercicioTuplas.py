import math #Importamos la clase math para hacer uso de la funcion sqrt(raiz cuadrada)
#Dada la siguiente tupla
tupla = (13,1,8,3,2,5,8) #definimos la tupla
#Crear una lista que solo incluya los numeros menores a 5
# e imprima por consola [1,3,2]

lista = []
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)

#Ejercicio de matemáticas
# Para sacar la raiz cuadrada de un número positivo
numero = int(input("Digite un número positivo: "))
while numero < 0:
    print("error -> Debería ser un número positivo")
    numero = int(input("Digite un número positivo: "))
print(f'\nSu raiz cuadrada es: { math.sqrt(numero):.2f}')