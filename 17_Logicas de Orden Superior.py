# Ejemplo de lógica modal en Python utilizando la biblioteca pymonad

from pymonad import *

# Definir una mónada para la lógica modal
class Modal(Monad):
    def __init__(self, value, possible=True):
        self.value = value
        self.possible = possible

    def bind(self, func):
        if self.possible:
            return func(self.value)
        else:
            return Modal(None, False)

    def __repr__(self):
        return f"Modal({self.value}, {self.possible})"

# Definir algunas proposiciones
A = Modal("A", True)
B = Modal("B", False)

# Operaciones modales
def necesidad(proposicion):
    return Modal(proposicion.value, True)

def posibilidad(proposicion):
    return Modal(proposicion.value, proposicion.possible)

# Ejemplo de uso de la lógica modal
print("Ejemplo de logica modal:")
print("Necesidad de A:", necesidad(A))
print("Necesidad de B:", necesidad(B))
print("Posibilidad de A:", posibilidad(A))
print("Posibilidad de B:", posibilidad(B))
