'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 23/Noviembre/2023
    Descrpcion: LAB 3.2.1.15
'''
class QueueError(Exception):  # Clase base para la nueva excepción relacionada con la cola.
    pass


class Queue:
    def __init__(self):
        self.__queue = []  # Inicializa una nueva cola vacía.

    def put(self, elem):
        self.__queue.insert(0, elem)  # Añade un elemento a la cola. Se inserta al principio para simular una cola.

    def get(self):
        if not self.__queue:
            raise QueueError("La cola está vacía")  # Si la cola está vacía, lanza una excepción QueueError.
        return self.__queue.pop()  # Obtiene y elimina el elemento del frente de la cola.

# Crear una instancia de la cola
que = Queue()

# Añadir elementos a la cola
que.put(1)
que.put("perro")
que.put(False)

try:
    # Intentar obtener elementos de la cola en un bucle
    for i in range(4):
        print(que.get())
except QueueError:
    # Manejar la excepción QueueError si ocurre al obtener elementos de la cola
    print("Error de Cola")

