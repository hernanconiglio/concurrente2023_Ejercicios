import threading
import time
import random

dato = 0
leido = False
contador = 0
def procesador():
    global dato
    global leido
    global contador
    while True:
        print(f'{threading.current_thread().name} Se proceso el dato : {dato}')
        contador += 1
        if leido == False:
            leido = True
        time.sleep(random.randint(1,5))


def generador():
    global dato
    global leido
    global contador
    while True:
        if leido == True and contador >= 2:
            leido = False
            dato = random.randint(0,100)
            contador = 0
            print(f'Se genero un nuevo dato = {dato}')
        time.sleep(random.randint(1,5))

print("Inicio programa principal")
print(f"Valor Inicial: {str(dato)}")

procesador_1=threading.Thread(target=procesador)
procesador_2=threading.Thread(target=procesador)
generador_1=threading.Thread(target=generador)

procesador_1.start()
procesador_2.start()
generador_1.start()

