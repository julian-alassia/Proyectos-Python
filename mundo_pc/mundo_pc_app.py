from mundo_pc.computadora import Computadora
from mundo_pc.teclado import Teclado
from mundo_pc.raton import Raton
from mundo_pc.monitor import Monitor
from mundo_pc.orden import Orden



print('=========== Mundo PC =============')
# Pagina principal


teclado1 = Teclado('LG', 'USB')
raton1 = Raton('HP', 'USB')
monitor1 = Monitor('HP', 15)

computadora1 = Computadora('MSI', monitor1, teclado1, raton1)

teclado2 = Teclado('Ryzen', 'USB')
raton2 = Raton('LG', 'Bluetooth')
monitor2 = Monitor('Phillips', 20)

computadora2 = Computadora('LG', monitor2, teclado2, raton2)

# Agrega lista en orden.py
primera_orden = [computadora1, computadora2]
# Se agregan en la orden 1
orden1 = Orden(primera_orden)
print(orden1)

teclado3 = Teclado('Kumara', 'USB')
raton3 = Raton('Ryzen', 'USB')
monitor3 = Monitor('MSI', 32)

computadora3 = Computadora('MSI',monitor2,teclado2,raton2)

segunda_orden = [computadora3]
orden2 = Orden(segunda_orden)
print(orden2)

