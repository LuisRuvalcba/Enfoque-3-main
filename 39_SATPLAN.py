from pysat.solvers import Glucose3

class SATPlanLogistica:
    def __init__(self, acciones, precondiciones, efectos):
        self.acciones = acciones
        self.precondiciones = precondiciones
        self.efectos = efectos

    def planificar(self):
        solver = Glucose3()

        variables = {}
        actions = {}
        for i, action in enumerate(self.acciones):
            variables[action] = i + 1
            actions[i + 1] = action

        for accion in self.acciones:
            for precondicion in self.precondiciones[accion]:
                solver.add_clause([-variables[accion], variables[precondicion]])
            for efecto in self.efectos[accion]:
                solver.add_clause([-variables[accion], variables[efecto]])

        result = solver.solve()
        if result:
            model = solver.get_model()
            plan = [actions[literal] for literal in model if literal > 0]
            return plan
        else:
            return None

# Ejemplo de uso para un problema de logística
acciones = ["Cargar", "Descargar", "Mover"]
precondiciones = {
    "Cargar": ["Localizacion libre", "Carga disponible"],
    "Descargar": ["Carga en vehiculo"],
    "Mover": ["Vehiculo en localizacion A"]
}
efectos = {
    "Cargar": ["Carga en vehiculo"],
    "Descargar": ["Localizacion libre"],
    "Mover": ["Vehiculo en localizacion B"]
}

sat_planner_logistica = SATPlanLogistica(acciones, precondiciones, efectos)
plan = sat_planner_logistica.planificar()
print("Plan generado por SATPLAN para un problema de logistica:", plan)
