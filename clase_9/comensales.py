import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)
semaforoCocinero = threading.Semaphore(0)
semaforoComensal = threading.Semaphore(1)

class Cocinero(threading.Thread):
    def __init__(self):
        super().__init__()
        self.name = 'Cocinero'

    def run(self):
        global platosDisponibles
        while (True):
            semaforoCocinero.acquire()
            try:
                logging.info('Reponiendo los platos...')
                platosDisponibles = 3
            finally:
                semaforoComensal.release()
            #time.sleep(1)

class Comensal(threading.Thread):
    def __init__(self, numero):
        super().__init__()
        self.name = f'Comensal {numero}'

    def run(self):
        global platosDisponibles
        semaforoComensal.acquire()
        while platosDisponibles > 0:
            try:
                platosDisponibles -= 1
                logging.info(f'¡Qué rico! Quedan {platosDisponibles} platos')
            finally:
                semaforoComensal.release()
        semaforoCocinero.release()

platosDisponibles = 3

Cocinero().start()

for i in range(5):
    Comensal(i).start()