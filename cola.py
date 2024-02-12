import os
os.system('cls' if os.name == 'nt' else 'clear')

#Clase para una cola
class Cola:
    def __init__(self):
        self.elementos = []

    def encolar(self, item):
        self.elementos.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        else:
            raise IndexError("Desencolar de una cola vacía")

    def esta_vacia (self):
        return len(self.elementos) == 0

#Uso de la c0la
cola = Cola()
cola.encolar('Elemento1')
cola.encolar('Elemento2')
cola.encolar('Elemento3')
print("Elemento desencolado:", cola.desencolar())
