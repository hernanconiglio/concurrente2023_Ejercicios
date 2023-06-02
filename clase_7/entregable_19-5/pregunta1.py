# Implemente un programa que ejecute 10 hilos que impriman un mensaje identificando 
# al hilo, luego esperen un tiempo aleatorio entre 1 y 5 segundos y luego impriman 
# un mensaje indicando que terminaron (identificando al hilo)

import threading
import time
import random

def hilo(id):
    print(f"Hilo {id} iniciando")
    time.sleep(random.randint(1,5))
    print(f"Hilo {id} terminando")

print("Hilos iniciados")

for i in range(10):
    t = threading.Thread(target=hilo, args=(i,),)
    t.start()
    t.join()


