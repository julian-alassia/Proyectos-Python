from mundo_pc.dispositivo_entrada import DispositivoEntrada



class Teclado(DispositivoEntrada):
    contador_teclado = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclado += 1
        self.Id_teclado = Teclado.contador_teclado
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return (f'Id: {self.Id_teclado}, '
                f'Marca: {self._marca}'
                f',Tipo entrada: {self._tipo_entrada}')

if __name__ == '__main__':
    teclado1 = Teclado('LG', 'USB')
    teclado2 = Teclado('Ryzen','USB')
    teclado3 = Teclado('Kumara', 'USB')

    print(f'{teclado1},\n{teclado2}')