# Ejemplo de sistema de recomendación de películas utilizando lógica difusa en Python

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definir las variables de entrada y salida difusas
calidad = ctrl.Antecedent(np.arange(0, 11, 1), 'calidad')
precio = ctrl.Antecedent(np.arange(0, 11, 1), 'precio')
recomendacion = ctrl.Consequent(np.arange(0, 101, 1), 'recomendacion')

# Definir las funciones de membresía para la calidad
calidad.automf(3)

# Definir las funciones de membresía para el precio
precio.automf(3)

# Definir las funciones de membresía para la recomendación
recomendacion['baja'] = fuzz.trimf(recomendacion.universe, [0, 0, 50])
recomendacion['media'] = fuzz.trimf(recomendacion.universe, [0, 50, 100])
recomendacion['alta'] = fuzz.trimf(recomendacion.universe, [50, 100, 100])

# Definir las reglas difusas
regla1 = ctrl.Rule(quality['poor'] | price['high'], recomendacion['baja'])
regla2 = ctrl.Rule(quality['average'], recomendacion['media'])
regla3 = ctrl.Rule(quality['good'] | price['low'], recomendacion['alta'])

# Crear el sistema de control difuso
sistema_control = ctrl.ControlSystem([regla1, regla2, regla3])
controlador = ctrl.ControlSystemSimulation(sistema_control)

# Simular el sistema de recomendación con una calidad y precio de entrada
controlador.input['calidad'] = 6
controlador.input['precio'] = 3
controlador.compute()

# Obtener la recomendación
recomendacion = controlador.output['recomendacion']
print("Recomendacion:", recomendacion)
