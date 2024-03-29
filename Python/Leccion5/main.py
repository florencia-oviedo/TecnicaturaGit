# Comenzamos con Funciones
#mi_function() #No se puede llamar antes de definir a una función
#Definimos una función
def mi_function(): #No se puede llamar antes de definir a una función
    print('Saludos a todos los alumnos de la Tecnicatura')

mi_function() #Estamos llamando a la función
mi_function() #Se puede llamar a una función N cantidad de veces

# Desempaquetado de listas o list Unpacking
def show(name,lastName):
    print(name+' '+lastName)
person = ['Ariel','Betancud']
show(person[0],person[1]) # Pasamos uno por uno los datos de la lista a la funcion
show(*person) # Es lo mismo que el anterior pero le pasamos todo junto
person2 = ('Osvaldo','Giordanini') # desempaquetamos a traves de una tupla
show(*person2)
person3 = {"lastName":"Lucero","name":"Natalia"}
show(**person3)

numbers = [1,2,3,4,5]
for n in numbers:
    print(n)
    if n == 3:
        break # Esta es la unica manera para que no se ejecute el else
else:
    print('Esto se terminó')

# List comprenhension, lista de compresion
names = ['Paolo','Rodrigo','Lupe','Pepe']
alongP = [p for p in names if p[0] == 'P'] # Esto regresa una nueva lista
print(alongP)

bottleC = [{"name":"Quilmes","country": "Arg"},
        {"name":"Corona","country": "Mex"},
        {"name":"Stella Artois ","country": "Belgium"},
           ]
Arg = [b for b in bottleC if b["country"]== "Arg"]
print(Arg)
print(bottleC)

# Paso de argumentos (funciones)
def mi_funcion2(name,lastName):
    print("Saludos a todos los que ven a tráves del canal de Youtube")
    print(f"Nombre: {name}, Apellido: {lastName}")
mi_funcion2("Jorge", "Lucero")
mi_funcion2("Ariel", "Betancud")
mi_funcion2("Analia","Pedrosa")

# La palabra return en funciones
# Creamos una funcion para sumar
def sumar(a,b):
    return a + b
#resultado = sumar(78,22)
#print(f'El resultado de la suma es: {resultado}')
print(f'El resultado de la suma es: {sumar(55,45)}')

def sumar2(a = 0,b = 0): # -> le damos un valor por default
    return a + b
resultado = sumar2()
print(f"Resultado de la suma: {resultado}")
print(f"Resultado de la suma: {sumar2(22,66)}")

# Argumentos, variables en funciones
def listarNombres(*nombres): # Normalmente se utiliza: *args
    for nombre in nombres: # Se va a convertir en una tupla
        print(nombre)
listarNombres('Lucas','José','Claudia','Rosa','María')
listarNombres('Marcos','Daniel','Romina','Pepe','Marcela','Carlos')

#Argumentos variables para un diccionario
def listarTerminos(**terminos): # Lo mas utilizado es **kwargs para recibir argumentos
    for llave,valor in terminos.items(): #kwargs significa: key word argument
        print(f'{llave} : {valor}')

listarTerminos() # no recibe nada y nada se va a mostrar
listarTerminos(IDE = 'Integrated Development Enviroment',PK = 'Primary key')
listarTerminos(Nombre = 'Leonel Messi')

# Distintos tipos de datos como argumentos
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ['Tito','Pedro','Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla')
#desplegarNombres(10,11) No es un objeto iterable es un int
desplegarNombres((10, 11)) # Los convertimos en una tupla, en un solo elemento no olvidar la coma
desplegarNombres([22, 55]) # La convertimos en una lista

#Funciones recursivas
def factorial(numero):
    if numero == 1: # Caso base
        return 1
    else:
        return numero*factorial(numero-1) # Caso recursivo

resultado = factorial(5) # Lo hacemos en codigo duro
print(f'El factorial del numero 5 es: {resultado}')
# Tarea : que el usuario ingrese el numero para calcular el factorial
numero = int(input("Digite un número para calcular el factorial: "))
resultado = factorial(numero)
print(f'El factorial del numero {numero} es: {resultado}')
