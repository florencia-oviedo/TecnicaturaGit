miVariable = 3
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
