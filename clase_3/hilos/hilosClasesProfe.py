import threading
import time

class UnHilo(threading.Thread):
    def __init__(self, i):
        super().__init__()
        self.i = i

    def run(self):
        self.name = "hilo_" + str(self.i)
        print("Arranco: " + self.name + "\n")
        time.sleep(random.randint(1, 5))
        print("Termino: " + self.name + "\n")
        print("Hilos activos: " + str(threading.active_count()) + "\n")
    
hilo = UnHilo(230)
hilo.start()
