class ConditionalPlanning:
    def __init__(self, conditions, actions):
        self.conditions = conditions
        self.actions = actions

    def planificar(self, estado_actual):
        plan = []
        for condition, action in zip(self.conditions, self.actions):
            if condition(estado_actual):
                plan.append(action)
        return plan

# Ejemplo de uso
def condition1(estado):
    return estado["temperatura"] > 25

def action1():
    return "Encender el aire acondicionado"

def condition2(estado):
    return estado["nivel_humedad"] > 80

def action2():
    return "Encender el deshumidificador"

conditions = [condition1, condition2]
actions = [action1, action2]

planner = ConditionalPlanning(conditions, actions)
estado_actual = {"temperatura": 30, "nivel_humedad": 85}
plan = planner.planificar(estado_actual)
print("Plan de accion:", plan)
