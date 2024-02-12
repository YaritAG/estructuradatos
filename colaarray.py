import os
os.system('cls' if os.name == 'nt' else 'clear')

# Clase para una cola
class ColaArray:
    def __init__(self):
        self.elementos = []

    def encolar(self, item):
        self.elementos.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        else:
            raise IndexError("No se puede desencolar, no quedan elementos")

    def esta_vacia(self):
        return len(self.elementos) == 0

# Uso de la cola
cola = ColaArray()
cola.encolar('55')
cola.encolar('76')
cola.encolar('34')
cola.encolar('12')
cola.encolar('5')
cola.encolar('87')

# Mostrar elementos en la cola
print("Elementos en la cola:", cola.elementos)
print()

# Desencolar y mostrar el elemento desencolado
elemento_desencolado = cola.desencolar()
print("Elemento desencolado:", elemento_desencolado)
print()

# Mostrar la cola después de desencolar
print("Elementos en la cola después de desencolar:", cola.elementos)
print()

# Mostrar el elemento encolado
elemento_encolado = '67'
cola.encolar(elemento_encolado)
print("Elemento encolado:", elemento_encolado)
print()


#Mostrar los elementos al final del proceso
print("Elementos finales de la cola: ", cola.elementos)
