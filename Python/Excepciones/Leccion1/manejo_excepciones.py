from NumerosIgualesException import NumerosIgualesException
resultado = None

try:
    a = int(input('Digite el primer número: '))
    b = int(input('Digite el segundo número: '))
    if a==b:
        raise NumerosIgualesException('Son números iguales')


    resultado = a / b #Modificamos y lo ponemos entre variables

except TypeError as e:
    print(f'TypeError-Ocurrió un error: {type(e)}')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError- Ocurrió un error: {type(e)}')
except Exception as e: #Clase con su respectivo objeto llamado e, es mejor usar la superclase Exception que poner especifico el tipo error
    print(f'Exception - Ocurrió un error: {type(e)}')
else:
    print('No arrojo ninguna excepcion')
finally: #Siempre se va a ejecutar
    print('ejecucion del bloque finally')

print(f'El resultado es: {resultado}')
print('seguimos...')