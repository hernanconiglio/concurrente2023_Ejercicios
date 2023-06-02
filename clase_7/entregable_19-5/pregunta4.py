'''
Modificar el programa anterior para que se ejecuten 2 hilos A y un hilo B. Identificar (con comentarios) 
las zonas críticas y colocar los objetos necesarios para evitar condiciones de carrera.

ESTA SOLUCIÓN NO ES CORRECTA
'''

import threading
import random
import time

x = random.randint(1,100)
lock = threading.Lock()

def hilo_A():
    global x
    print(f"hilo_A iniciando identificado como {threading.current_thread().name} valor inicial de x: {x}")
    while x > 0:
        lock.acquire() #acá se bloquea el acceso a la variable x
        x -= 1
        print(f"hilo_A identificado como {threading.current_thread().name} el valor actualizado de x es: {x}")
        lock.release() # acá se libera el acceso a la variable x
        time.sleep(random.randint(0,1))
    print(f"hilo_A terminando identificado como {threading.current_thread().name} valor final de x: {x}")

def hilo_B():
    global x
    print(f"hilo_B iniciando identificado como {threading.current_thread().name}")
    while x > 0:
        lock.acquire()
        print(f"hilo_B identificado como {threading.current_thread().name} el valor de x es: {x}")
        lock.release()
        time.sleep(random.randint(1,4))
    print(f"hilo_B terminando identificado como {threading.current_thread().name}")

hA1 = threading.Thread(target=hilo_A)
hA2 = threading.Thread(target=hilo_A)
hB1 = threading.Thread(target=hilo_B)

hA1.start()
hA2.start()
hB1.start()


