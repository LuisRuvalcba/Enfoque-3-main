# Ejemplo de un agente lógico para toma de decisiones utilizando lógica de primer orden

# Definir la base de conocimiento como una lista de cláusulas
base_conocimiento = [
    ("temperatura_alta", False),  # Hecho: No hay temperatura alta
    ("dolor_cabeza", True),        # Hecho: Hay dolor de cabeza
    ("tomar_medicamento", "ibuprofeno")  # Regla: Si hay dolor de cabeza, tomar ibuprofeno
]

# Definir un agente lógico para toma de decisiones
class AgenteLogico:
    def __init__(self, base_conocimiento):
        self.base_conocimiento = base_conocimiento

    def tomar_decision(self):
        # Verificar las reglas de la base de conocimiento para tomar una decisión
        for clausula, valor in self.base_conocimiento:
            if valor != False and valor != True:
                return valor  # Tomar la decisión indicada en la regla
        return "No se puede tomar una decision"  # No hay reglas aplicables

# Crear una instancia del agente lógico
agente = AgenteLogico(base_conocimiento)

# Tomar una decisión basada en la información disponible
decision = agente.tomar_decision()
print("Decision:", decision)
