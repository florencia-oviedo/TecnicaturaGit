from mundo_pc.Monitor import Monitor
from mundo_pc.Raton import Raton
from mundo_pc.Teclado import Teclado


class Computadora:
    contador_computadoras = 0

    def __init__(self,nombre,monitor,teclado,raton):
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''
            {self._nombre}: {self._id_computadora}
            Monitor: {self._monitor}
            Teclado: {self._teclado}
            Ratón: {self._raton}
        '''

#Pruebas
if __name__ == '__main__':
    teclado1 = Teclado('HP','USB')
    monitor1 = Monitor('HP','15 Pulgadas')
    raton1 = Raton('HP','USB')

    computadora1 = Computadora('HP',monitor1,teclado1,raton1)
    print(computadora1)

    teclado2 = Teclado('Acer', 'Bluetooh')
    monitor2 = Monitor('Acer', '27 Pulgadas')
    raton2 = Raton('Acer', 'Bluetooh')

    computadora2 = Computadora('Acer', monitor2, teclado2, raton2)
    print(computadora2)
