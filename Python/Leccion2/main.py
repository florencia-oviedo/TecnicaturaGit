# En esta clase 6 veremos la sentencia if/else
"""condicion = True
if condicion == True: #comprueba si nuestra variable esta vacia o no, si tiene algun dato(10) y ""(vacia)
    print("Condición Verdadera") #automaticamente se genera un tabulador / espacios (identacion)
elif condicion == False:
    print("condicion Falsa")
else:
    print("condición sin especificar") """
#Debug es un paso a paso, depuracion muestra todo el codigo y lo q este mal se puede arreglar
#step over sigue el paso el puntito rojo siempre en la variable declarada
"""
num = int(input("Digite un numero en el rango de 1 a 3: "))
numTexto = ""
if num == 1:
    numTexto = "Numero uno"
elif num == 2:
    numTexto = "numero dos"
elif num == 3:
    numTexto = "numero tres"
else:
    numTexto= "Haz ingresado un numero fuera de rango"
print( f"El numero ingresado es: {num} - {numTexto}")

#Siempre respetar la identacion(espacios) OJO en el siguiente codigo print sin espacio 
"""
#condicion = True
#if condicion:
#    print("condicion verdadera")
#else:
#    print("condicion falsa")

#CODIGO SIMPLIFICADO PARA CODIGOS CORTOS- OPERADOR TERNARIO
condicion= False
print("condicion verdadera") if condicion else print("condicion falsa")