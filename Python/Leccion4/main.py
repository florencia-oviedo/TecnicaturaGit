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