import threading
import time
import random
import logging

from ColaFIFOconcurrente import ColaFIFOconcurrente

cola = ColaFIFOconcurrente(0)

for i in range(10):
    cola.insertar(i)
    

print(cola.cantidad_elementos())
print(cola.primero(),cola.ultimo())
print(cola)
