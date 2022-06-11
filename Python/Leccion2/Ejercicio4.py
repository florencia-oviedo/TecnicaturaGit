#Ejercicio4

"""edad= int(input("Digite su edad: "))

if edad>=0 and edad<10:
    print("La infancia es increible y bella")
elif edad>=10 and edad<20:
    print("Tienes muchos cambios,mucho que estudiar")
elif edad>=20 and edad<30:
    print("Amor y comienza el trabajo")
else:
    print("Error, digite nuevamente") """

#Profe
edad= int(input("Digite su edad: "))
mensaje= None
if 0<=edad<10:
    mensaje= "La infancia es increible y bella"
elif 10<=edad<20:
    mensaje= "Tienes muchos cambios,mucho que estudiar"
elif 20<=edad<30:
    mensaje= "Amor y comienza el trabajo"
else:
    mensaje= "Error, etapa de vida no reconocida"
print(f'Tu edad es: {edad}, {mensaje}')
