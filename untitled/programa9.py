import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

class Cronometro:
    def iniciar(self):
        self.inicio = time.perf_counter()

    def finalizar(self):
        self.fin = time.perf_counter()

    def imprimir(self):
        logging.info(f'Pasaron {self.fin - self.inicio} segundos')

class Procesador(threading.Thread):
    def __init__(self, Dato):
        super().__init__()
        self.Dato = Dato
    def run(self):
        logging.info("Arranca "+ self.Dato)
        time.sleep(1)
        logging.info("Finalizo "+ self.Dato)


cron = Cronometro()
cron.iniciar()
procesadorA = Procesador('A')
procesadorB = Procesador('B')
procesadorC = Procesador('C')

procesadorA.start()
procesadorA.join()

procesadorB.start()
procesadorB.join()

procesadorC.start()
procesadorC.join()




cron.finalizar()
cron.imprimir()