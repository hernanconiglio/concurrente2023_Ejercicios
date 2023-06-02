# Modifique el programa del ejercicio pregunta1 de modo que pueda medir e imprimir el tiempo total que tomo ejecutarse cada hilo (en milisengundos)

import threading
import time
import random
import datetime

def hilo(id):
    print(f"Hilo {id} iniciando")
    start = time.time()
    time.sleep(random.randint(1,5))
    end = time.time()
    #print(f"Hilo {id} terminando, tiempo: {end-start}")
    tiempo_transcurrido = datetime.timedelta(seconds=end-start)
    print(f"Hilo {id} terminando, tiempo: {tiempo_transcurrido}")
        


for i in range(10):
    t = threading.Thread(target=hilo, args=(i,))
    t.start()

print("Hilos iniciados")
