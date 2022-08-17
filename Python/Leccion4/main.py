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
print(nombres)

