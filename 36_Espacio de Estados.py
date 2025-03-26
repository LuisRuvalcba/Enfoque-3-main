class TSPState:
    def __init__(self, cities):
        self.cities = cities

    def __eq__(self, other):
        return self.cities == other.cities

    def __hash__(self):
        return hash(tuple(self.cities))

    def generar_acciones(self):
        acciones = []
        for i in range(len(self.cities)):
            for j in range(i + 1, len(self.cities)):
                new_cities = self.cities[:]
                new_cities[i], new_cities[j] = new_cities[j], new_cities[i]  # Intercambio de ciudades
                acciones.append(TSPState(new_cities))
        return acciones

# Ejemplo de uso
estado_inicial = TSPState(["A", "B", "C", "D"])
acciones_posibles = estado_inicial.generar_acciones()

print("Acciones posibles desde el estado inicial:")
for accion in acciones_posibles:
    print(accion.cities)
