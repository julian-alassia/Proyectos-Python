from mundo_pc.monitor import Monitor
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado


class Computadora:
    contar_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contar_computadoras += 1
        self.Id_computadoras =  Computadora.contar_computadoras
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

    def __str__(self):
        return f'''{self.nombre}: 
        {self.Id_computadoras}
        Monitor: {self.monitor}
        Teclado: {self.teclado}
        Raton: {self.raton}'''

if __name__ == '__main__':

    # Computadora nro 1
    teclado1 = Teclado('LG', 'USB')
    raton1 = Raton('HP', 'USB')
    monitor1 = Monitor('HP',15)

    computadora1 = Computadora('MSI',monitor1,teclado1,raton1)
    print(computadora1)



    # Computadora nro 2
    teclado2 = Teclado('Ryzen','USB')
    raton2 = Raton('LG', 'Bluetooth')
    monitor2 = Monitor('Phillips',20)

    computadora2 = Computadora('LG',monitor2,teclado2,raton2)
    print(computadora2)


    # Computadora nro 3
    teclado3 = Teclado('Kumara', 'USB')
    raton3 = Raton('Ryzen', 'USB')
    monitor3 = Monitor('MSI', 32)

    computadora3 = Computadora('MSI',monitor3,teclado3,raton3)
    print(computadora3)
