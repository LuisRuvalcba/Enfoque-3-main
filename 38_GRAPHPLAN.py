class GraphPlanLogistica:
    def __init__(self, acciones, precondiciones, efectos):
        self.acciones = acciones
        self.precondiciones = precondiciones
        self.efectos = efectos

    def planificar(self, nivel):
        if nivel == 0:
            return [[]]

        plan_nivel_anterior = self.planificar(nivel - 1)
        nuevo_nivel = []

        for accion in self.acciones:
            for plan in plan_nivel_anterior:
                if all(precondicion in plan for precondicion in self.precondiciones[accion]):
                    nuevo_plan = plan + [accion]
                    if all(efecto in nuevo_plan for efecto in self.efectos[accion]):
                        nuevo_nivel.append(nuevo_plan)

        return nuevo_nivel

# Ejemplo de uso para un problema de logística
acciones = ["Cargar", "Descargar", "Mover"]
precondiciones = {
    "Cargar": ["Localizacion libre", "Carga disponible"],
    "Descargar": ["Carga en vehículo"],
    "Mover": ["Vehiculo en localización A"]
}
efectos = {
    "Cargar": ["Carga en vehiculo"],
    "Descargar": ["Localización libre"],
    "Mover": ["Vehiculo en localizacion B"]
}

graph_planner_logistica = GraphPlanLogistica(acciones, precondiciones, efectos)
plan = graph_planner_logistica.planificar(3)
print("Plan generado por GRAPHPLAN para un problema de logistica:", plan)
