import threading
import time
import random

class MiHilo(threading.Thread):
    def __init__(self, i):
        threading.Thread.__init__(self)
        self.i = i
        self.continuar = True

    def terminar(self):
        self.continuar = False

    def run(self):
        self.name = "hilo_" + str(self.i)
        print("Arranco: " + self.name + "\n")
        time.sleep(random.randint(1, 5))
        print("Termino: " + self.name + "\n")
        print("Hilos activos: " + str(threading.active_count()) + "\n")


def main():
    for i in range(random.randint(2, 15)):
        hilo = MiHilo(i)
        hilo.start()
    time.sleep(4)
    hilo.terminar()

if __name__ == '__main__':
    main()
