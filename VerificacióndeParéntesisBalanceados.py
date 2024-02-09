class Stack:
                            #Se empieza a colocar las funciones
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

def paréntesis_balanceados(cadena):
    pila = Stack()
                         # Se empiezan a realizar iteraciones para agregar parentesis
    for char in cadena:
        if char in "({[":
            pila.push(char)
        elif char in ")}]":
            if pila.is_empty():
                return False  # Hay un cierre sin apertura correspondiente
            elif (char == ")" and pila.peek() == "(") or (char == "}" and pila.peek() == "{") or (char == "]" and pila.peek() == "["):
                pila.pop()
            else:
                return False  # Paréntesis desbalanceados

    return pila.is_empty()

#Aca de define cada cadena de prueba
cadena1 = input("Cadena1: ")
cadena2 = input("Cadena2: ")
cadena3 = input("Cadena3: ")
cadena4 = input("Cadena4: ")
cadena5 = input("Cadena5: ")
#Por medio de los print comprobamos si las cadenas estan balanceadas o no para mostrarlas
print("Cadena 1 balanceada:", paréntesis_balanceados(cadena1))
print("Cadena 2 balanceada:", paréntesis_balanceados(cadena2))
print("Cadena 3 balanceada:", paréntesis_balanceados(cadena3))
print("Cadena 4 balanceada:", paréntesis_balanceados(cadena4))
print("Cadena 5 balanceada:", paréntesis_balanceados(cadena5))