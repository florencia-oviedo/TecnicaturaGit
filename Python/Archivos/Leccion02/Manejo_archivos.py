#Declaramos una variable
try:
    archivo = open('prueba.txt', 'w', encoding= 'utf8')  # La w viene de la palabra write = escribir
    archivo.write('Programamos con diferentes tipos de archivos, ahora con txt.\n')
    archivo.write('Los acentos son importantes para nuestras palabras\n')
    archivo.write('Como por ejemplo: acción, ejecución y producción\n')
    archivo.write('las letras son:\nw write escribe,\nr read leer,\na append anexa,\nx crea una archivo')
    archivo.write('\nt esta para texto o text, \nb archivos binarios,\nw+ escribe y lee, \nr+ lee y escribe \n')
    archivo.write('Saludos a todos los alumnos de la tecnicatura\n')
    archivo.write('Con esto terminamos')
except Exception as e:
    print(e)
finally: #siempre se ejecuta
    archivo.close() #Con esto se debe cerrar el archivo 
#archivo.write('Todo quedo perfecto')

