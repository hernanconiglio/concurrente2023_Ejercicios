# Implemente un programa que pueda lanzar 10 hilos tipo A y 2 hilos tipo B, todos con acceso a una variable global X incializada en 0. 
# Los Hilos A incrementan el valor de X hasta 1000000. 
# Los Hilos B imprime el valor de X cada 2 segundos. 
# Colocar líenas de comentario en el código, identificando las zonas críticas y los objetos utilizados para evitar condiciones de carrera.

import threading
import random
import time

x = 0
lock = threading.Lock()

def hilo_A():
    global x
    print(f"hilo_A iniciando identificado como {threading.current_thread().name} valor inicial de x: {x}")
    while x < 1000000:
        lock.acquire() #acá se bloquea el acceso a la variable x
        if (x < 1000000): 
            x += 1
        lock.release() # acá se libera el acceso a la variable x
    print(f"hilo_A terminando identificado como {threading.current_thread().name} valor final de x: {x}")

def hilo_B():
    global x
    print(f"hilo_B iniciando identificado como {threading.current_thread().name}")
    while x < 1000000:
        lock.acquire() # acá se bloquea el acceso a la variable x para poder leerla
        print(f"hilo_B identificado como {threading.current_thread().name} el valor de x es: {x}")
        lock.release() # acá se libera el acceso a la variable x
        time.sleep(2)
    print(f"hilo_B terminando identificado como {threading.current_thread().name}")

for i in range(10):
    hA = threading.Thread(target=hilo_A)
    hA.start()

for i in range(2):
    hB = threading.Thread(target=hilo_B)
    hB.start()
