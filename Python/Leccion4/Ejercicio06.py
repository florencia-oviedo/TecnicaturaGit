# Ejercicio 6: Tabla de multiplicar
# Hacer un programa que pida un número por teclado y guarde
# en una lista su tabla de multiplicar hasta el 10. Por ejemplo:
# Si digita el 5 la lista tendrá: 5,10,15,20,,25,30,35,40,45,50

num = int(input('Digite un número para multiplicar:'))
lista = []

for i in range(1,11):
    lista.append(i*num)
print(f'\n Tabla de multiplicar del {num} : \n {lista}')

print()
#for i in range(1,11):
#    print(f'{num} x {i} = {num*i}')

for indice,i in enumerate(lista):
    print(f'{num} x {i} = {lista[indice]}')
