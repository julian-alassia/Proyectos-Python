from mundo_pc.dispositivo_entrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contador_ratontes = 0

    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratontes += 1
        self.id_raton = Raton.contador_ratontes
        super().__init__(marca, tipo_entrada) # busca los atributos de la clase dispositivo_entrada.py

    def __str__(self):
        return (f'Id: {self.id_raton}, Marca: {self._marca}'
                f',Tipo entrada: {self._tipo_entrada}')

if __name__ == '__main__':
    raton1 = Raton('HP', 'USB')
    raton2 = Raton('LG', 'Bluetooth')
    raton3 = Raton('Ryzen', 'USB')
    print(f'{raton1},\n{raton2}')