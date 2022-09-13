# Ejercicio 4: Sumar números pares dentro de un rango
# Hacer un programa para sumar números pares dentro
# de un rango, por ejemplo:
#                           suma de números pares del 2 al 30
#                           suma = 240
#Mi forma
#sumaPares=0
#for i in range(2,31):
#    if i % 2 == 0:
#        sumaPares +=i
#print(f"La suma de los números pares es {sumaPares}")

a = int(input("Digite de donde va a comenzar la suma: "))
b = int(input("Digite hasta donde quiere llegar a sumar: "))
suma = 0
for i in range(a,b+1):
    if i % 2 == 0: #Esto si es un numero par
        suma +=i
print(f'\n La suma de números pares dentro del rango es {suma}')