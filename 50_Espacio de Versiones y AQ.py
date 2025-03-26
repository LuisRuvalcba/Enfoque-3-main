# Definir función para determinar si un correo es spam o no spam
def es_spam(oferta, gratis):
    if oferta == 1 and gratis == 1:
        return "spam"
    else:
        return "no spam"

# Ejemplos de correos electrónicos y sus etiquetas
correos_electronicos = [
    {"oferta": 1, "gratis": 0},  # Correo 1: oferta pero no gratis
    {"oferta": 0, "gratis": 1},  # Correo 2: gratis pero no oferta
    {"oferta": 1, "gratis": 1},  # Correo 3: oferta y gratis
]

# Etiquetas correspondientes a los correos electrónicos
etiquetas = ["spam", "no spam", "spam"]

# Construir espacio de versiones
versiones = set()
for correo in correos_electronicos:
    versiones.add(es_spam(correo["oferta"], correo["gratis"]))

print("Espacio de Versiones:", versiones)

# Definir función para determinar si un estudiante aprobará el examen
def aprobara_examen(horas_estudio, horas_sueno, cafe):
    if horas_estudio >= 5 and horas_sueno >= 7 and cafe <= 2:
        return "aprobado"
    else:
        return "reprobado"

# Ejemplos de estudiantes y sus etiquetas
estudiantes = [
    {"horas_estudio": 6, "horas_sueno": 8, "cafe": 1},  # Estudiante 1: aprobado
    {"horas_estudio": 4, "horas_sueno": 6, "cafe": 3},  # Estudiante 2: reprobado
    {"horas_estudio": 7, "horas_sueno": 9, "cafe": 2},  # Estudiante 3: aprobado
]

# Etiquetas correspondientes a los estudiantes
etiquetas = ["aprobado", "reprobado", "aprobado"]

# Construir árbol de decisión con AQ
arbol_decision = {}
for estudiante, etiqueta in zip(estudiantes, etiquetas):
    pregunta = tuple(estudiante.values())
    if etiqueta not in arbol_decision:
        arbol_decision[etiqueta] = pregunta

print("Arbol de Decision con AQ:", arbol_decision)
