class Orden:
    contador_ordenes = 0

    def __init__(self, computadoras):
        Orden.contador_ordenes += 1
        self.Id_ordenes = Orden.contador_ordenes
        self.computadoras = computadoras

    def agregar_computadora(self, computadoras):
        self.computadoras.append(computadoras)

    def __str__(self):
        computadoras_str = ''
        for computadora in self.computadoras:
            computadoras_str += '\n' + computadora.__str__()
        return f'''Orden {self.Id_ordenes}
        Computadoras: {computadoras_str}'''
