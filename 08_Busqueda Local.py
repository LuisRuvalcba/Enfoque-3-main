import random

# Función objetivo: número de cláusulas satisfechas
def funcion_objetivo(asignacion, clausulas):
    satisfaccion = 0
    for clausula in clausulas:
        if any(asignacion[literal] for literal in clausula):
            satisfaccion += 1
    return satisfaccion

# Algoritmo de ascenso de colinas
def hill_climbing(clausulas, asignacion_inicial):
    asignacion_actual = asignacion_inicial
    mejor_satisfaccion = funcion_objetivo(asignacion_actual, clausulas)

    while True:
        vecino = dict(asignacion_actual)
        # Generar vecino cambiando el valor de una variable aleatoria
        variable_aleatoria = random.choice(list(asignacion_actual.keys()))
        vecino[variable_aleatoria] = not vecino[variable_aleatoria]

        satisfaccion_vecino = funcion_objetivo(vecino, clausulas)
        if satisfaccion_vecino > mejor_satisfaccion:
            asignacion_actual = vecino
            mejor_satisfaccion = satisfaccion_vecino
        else:
            break

    return asignacion_actual

# Clausulas del problema
clausulas = [
    {"p", "q"},
    {"not p", "r"},
    {"not r", "q"}
]

# Asignación inicial
asignacion_inicial = {"p": False, "q": False, "r": False}

# Ejecutar algoritmo de ascenso de colinas
solucion = hill_climbing(clausulas, asignacion_inicial)
print("Asignacion optima encontrada:", solucion)
