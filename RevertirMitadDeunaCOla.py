class Queue:
    def __init__(self): #Inicializa una lista vacia
        self.items = []

    def enqueue(self, item):  # Agrega un elemento a la cola
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0 # Devuelve True si la cola está vacía, False en caso contrario

    def size(self):
        return len(self.items)    # Devuelve el tamaño de la cola

def reversa(queue):
    stack = []
    size = queue.size()
    half_size = size // 2

    for _ in range(half_size):
        stack.append(queue.dequeue()) #agregan a la pila los primeros elementos de la cola, hasta la mitad.

    if size % 2 != 0:
        queue.enqueue(stack.pop())  # Manejo del elemento central si la longitud es impar

    while stack:
        queue.enqueue(stack.pop())

def ingreso_datos():
    queue = Queue()
    n = int(input("Ingrese la cantidad de elementos en la cola: "))
    for i in range(n):                                                  #Pide ingresar los datos para poderlos ingresar a la pila
        item = input(f"Ingrese el elemento {i + 1}: ")
        queue.enqueue(item)#Agrega los datos a una pila
    return queue

if __name__ == "__main__":
    queue = ingreso_datos() #Toma los datos ingresados
    print("Cola original:", queue.items)#Imprime pila original ingresada

    reversa(queue)
    print("Cola con la mitad de elementos revertidos:", queue.items) #imprime la cola revertida