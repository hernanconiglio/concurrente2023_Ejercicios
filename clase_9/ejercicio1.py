'''
Generadores - Medidor
En este tipo de problemas hay varios hilos Generadores qué van incrementando aleatoriamente un recurso en común y varios hilos Medidores que pueden tomar muestras temporales del valor del recurso común y  realizar operaciones .
Por ejemplo, los hilos generadores podrían simular un conjunto de generadores eléctricos y el recurso común ser una variable que cuente la energía total generada por el conjunto. Los medidores pueden calcular la potencia (energía/tiempo) generada por el conjunto de generadores, calculando la diferencia del valor de la variable al comienzo y al final de un lapso de tiempo determinado.

Ejercicio:
Implemente un programa que ejecute dos hilos llamados generador y 10 hilos llamados medidor que acceden todos a una variable global energia.

Generador:
Los hilos generador debe ejecutar un loop infinito en el que incrementan en 1 la variable energia y esperan un retardo aleatorio entre 0.01 (1/100) y y 0.02 (2/100) antes de la siguiente iteración.
Ejemplo del loop Generador (operación básica, no incluye el código necesario para funcionar tal como lo piden los requerimientos):

while True:

    energia += 1

    time.sleep(random.randint(1,2)/100)

Nota: El uso de este ejemplo en la solución es opcional, puede modificarlo o incluso utilizar uno completamente diferente si lo consideran necesario.

Medidor:
Los hilos medidor deben deben ejecutar un loop infinito en el que se calcule en cuanto se incrementó la variable energía en el lapso de 1 segundo.  
Para esto debe tomar un valor inicial de la variable energía (valor0), esperar 1 segundo y luego tomar el valor final (valor1) y calcular la diferencia. Nota: debe asegurarse que los generadores continúen incrementando la variable energia entre las tomas del valor0 y valor1.
Deberá luego generar un mensaje indicando la diferencia como valor de potencia. Por ejemplo: Energía generada = 58kw, 
y esperar luego un retardo fijo de 2 segundos antes de volver a realizar una nueva medición.
No debe haber más de dos medidores tomando mediciones en forma simultánea.

Ejemplo del loop Generador (operación básica, no incluye el código necesario para funcionar tal como lo piden los requerimientos):

while True:
    valor0 = energia
    time.sleep(1)
    valor1 = energía
    logging.info(f'Potencia generada = {valor1 - valor0}kw')
    time.sleep(2)

Nota: El uso de este ejemplo en la solución es opcional, puede modificarlo o incluso utilizar uno completamente diferente si lo consideran necesario.

El programa debe funcionar para cualquier número de generadores y medidores

Debe colocarse el código suficiente para evitar condiciones de carrera, asegurar la condición de sincronización y evitar deadlocks.
Ejemplo de Salida:
17:33:31.267 [Thread-12] - Potencia generada = 60kw
17:33:32.270 [Thread-10] - Potencia generada = 54kw
17:33:32.271 [Thread-17] - Potencia generada = 54kw
17:33:33.275 [Thread-9] - Potencia generada = 62kw
17:33:33.275 [Thread-14] - Potencia generada = 62kw

'''
import logging
import random
import threading
import time

logging.basicConfig(
    format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s',
    datefmt='%H:%M:%S',
    level=logging.INFO
)

energia = 0

#Se agrega lock para evitar condiciones de carrera
lockG = threading.Lock()
lockL = threading.Lock()

class Generador(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        nombre = threading.current_thread().name
        global energia
        logging.info("El Generador "+str(nombre)+" ha arrancado, el valor de la energía al inicio es: "+str(energia))
        while True:
            lockG.acquire() #Se agrega lock para evitar condiciones de carrera
            try:
                energia += 1
                #logging.info("El "+str(nombre) +" incrementó la energía, ahora es de : " + str(energia))
            finally:
                lockG.release()
            time.sleep(random.randint(1,2)/100)
        

class Medidor(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        nombre = threading.current_thread().name
        logging.info("El Medidor "+str(nombre)+" ha arrancado.")
        global energia
        while True:
            lockG.acquire() #Se agrega lock para evitar condiciones de carrera
            try:
                inicial = energia
                #logging.info(f'Medidor '+str(nombre)+' valor inicial energia : ' +str(energia))
            finally:
                lockG.release()
            time.sleep(1)
            lockG.acquire() #Se agrega lock para evitar condiciones de carrera
            try:
                logging.info(f'Medidor con valor final energia : ' +str(energia)+'. Energia Generada: '+str(energia-inicial))
            finally:
                lockG.release()
            time.sleep(2)
                


def generarHilosMedidor(cantidad):
    for i in range(cantidad):
        hilo = Medidor()
        hilo.start()

def generarHilosGenerador(cantidad):
    for i in range(cantidad):
        hilo = Generador()
        hilo.start()

def main():
    generarHilosMedidor(10)
    generarHilosGenerador(2)

main()
