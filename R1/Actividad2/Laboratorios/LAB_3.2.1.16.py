'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 23/Noviembre/2023
    Descrpcion: LAB 3.2.1.16
'''
class QueueError(Exception):
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

    def isempty(self):
        return not bool(self.__queue)  # Verifica si la cola está vacía

class SuperQueue(Queue):
    # Agrega funcionalidad adicional a SuperQueue si es necesario
    def isempty(self):
        return not bool(self._Queue__queue)  # Accede al atributo __queue de la clase base usando el nombre de la clase base

# Crear una instancia de la SuperQueue
que = SuperQueue()
que.put(1)
que.put("perro")
que.put(False)
for i in range(4):
    if not que.isempty():  # Ahora estás llamando al método 'isempty' de la clase derivada 'SuperQueue'
        print(que.get())
    else:
        print("Cola vacía")
