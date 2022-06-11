#Ejercicio 5
"""nota= int(input("Digite su nota de 0-10: "))
calificacion= None

if nota==10 or nota==9:
    calificacion= "A"
elif 8<=nota<9:
    calificacion= "B"
elif 7<=nota<8:
    calificacion= "C"
elif 6<=nota<7:
    calificacion= "D"
elif 0<=nota<6:
    calificacion= "F"
else:
    calificacion= "El valor ingresado es incorrecto"
print(f'La nota es: {nota} y su calificacion es: {calificacion}') """

#Profe
calificacion=int(input('Digite una calificacion entre 0 y 10'))
if 9<= calificacion<=10:
    print('A')
elif 8<=calificacion<9:
    print('B')
elif 7<=calificacion<8:
    print('C')
elif 6<=calificacion<7:
    print('D')
elif 0<=calificacion<6:
    print('F')
else:
    print('Valor incorrecto...')
