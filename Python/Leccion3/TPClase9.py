#Diseñar un programa que ingresando un año, nos devuelva
#por consola si es un año bisiesto o no,repetir la accion
#hasta que el usuario lo decida

print("Comprobamos que año es bisiesto")
anio = int(input("Ingrese un año: "))
while anio % 4 ==0 and num % 100 == 0 or num%400==0:
    if anio % 4 ==0 and num % 100 == 0 or num%400==0:
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")
    anio = int(input("Ingrese un año: "))
