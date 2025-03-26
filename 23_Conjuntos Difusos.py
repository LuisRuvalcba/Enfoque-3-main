# Definir variables de entrada y salida
temperatura = ctrl.Antecedent(np.arange(0, 101, 1), 'temperatura')
velocidad_ventilador = ctrl.Consequent(np.arange(0, 101, 1), 'velocidad_ventilador')

# Definir funciones de membresía para la temperatura
temperatura['fria'] = fuzz.trimf(temperatura.universe, [0, 0, 50])
temperatura['calida'] = fuzz.trimf(temperatura.universe, [0, 50, 100])
temperatura['caliente'] = fuzz.trimf(temperatura.universe, [50, 100, 100])

# Definir funciones de membresía para la velocidad del ventilador
velocidad_ventilador['baja'] = fuzz.trimf(velocidad_ventilador.universe, [0, 0, 50])
velocidad_ventilador['media'] = fuzz.trimf(velocidad_ventilador.universe, [0, 50, 100])
velocidad_ventilador['alta'] = fuzz.trimf(velocidad_ventilador.universe, [50, 100, 100])

# Definir reglas difusas
regla1 = ctrl.Rule(temperatura['fria'], velocidad_ventilador['baja'])
regla2 = ctrl.Rule(temperatura['calida'], velocidad_ventilador['media'])
regla3 = ctrl.Rule(temperatura['caliente'], velocidad_ventilador['alta'])

# Crear sistema de control difuso
sistema_control = ctrl.ControlSystem([regla1, regla2, regla3])
controlador = ctrl.ControlSystemSimulation(sistema_control)

# Simular control difuso con una temperatura de entrada
controlador.input['temperatura'] = 75
controlador.compute()

# Obtener la velocidad del ventilador de salida
velocidad = controlador.output['velocidad_ventilador']
print("Velocidad del ventilador:", velocidad)
