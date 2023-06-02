#hacer un código en python que implemente un programa que lance 2 hilas, A y B, ambos con acceso a una variable X (global) inicializada en cero.
#el hilo A incrementa X en 1 hasta llegar a una cantidad aleatoria entre 50 y 100 intercalando un retardo aleatorio entre 0 y 1 segundo entre cada incremento de X
#el hilo B hará un número aleatorio de iteraciones entre 10 y 100 cada un tiempo aleatorio entre 1 y 2 segundos, imprimiendo el valor de X en cada iteración.
#Tanto A como B deberán imprimir mensajes al arrancar al terminar, identificando al hilo.
#El hilo A deberá también indicar el valor final de X en el mensaje final

#¿Hay condiciones de carrera? Cómo las evitaría?


import threading
import time
import random

x = 0
lock_x = threading.Lock()


def hiloA():
    global x
    print(f"Arranca hiloA {threading.current_thread().name} y el valor de x es: "+str(x)+"\n")
    aleatorio = random.randint(50,100)
    print(f"El hilo A {threading.current_thread().name} incrementara x {aleatorio-1} veces")
    for i in range(aleatorio):
        with lock_x:
            x+=1
            print(f"Soy el hilo A {threading.current_thread().name} , en iteracion: {i} y el valor de x es: {x}")
        time.sleep(random.randint(0,1))
    print(f"Finaliza hiloA {threading.current_thread().name} y el valor de x es: "+str(x)+"\n")


def hiloB():
    global x
    print(f"Arranca hiloB {threading.current_thread().name} y el valor de x es: "+str(x)+"\n")
    for i in range(random.randint(10,100)):
        time.sleep(random.randint(1,4))
        with lock_x:
            print(f"Hilo B {threading.current_thread().name} el valor de x es: "+str(x)+"\n")
    print(f"Finaliza hiloB {threading.current_thread().name} y el valor de x es: "+str(x)+"\n")


hiloA1 = threading.Thread(target=hiloA)
hiloA2 = threading.Thread(target=hiloA)
hiloA3 = threading.Thread(target=hiloA)
hiloB1 = threading.Thread(target=hiloB)
hiloB2 = threading.Thread(target=hiloB)
hiloB3 = threading.Thread(target=hiloB)
hiloA1.start()
hiloA2.start()
hiloA3.start()
hiloB1.start()
hiloB2.start()
hiloB3.start()