class ADLPlanner:
    def __init__(self, estado_inicial, estado_final, acciones):
        self.estado_inicial = estado_inicial
        self.estado_final = estado_final
        self.acciones = acciones

    def planificar(self):
        plan = []
        estado_actual = self.estado_inicial.copy()

        while estado_actual != self.estado_final:
            accion_seleccionada = None

            for accion in self.acciones:
                precondiciones_satisfechas = all(estado_actual[p] for p in accion["precondiciones"])
                if precondiciones_satisfechas:
                    accion_seleccionada = accion
                    break

            if accion_seleccionada:
                plan.append(accion_seleccionada["nombre"])
                for efecto in accion_seleccionada["efectos"]:
                    estado_actual[efecto] = True
            else:
                return None  # No se puede alcanzar el estado final

        return plan

# Ejemplo de uso
estado_inicial = {"casa_limpia": False, "ropa_lavada": False}
estado_final = {"casa_limpia": True, "ropa_lavada": True}

acciones = [
    {"nombre": "Lavar ropa", "precondiciones": [], "efectos": ["ropa_lavada"]},
    {"nombre": "Limpiar casa", "precondiciones": [], "efectos": ["casa_limpia"]}
]

planner_adl = ADLPlanner(estado_inicial, estado_final, acciones)
plan = planner_adl.planificar()
print("Plan de accion:", plan)
