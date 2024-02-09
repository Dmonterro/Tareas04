class ColaConPilas:
    def __init__(self):
        self.pila_entrada = []
        self.pila_salida = []

    def is_empty(self):
        return len(self.pila_entrada) == 0 and len(self.pila_salida) == 0

    def enqueue(self, ele):
        self.pila_entrada.append(ele)

    def dequeue(self):
        if self.is_empty():
            return None

        if len(self.pila_salida) == 0:
            while len(self.pila_entrada) > 0:
                self.pila_salida.append(self.pila_entrada.pop())

        return self.pila_salida.pop()

cola = ColaConPilas()

num_elementos = int(input("Ingrese el número de elementos en la cola: "))
for i in range(num_elementos):
    elemento = input(f"Ingrese el elemento {i + 1}: ")
    cola.enqueue(elemento)

print("Inicio del proceso de atención:")
elemento_atendido = cola.dequeue()

while elemento_atendido is not None:
    print("Atendiendo al cliente", elemento_atendido)
    elemento_atendido = cola.dequeue()

print("Todos los clientes han sido atendidos. Fin del proceso.")