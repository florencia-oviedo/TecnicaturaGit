# Ejercicio 1: Llenar una lista
# Llenar con una lista de 1 al 50, luego mostra
# la lista con el bucle for, los elementos deben mostrarse de la siguiente forma:
# 1-2-3-4-5...-50
#lista = []
#i = 1
#while i<=50:
    #lista.append(i)
    #i +=1
lista = list(range(1,51)) #algoritmo eficaz
for i in lista:
    print(i,end="-")