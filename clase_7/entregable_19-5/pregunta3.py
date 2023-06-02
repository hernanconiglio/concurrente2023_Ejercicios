'''
Implemente un programa que tenga dos hilos A y B, los dos con acceso a una variable X (global) inicializa la variable en un valor entero aleatorio (entre 1 y 100). 
El hilo A decrementa X en 1 hasta llegar a 0 intercalando un retardo aleatorio entre 0 y 1 segundo entre cada decremento de X. 
El hilo B hará iteraciones cada un tiempo aleatorio entre 1 y 4 segundos, imprimiendo el valor de X en cada iteración hasta que X sea 0. 
Tanto A como B deberán imprimir mensajes al arrancar y al terminar, identificando al hilo. El hilo A deberá también indicar el valor inicial de X en el mensaje de arranque o final. 
Pregunta: Hay condiciones de carrera? Como las evitaría?
'''


import threading
import random
import time

x = random.randint(1,100)

def hilo_A():
    global x
    print(f"hilo_A iniciando identificado como {threading.current_thread().name} valor inicial de x: {x}")
    while x > 0:
        x -= 1
        print(f"hilo_A el valor de x es: {x}")
        time.sleep(random.randint(0,1))
    print(f"hilo_A terminando identificado como {threading.current_thread().name} valor final de x: {x}")

def hilo_B():
    global x
    print(f"hilo_B iniciando identificado como {threading.current_thread().name}")
    while x > 0:
        print(f"hilo_B el valor de x es: {x}")
        time.sleep(random.randint(1,4))
    print(f"hilo_B terminando identificado como {threading.current_thread().name}")

h1 = threading.Thread(target=hilo_A, name="Hilo A")
h2 = threading.Thread(target=hilo_B, name="Hilo B")

h1.start()
h2.start()
