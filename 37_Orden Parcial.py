class PartialOrderPlanner:
    def __init__(self, acciones, restricciones):
        self.acciones = acciones
        self.restricciones = restricciones

    def planificar(self):
        orden = []
        while self.acciones:
            for action in self.acciones:
                if all(precondition in orden for precondition in self.restricciones[action]):
                    orden.append(action)
                    self.acciones.remove(action)
                    break
            else:
                return None  # No se puede planificar debido a restricciones incumplidas
        return orden

# Ejemplo de uso
acciones = ["A", "B", "C", "D", "E"]
restricciones = {
    "B": ["A"],
    "C": ["A"],
    "D": ["B"],
    "E": ["C"]
}

planner = PartialOrderPlanner(acciones, restricciones)
plan = planner.planificar()
print("Plan de Orden Parcial:", plan)
