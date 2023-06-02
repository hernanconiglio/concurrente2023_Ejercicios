import threading
import time
import random

def miHilo(i):
    threading.current_thread().name="hilo"+str(i)
    print("Arranco: " + threading.current_thread().name+"\n")
    time.sleep(random.randint(1,5))
    print("Terminó: " + threading.current_thread().name+"\n")

def main():
    for i in range(random.randint(2,50)):
        hilo = threading.Thread(target=miHilo, args=(i,))

        hilo.start()
    time.sleep(4)

if __name__ == '__main__':
    main()