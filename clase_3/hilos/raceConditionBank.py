import threading
import time
import random

movimientos = [-10000, 50000]

operaciones = []

class cuentaBancaria():
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        self.lock = threading.Lock()

    def movimiento(self,monto):
        self.lock.acquire()
        try: 
            time.sleep(random.randint(1,5)/10)
            copia_local = self.saldo
            copia_local += monto
            time.sleep(random.randint(1,5)/10)
            self.saldo = copia_local
        finally:
            self.lock.release()

cuenta = cuentaBancaria(20000)

print("Saldo Inicial:", cuenta.saldo)

for i in range(2):
    operacion = threading.Thread(target=cuenta.movimiento, args = (movimientos[i],))
    operacion.start()
    operaciones.append(operacion)

for i in range(2):
    operaciones[i].join()

print("Saldo Final:",cuenta.saldo)