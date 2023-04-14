from ManejoArchivos import ManejoArchivos
# Manejo de contexto with: sintaxis simplificada, abre y cierra el archivo
#with open('prueba.txt','r',encoding='utf8') as archivo:
    #print(archivo.read())
# no hace falta ni el try, ni el finally
# en el contexto de with lo que se ejecuta de manera automatica
#Utiliza diferentes metodos: __enter__ es el que abre el recurso
#__exit__ es el que cierra el recurso

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())