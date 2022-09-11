#Colecciones en Python
#Las listas se los conoce en otros lenguajes como arreglos o vectores
# lista = Ariel,Liliana , Natalia, Osvaldo puede ser cualquier tipo de dato

nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']
print(nombres)
print(nombres[0:2]) #solo muestra el indice 0 y 1
#ir al inicio de la lista hasta el indice (sin incluirlo)
print(nombres[ :3])

#Desde el indice indicado hasta el final
print(nombres[1: ])

#Modificamos un valor
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)

# Iterar la lista

for nombre in nombres:
    print(nombre)
else:
    print("se acabaron los elementos de la lista")

# Preguntamos cuantos elementos tiene una lista

print(len(nombres)) #le pasamos como parametro una lista

# agregamos un elemento a la lista

nombres.append('Marcelo')
nombres.append([1,2,3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4,5])
nombres.append(7)
print(nombres)

#Insertar un elemento en un indice especifico

nombres.insert(1,'Alberto')
print(nombres)
nombres.insert(3,'Debora')
print(nombres)

#Eliminar elemento

nombres.remove('Alberto')
print(nombres)

#Eliminar el ultimo elemento
nombres.pop()
print(nombres)

#Eliminar un indice especifico

del nombres[2]
print(nombres)

#Eliminar o borrar o limpiar todos los elementos

nombres.clear()
print(nombres)

#Eliminar lista completamente

del nombres
#print(nombres)

# Definimos una tupla
cocina = ('cuchara','cuchillo','tenedor')
print(cocina)
print(len(cocina))

#Acceder a un elemento de una tupla utilizamos CORCHETES NO PARENTESIS
print(cocina[0])

#Mostrar de manera inversa
print(cocina[-1])

#Acceder a un rango
print(cocina[0:2])

#Ejemplo
#verduras= ('papa') No es tupla es una cadena String
verduras = ('papa',) #es una tupla porque tiene aunque sea elemento y tiene una coma!

# Recorremos los elementos de una tupla

for cocinar in cocina:
    print(cocinar, end=" ") #Print esta utilizando \n para saltos de linea y eliminamos eso con end=''

cocinaLista= list(cocina) #Nuestra tupla cocina pasa a una lista
cocinaLista[0]= 'plato' #modificacos un elemento
cocina= tuple(cocinaLista) #La lista pasa a tupla
print('\n',cocina)

#Eliminar una tupla
#del cocina
#print(cocina)

#Tipo set
planetas = {'Marte','Júpiter','Venus'}
print(len(planetas)) #Usamos len = length significa largo

#Revisar si un elemento existe en un tipo set
print('Júpiter' in planetas)

#Agregar elemento

planetas.add('Tierra') #add es una función
planetas.add('Tierra')
print(planetas)

#Eliminar elementos, puede arrojar error si el elemento no existe
planetas.remove('Júpiter') #Esta funcion ante un mal ingreso o inexistente elemento arroja error
print(planetas)
planetas.discard('tierra') #Esta funcion no nos presenta ningun error
print(planetas)

#Limpiar set

planetas.clear()
print(planetas)

#Eliminar set

del planetas
#print(planetas) muestra error

#Diccionario
# 'Maradona'=10 un diccionario esta compuesto por dos elementos
# UNA LLAVE Y UN VALOR ASOCIADO
# dic(key,value)
diccionario = {
    'IDE':'Integrated Development Environment',
    'POO': 'Programación Orientado a Objetos',
    'SABD': 'Sistema de Administración de Base de Datos'
}
#Verificar la cantidad de elementos de un diccionario
print(len(diccionario))
print(diccionario)

#Acceder a un diccionario con llave(key)
print(diccionario['IDE'])

#otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

#Modificar los elementos

diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

#Como recorrer los elementos

for termino in diccionario: #Recorremos solo las llaves
    print(termino)

#Necesitamos una funcion para recorrer un diccionario

for termino,valor in diccionario.items():
    print(termino,valor)

#Otras maneras de acceder a un diccionario

for termino in diccionario.keys(): # fx que solo muestra las llaves
    print(termino)

for valor in diccionario.values(): # fx solo muestra los valores
    print(valor)

#Comprobar la existencia de un elemento
print('IDE' in diccionario) #devuelve un booleano

#Agregar un elemento
diccionario['PK'] = 'Primary key'
print(diccionario)

#Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

#Vaciar un diccionario
diccionario.clear()
print(diccionario)

#Eliminar diccionario
del diccionario #El diccionario se borro

#Concatenamos dos listas
lista1 = [1,2,3,1]
lista2 = [4,5,6,1]
lista3 = lista1 + lista2 #Concatenacion
print(lista3)
lista3.extend([7,8,9,1]) #Funcion para agregar varios elementos a una lista
print(lista3)
print(lista3.index(5)) #Para saber en que indice esta el elemento ingresado
#print(lista3.index(0)) esto da error porque el elemento es inexistente en la lista3

#Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1)) #cuenta cuantos valores iguales hay dentro de una lista

#Para poner al reves una lista
lista3.reverse()
print(lista3)

#Para que una lista se multiplique repitiendo  sus elementos
lista3= lista3 * 2
print(lista3)

