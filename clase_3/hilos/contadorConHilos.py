import threading

THREADS = 2
MAX_COUNT = 1000000

counter = 0


def cuenta():
    global counter

    for i in range(int(MAX_COUNT/THREADS)):
        counter += 1


threadsLista = []

for i in range(THREADS):
    t = threading.Thread(target=cuenta)
    threadsLista.append(t)
    t.start()



print(f"Valor del contador: {counter}")
