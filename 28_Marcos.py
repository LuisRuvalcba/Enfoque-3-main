class MarcoAccion:
    def __init__(self, accion, agentes, objetos):
        self.accion = accion
        self.agentes = agentes
        self.objetos = objetos

# Crear instancias de marcos de acciones
marco1 = MarcoAccion("Comer", ["persona"], ["comida"])
marco2 = MarcoAccion("Correr", ["persona"], ["calle"])

# Mostrar información
print("Accion:", marco1.accion)
print("Agentes:", marco1.agentes)
print("Objetos:", marco1.objetos)

print("\nAccion:", marco2.accion)
print("Agentes:", marco2.agentes)
print("Objetos:", marco2.objetos)