# Métodos de ordenamiento
lista3.sort() #Ordena ascendentemente los elementos
print(lista3)
lista3.sort(reverse=True) #Ordena descendentemente los elementos
print(lista3)

tupla = (4,'Hola',6.78,[1,2,78],True,4,'Hola') #Puede tener diferentes de tipos de datos
print(tupla)
print(4 in tupla) #Accion booleana su respuesta es booleana
#Lo que podemos usar en tuplas: index,count,len
#En tuplas se puede convertir de tupla a lista y de lista a tupla

conjunto1 = set()
conjunto2 = {'bye',}
conjunto1.add(7)
conjunto1.add('Hola')
print(conjunto1)
conjunto2.add('hola')
print(conjunto2)
print(3 not in  conjunto2) #Preguntamos si el numero 3 NO esta en el conjunto1

#Como hacer la igualdad entre 2 conjuntos
print(conjunto1 == conjunto2) #Devuelve booleano

#Operaciones con conjuntos
conjunto3 = conjunto1 | conjunto2 #Une a los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2 #que elemento tienen en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 #Asigna el valor que esta en el conjunto 1 y no en el conjunto 2
print(conjunto3)

conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 #elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto1.issubset(conjunto3)) #Aqui preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto2.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) #Preguntamos si los elementos del conjunto 1 estan dentro del 3
print(conjunto3.issuperset(conjunto2)) #Si es verdadero quiere decir que el conjunto 3 es un superconjunto
print(conjunto2.issuperset(conjunto3))

#Como saber si ambos conjuntos son disconexos,esto es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2)) #No hay cosas en comun

#Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset #Esto hace q el conjunto sea totalmente inmutable
#No se puede agregar, modificar ni eliminar elementos del conjunto

#Repaso diccionario
diccionarioNuevo = { 'Azul': 'Blue', 'Rojo':'Red', 'Verde':'Green','Amarillo':'Yellow'}
print(diccionarioNuevo)

#Como eliminar
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

#Los diccionarios pueden almacenar diferentes tipo de datos
diccionario2 = {'Ariel':{'Edad': 40, 'Altura':1.83},'Osvaldo': [45,1.85],'Natalia':[35,1.67]}
print(diccionario2)

seleccionArgentina = {
    10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 millones', 'Posición': 'Extremo derecho'},
    11: {'Nombre': 'Angel Di Maria','Edad': 34, 'Altura': 1.80, 'Precio': '12 millones', 'Posición': 'Extremo derecho' },
    21: {'Nombre': 'Paulo Dybala','Edad': 28, 'Altura': 1.77, 'Precio': '35 millones', 'Posición': 'Media Punta' },
    19: {'Nombre': 'Nicolas Otamendi','Edad': 34, 'Altura': 1.83, 'Precio': '3.5 millones', 'Posición': 'Defensa Central'},
    1: {'Nombre': 'Franco Armani','Edad': 35, 'Altura': 1.89, 'Precio': '3.5 millones', 'Posición': 'Portero'},
    7: {'Nombre': 'Rodrigo De Paul','Edad': 28, 'Altura': 1.80, 'Precio': '40 millones', 'Posición': 'Mediocampista'},
    8: {'Nombre': 'Marcos Acuña','Edad': 30, 'Altura': 1.72, 'Precio': '18 millones', 'Posición': 'Lateral Izquierdo'},
    17: {'Nombre': 'Alejandro Gomez','Edad': 34, 'Altura': 1.67, 'Precio': '6 millones', 'Posición': 'Medio Centro Ofensivo'},
    5: {'Nombre': 'Leandro Paredes','Edad': 28, 'Altura': 1.80, 'Precio': '17 millones', 'Posición': 'Mediocampista'},
    3: {'Nombre': 'Nicolas Tagliafico','Edad': 30, 'Altura': 1.72, 'Precio': '11 millones', 'Posición': 'Lateral Izquierdo'},
}
for llave,valor in seleccionArgentina.items():
    print(llave,valor)
#Como tarea agregar por lo menos 4 jugadores más al diccionario seleccion argentina

print("Tenemos cargados en el diccionario la cantidad de jugadores: ", end="")
print(len(seleccionArgentina))

#Pilas usando listas
pila = [1,2,3]

#Agregar elementos a la pila final
pila.append(4)
pila.append(5)
print(pila)

#Sacamos elementos desde el final
elementoBorrado = pila.pop() #elimina el ultimo elemento de la lista y lo guarda en una variable
print(f'El elemento borrado es {elementoBorrado}')
print(f'La pila quedo asi:{pila}')

#Colas con listas
#Estructura de datos de tipo fifo(first input/ first ouput)
cola = ['Ariel', 'Osvaldo', 'Liliana','Pilar']
cola.append('Natalia')
cola.append('José')
print(cola)

#Sacamos  elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente {seRetira}')
print(cola)

seRetira=cola.pop(0)
print(f'Atendido el cliente {seRetira}')
print(cola)

seRetira=cola.pop(0)
print(f'Atendido el cliente {seRetira}')
print(cola)

seRetira=cola.pop(0)
print(f'Atendido el cliente {seRetira}')
print(cola)

seRetira=cola.pop(0)
print(f'Atendido el cliente {seRetira}')
print(cola)

# Seguimos mostrando como recorrer un diccionario con el ciclo for
for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')