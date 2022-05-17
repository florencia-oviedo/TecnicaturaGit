""" miVariable = 3
print(miVariable)
miVariable = "Hola a todos los alumnos de la tecnicatura"
print(miVariable)
miVariable = 3.5
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))
# Las literales se escriben de la siguiente manera x776 (la x no tiene q ver con la variable) si ejecutamos cambia
# de id y=x184 y z= x504
print(id(y))
print(id(z))

# Tipos int (enteros), float (decimal) , string (text), boolean (booleanos)
x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola alumnos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# Manejo de cadenas (string)
miGrupoFavorito = "The Beatles: "
caracteristicas = "The bes rock band"
print("Mi grupo favorito es: ", miGrupoFavorito, caracteristicas)

#numero1 = "7"
#numero2 = "8"
#print(int(numero1) + int(numero2))
# Tipos de Booleanos (bool)
miBooleano = 3 > 2
print(miBooleano)
if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

# Procesar la entrada del usuario
 #funcion input
#resultado = input("Digite un numero: ")#Regresa un dato tipo string
#print(resultado)

 #Conversion de la entrada de datos
numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))
resultado = numero1 + numero2
print("El resultado de la suma es: ", resultado)

operandoA= 8
operandoB= 5
suma= operandoA + operandoB
print("Resultado de la suma: ", suma)
print(f"El resultado de la suma es: {suma}")
resta= operandoA - operandoB
print(f"El resultado de la resta es: {resta}")
multiplicacion= operandoA * operandoB

print(f"El resultado de la multiplicacion es: {multiplicacion}")
division= operandoA/operandoB
print(f"El resultado de la division es: {division}")
division= operandoA// operandoB # Devuelve el numero entero de la division
print(f"El resultado de la division en numero entero es {division}")
modulo= operandoA % operandoB
print(f"El resultado del modulo es {modulo}")
exponente= operandoA ** operandoB
print(f"El resultado del exponente es {exponente}")
"""
#Ejercicio rectangulo
"""
alto= int(input("Proporcione el alto del rectángulo: "))
ancho= int(input("Proporcione el ancho del rectángulo: "))
area= alto*ancho
perimetro= (alto + ancho)*2
print(f"El área del rectángulo es {area} y el perímetro es {perimetro}")
"""
"""
miVariable3= 10
print(miVariable3)

# Operadores de reasignacion
miVariable3= miVariable3 + 1
print(miVariable3)
#Lo mismo q antes pero resumido
miVariable3 += 1
print(miVariable3)
# Se puede con todos los operadores aritmericos
# miVariable3= miVariable3  - 2
miVariable3 -=2
print(miVariable3)
# miVariable3= miVariable3*3
miVariable3 *=3
print(miVariable3)
# miVariable3= miVariable3/2
miVariable3 /=2
print(miVariable3)
"""
"""
# Operadores de comparación nos permite ver si son iguales o distintos
d= 4
b= 4
resultado= d== b #Comprobamos si son iguales
print(resultado)

#Ejercicio numeros primos




#Ejercicio edad
edad= int(input("Digite su edad: "))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
"""
"""
# Valor dentro de un rango
num= int(input("Digite un número: "))
if num>=0 and num<=5:
    print(f"El número {num} ingresado está en el rango")
else:
    print(f"El número {num} ingresado está fuera del rango")
"""
"""
#Ejercicio Operador Or, operador NOT
vacaciones = False
diaDescanso= False
if not(vacaciones or diaDescanso):
    print("Tiene trabajo que hacer")
else:
    print("Puede asistir al juego")
"""
#Ejercicio rango de edades
num= int(input("Digite su edad: "))
""" if num>=20 and num<30 or num>=30 and num<40:
    print(f"Su edad {num} está dentro del rango")
else:
    print(f"Su edad {num} está fuera de rango")"""
#Ejercicio rango de edades del profe: temas identacion (sangria)


#Sintaxis mas simplificada del operador and
if (20 <=num < 30) or (30<= num <40):
    print(f"Su edad {num} está dentro del rango")
else:
    print(f"Su edad {num} está fuera de rango")

