
from collections import deque
import time

def simular_linea_espera(clientes):
    queue = deque(clientes)
    while queue:
        print("Atendiendo al cliente", queue.popleft())
        time.sleep(1)

def ingresar_clientes():
    clientes = []
    while True:
        cliente = input("Ingrese el nombre del cliente (o presione Enter para terminar): ")
        if not cliente:
            break
        clientes.append(cliente)
    return clientes

print("Bienvenido al banco, se les estará atendiendo según este orden")
clientes_en_espera = ingresar_clientes()
simular_linea_espera(clientes_en_espera)
print("Todos los clientes han sido atendidos")