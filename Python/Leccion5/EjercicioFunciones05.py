# Ejercicio 5: Convertidor de temperaturas
# Realizar dos funciones para convertir de grados celsius
# a fahrenheit y viceversa.
# Investigar las fórmulas

# Hecha por mi
# def celsius_a_fahrenheit(celsius):
#     fahrenheit = celsius*1.8 + 32
#     return fahrenheit
# def fahrenheit_a_celsius(fahrenheit):
#     celsius = (fahrenheit -32)/1.8
#     return celsius
# bandera= True
# while bandera:
#     print(".:CONVERTIDOR DE TEMPERATURAS:.")
#     print("1. Convertir de Celsius a Fahrenheit")
#     print("2. Convertir de Fahrenheit a Celsius")
#     print("3. Salir")
#     print()
#     opcion= int(input("Digite una opción: "))
#     if opcion == 1:
#         celsius = float(input("Digite los grados Celsius: "))
#         print(f'La conversión de {celsius}°C a Fahrenheit es {celsius_a_fahrenheit(celsius)}°F')
#     elif opcion == 2:
#         fahrenheit = float(input("Digite los Fahrenheit: "))
#         print(f'La conversión de {fahrenheit}°F a Celsius es {fahrenheit_a_celsius(fahrenheit)}°C')
#     elif opcion == 3:
#         print("Gracias por utilizar el convertidor de temperaturas")
#         bandera = False
#     else:
#         print('Opción incorrecta, digite nuevamente')

# Version del profe

# Función que convierte de celsius a fahrenheit
def celsius_fahrenheit(celsius):
    return celsius*9/5 +32 # La presedencia:multiplicacion, division y suma

# Función que convierte de fahrenheit a celsius
def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9 # Respetar la presedencia utilizando paréntesis

celsius = float(input('Digite el valor de celsius: '))
resultado = celsius_fahrenheit(celsius)
print(f'{celsius}°C a F -> {resultado:.2f}')

fahrenheit = float(input('Digite el valor de fahrenheit: '))
resultado = fahrenheit_celsius(fahrenheit)
print(f'{fahrenheit} F a C -> {resultado:.2f}')