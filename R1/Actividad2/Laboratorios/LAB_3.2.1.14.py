'''
    Autor: Christian Geovanni Arredondo Rangel
    Fecha: 23/Noviembre/2023
    Descrpcion: LAB 3.2.1.14
'''
# Definición de la clase base 'Stack'
class Stack:
    def __init__(self):
        # Inicializa la pila como una lista vacía
        self.__stk = []

    def push(self, val):
        # Agrega un elemento a la pila
        self.__stk.append(val)

    def pop(self):
        # Obtiene el último elemento de la pila, lo elimina y lo retorna
        val = self.__stk[-1]
        del self.__stk[-1]
        return val

# Definición de la clase derivada 'CountingStack' que hereda de 'Stack'
class CountingStack(Stack):
    def __init__(self):
        # Llama al constructor de la clase base 'Stack'
        super().__init__()
        # Inicializa un contador para contar operaciones de 'pop'
        self.__counter = 0

    def get_counter(self):
        # Retorna el valor actual del contador
        return self.__counter

    def pop(self):
        # Llama al método 'pop' de la clase base 'Stack'
        val = super().pop()
        # Incrementa el contador cada vez que se realiza un 'pop'
        self.__counter += 1
        # Retorna el valor obtenido al hacer 'pop'
        return val

# Creación de una instancia de la clase 'CountingStack'
stk = CountingStack()

# Bucle que realiza operaciones 'push' y 'pop' en la pila
for i in range(100):
    stk.push(i)
    stk.pop()

# Imprime el resultado: el número total de operaciones de 'pop'
print(stk.get_counter())
