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


def procesar(Dato):
    logging.info("Arranca "+ Dato)
    time.sleep(1)
    logging.info("Finalizo "+ Dato)


cron = Cronometro()

cron.iniciar()
procesar('A')
procesar('B')
procesar('C')
cron.finalizar()
cron.imprimir()

cron.iniciar()
thread1 = threading.Thread(target=procesar, args=('A'))
thread2 = threading.Thread(target=procesar, args=('B'))
thread3 = threading.Thread(target=procesar, args=('C'))

thread1.start()
thread2.start()
thread3.start()

cron.finalizar()
cron.imprimir()

cron.iniciar()
thread1 = threading.Thread(target=procesar, args=('A'))
thread2 = threading.Thread(target=procesar, args=('B'))
thread3 = threading.Thread(target=procesar, args=('C'))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

cron.finalizar()
cron.imprimir()
