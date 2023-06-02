import threading
import time
import random

x = 0
lock_x = threading.Lock()
semaphore_b_active = threading.Semaphore(3)
semaphore_b_done = threading.Semaphore(0)


def hiloA():
    global x
    print(f"Arranca hiloA {threading.current_thread().name} y el valor de x es: "+str(x)+"\n")
    aleatorio = random.randint(20,60)
    print(f"El hilo A {threading.current_thread().name} incrementará x {aleatorio-1} veces")
    for i in range(aleatorio):
        with lock_x:
            x+=1
            print(f"Soy el hilo A {threading.current_thread().name} , en iteracion: {i} y el valor de x es: {x}")
        time.sleep(random.randint(0,1))
    print(f"Finaliza hiloA {threading.current_thread().name} y el valor de x es: "+str(x)+"\n")


def hiloB():
    global x
    print(f"Arranca hiloB {threading.current_thread().name} y el valor de x es: "+str(x)+"\n")
    semaphore_b_active.acquire()
    for i in range(random.randint(10,70)):
        time.sleep(random.randint(1,3))
        with lock_x:
            print(f"Hilo B {threading.current_thread().name} el valor de x es: "+str(x)+"\n")
        #time.sleep(random.randint(1,4))
    semaphore_b_done.release()
    semaphore_b_active.release()
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

semaphore_b_done.acquire()  # Esperamos a que todos los hilos B hayan terminado
print("Todos los hilos B han terminado.")
