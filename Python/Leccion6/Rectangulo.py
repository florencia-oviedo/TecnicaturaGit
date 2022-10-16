class Rectangulo:
    """Crear una clase llamada Rectangulo debe tener 2 atributos: altura y base
       el nombre del  método sera calcular_area utilizando la fórmula:
       area =  base * altura. Pero la base y la altura deben ser ingresadas por
       el usuario y los objetos deben ser tres.
    """

    # Creamos los atributos
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    # Creamos el método calcular area
    def calcular_area(self):
        return self.base * self.altura


base = int(input("Digite el número para la base del rectángulo: "))
altura = int(input("Digite el número para la altura del rectángulo: "))

rectangulo1 = Rectangulo(base, altura)
print(f'El área del rectángulo es: {rectangulo1.calcular_area()}')


