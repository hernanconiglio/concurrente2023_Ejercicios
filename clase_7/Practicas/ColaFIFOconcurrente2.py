"""
Clase ColaFIFOconcurrente(self, size=0)

Constructores:

    ColaFIFOconcurrente(self, size) instancia una cola de tamaño = size (infinita si size = 0)
    ColaFIFOconcurrente(self) instancia una cola infinita.

Metodos principales:

 insertar(), inserta un elemento si hay espacio en la cola y notifica la operación.
            Si la cola está llena se duerme hasta ser notificado. Una vez notificado
            verifica si hay espacio en la cola para insertar, sino se duerme nuevamente
            hasta la próxima notificación.

 extraer(), extrae un elemento disponible en la cola y notifica la operación.
            Si la cola esta vacia se duerme hasta ser notificado. Una vez notificado
            verifica si hay elementos en la cola para extrear, sino se duerme nuevamente
            hasta la próxima notificación.


"""
import threading

class ColaFIFOconcurrente:

    def __init__(self, size=0):
        self.elementos = []
        self.size = size
        self.condition = threading.Condition()

    def insertar(self, dato):
        self.condition.acquire()
        if self.size != 0:
            while len(self.elementos) == self.size:
                self.condition.wait()
        self.elementos.append(dato)
        self.condition.notify()
        self.condition.release()

    def extraer(self):
        self.condition.acquire()
        while len(self.elementos) == 0:
            self.condition.wait()
        elemento = self.elementos.pop(0)
        self.condition.notify()
        self.condition.release()
        return elemento

    def ultimo(self):
        return self.elementos[-1]

    def primero(self):
        return self.elementos[0]

    def cola_vacia(self):
        return len(self.elementos) == 0

    def cantidad_elementos(self):
        return len(self.elementos)


def main():
    cola = ColaFIFOconcurrente(0)
    cola2 = ColaFIFOconcurrente(5)

    # check if esta_vacia()

    print(f'cola.cola_vacia {cola.cola_vacia()}')
    print(f'cola2.cola_vacia {cola2.cola_vacia()}')

    for i in range (0,6):
        cola.insertar(i)
        cola2.insertar(i)

    print(f'cola.cola_vacia {cola.cola_vacia()}')
    print(f'cola.cantidad_elementos {cola.cantidad_elementos()}')

    print(f'cola2.cola_vacia {cola2.cola_vacia()}')
    print(f'cola2.cantidad_elementos {cola2.cantidad_elementos()}')


    print(cola.primero(),cola.ultimo())
    cola.extraer()
    print(cola.primero(),cola.ultimo())

    print(cola2.primero(),cola.ultimo())
    cola2.extraer()
    print(cola2.primero(),cola.ultimo())


    cola.extraer()
    cola.extraer()
    cola.extraer()
    cola.extraer()

    print(cola.cola_vacia())
    print(cola.cantidad_elementos())

if __name__ == '__main__':
    main()