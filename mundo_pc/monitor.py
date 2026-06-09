class Monitor:
    contador_monitores = 0

    def __init__(self, marca, size):
        Monitor.contador_monitores += 1
        self.Id_monitor = Monitor.contador_monitores
        self.size = size
        self.marca = marca

    def __str__(self):
        return f'Id: {self.Id_monitor},Size: {self.size}, Marca: {self.marca}'

if __name__ == '__main__':
    monitor1 = Monitor('HP',15)
    monitor2 = Monitor('Phillips',20)
    monitor3 = Monitor('MSI', 32)
    print(f'{monitor1},\n{monitor2}')