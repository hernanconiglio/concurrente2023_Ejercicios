import threading
import time

def tarea(lock, identificador):
    with lock:
        # executa tarea
        time.sleep(0.001)
        for i in range(5):
            
            # simula procesamiento
            print(f'Hilo {identificador} ejecutando')
            time.sleep(1)


lock = threading.Lock()
# crea hilos
hilos = [threading.Thread(target=tarea, args=(lock,i)) for i in range(2)]
# arranca hilos
for hilo in hilos:
    hilo.start()
# Espera a que terminen los hilos
for hilo in hilos:
    hilo.join()