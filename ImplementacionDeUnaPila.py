class Queue:
    def __init__(self):
        self.items = []     #la lista que utilizaremos como cola

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0) #Quita y devuelve el primer dato
        else:
            return None          # Nos da none si la cola no tiene contenido
        
    def front(self):
        if not self.is_empty():
            return self.items[0]  #Devuelve el primer elemento pero no lo quita
        else:
            return None
    
    def is_empty(self):
        return len(self.items) == 0 #Mira si esta vacia la cola
    
    def size(self):
        return len(self.items)
def proceso_atencion(fila):
    while not fila.is_empty():
        cliente = fila.dequeue()
        print("Atentiendo al cliente", cliente) #Aca se agrega el proceso al cliente
def get_queue_from_user():
    queue = Queue()
    num_clientes = int(input("Ingrese el número de clientes: "))
    for i in range(num_clientes):                                               #Aca se marca cuantos clientes queremos o necesitamos antender 
        nombre_cliente = input(f"Ingrese el nombre del cliente {i + 1}: ")
        queue.enqueue(nombre_cliente)
    return queue
if __name__ == "__main__":
    fila_de_clientes = get_queue_from_user()
    print("Inicio del proceso de atención: ")  
    proceso_atencion(fila_de_clientes)