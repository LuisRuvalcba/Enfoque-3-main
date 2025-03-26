import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definir variables de entrada y salida
calidad = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad')
servicio = ctrl.Antecedent(np.arange(0, 11, 1), 'servicio')
propina = ctrl.Consequent(np.arange(0, 26, 1), 'propina')

# Definir funciones de membresía para la calidad, servicio y propina
calidad.automf(3)
servicio.automf(3)
propina['baja'] = fuzz.trimf(propina.universe, [0, 0, 13])
propina['media'] = fuzz.trimf(propina.universe, [0, 13, 25])
propina['alta'] = fuzz.trimf(propina.universe, [13, 25, 25])

# Definir reglas difusas
regla1 = ctrl.Rule(calidad['poor'] | servicio['poor'], propina['baja'])
regla2 = ctrl.Rule(servicio['average'], propina['media'])
regla3 = ctrl.Rule(servicio['good'] | calidad['good'], propina['alta'])

# Crear sistema de control difuso
sistema_control = ctrl.ControlSystem([regla1, regla2, regla3])
controlador = ctrl.ControlSystemSimulation(sistema_control)

# Simular sistema de inferencia con calidad y servicio de entrada
controlador.input['calidad'] = 6.5
controlador.input['servicio'] = 9.8
controlador.compute()

# Obtener la propina
propina_resultante = controlador.output['propina']
print("Propina:", propina_resultante)
