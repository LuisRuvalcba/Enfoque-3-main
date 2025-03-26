from pyclips import Environment

# Crear un nuevo entorno CLIPS
env = Environment()

# Cargar la extensión Fuzzy CLIPS
env.load("fuzzy.clp")

# Resetear el entorno
env.reset()

# Definir los hechos de entrada (calidad y servicio) y salida (propina)
env.assert_string("(calidad 6.5)")
env.assert_string("(servicio 9.8)")
env.assert_string("(propina)")

# Ejecutar el sistema de inferencia
env.run()

# Obtener el valor de la propina resultante
propina = env.find_template("propina").slot_value("value").float_value

print("Propina:", propina)
