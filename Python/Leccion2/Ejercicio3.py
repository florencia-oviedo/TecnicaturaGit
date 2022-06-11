#Ejercicio3
#hecho por mi
"""mes= int(input("Digite un mes de 1-12: "))
if mes==12 or mes<=3 and mes>=1:
    print("Está en  Verano")
elif mes>3 and mes<=6:
    print("Está en Otoño")
elif mes>6 and mes<=9:
    print("Está en Invierno")
elif mes>9 and mes<12:
    print("Está en Primavera")
else:
    print("Ingreso numero incorrecto, digite nuevamente")"""


#Hecho por el profe
mes= int(input("Digite un mes de 1-12: "))
estacion= None
if mes==1 or mes ==2 or mes==3:
    estacion= "Verano"
elif mes==4 or mes ==5 or mes==6:
    estacion= "Otoño"
elif mes==7 or mes ==8 or mes==9:
    estacion= "Invierno"
elif mes==10 or mes==11 or mes==12:
    estacion= "Privamera"
else:
    estacion= "Error , no hay numero para este mes"

print(f'Para el mes {mes} la estación es: {estacion}')