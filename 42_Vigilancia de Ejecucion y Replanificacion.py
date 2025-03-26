class TrafficControlSystem:
    def __init__(self, acciones, precondiciones, efectos):
        self.acciones = acciones
        self.precondiciones = precondiciones
        self.efectos = efectos

    def ejecutar_accion(self, accion, estado_actual):
        print(f"Ejecutando acción: {accion}")
        for efecto in self.efectos[accion]:
            estado_actual[efecto] = True

    def verificar_estado(self, estado_actual):
        for accion in self.acciones:
            if all(precondicion in estado_actual for precondicion in self.precondiciones[accion]):
                return accion
        return None

# Ejemplo de uso
acciones = ["Cambiar_semaforo", "Detener_trafico", "Iniciar_trafico"]
precondiciones = {
    "Cambiar_semaforo": ["Semaforo_en_rojo"],
    "Detener_trafico": ["Trafico_congestionado"],
    "Iniciar_trafico": ["Trafico_fluido"]
}
efectos = {
    "Cambiar_semaforo": ["Semaforo_en_verde"],
    "Detener_trafico": ["Trafico_detenido"],
    "Iniciar_trafico": ["Trafico_fluido"]
}

traffic_system = TrafficControlSystem(acciones, precondiciones, efectos)
estado_actual = {"Semaforo_en_rojo": True, "Trafico_congestionado": True}

# Ejecutar acciones hasta que se cumpla una condición deseada
while True:
    accion_a_ejecutar = traffic_system.verificar_estado(estado_actual)
    if accion_a_ejecutar is None:
        print("No hay acciones disponibles para el estado actual. Replanificando...")
        # Aquí se puede implementar la replanificación
        break
    else:
        traffic_system.ejecutar_accion(accion_a_ejecutar, estado_actual)
        print("Estado actual:", estado_actual)
