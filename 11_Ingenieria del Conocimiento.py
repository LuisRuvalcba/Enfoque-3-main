# Ejemplo de un sistema experto en diagnóstico médico utilizando lógica de primer orden

# Base de conocimiento: Relación entre síntomas y posibles enfermedades
base_conocimiento = {
    "Fiebre": ["Gripe", "Infeccion"],
    "Dolor de cabeza": ["Migraña", "Tension"],
    "Tos": ["Resfriado", "Bronquitis"]
}

# Función para diagnosticar enfermedades basadas en síntomas
def diagnosticar_enfermedad(sintomas):
    enfermedades_posibles = []
    for sintoma in sintomas:
        if sintoma in base_conocimiento:
            enfermedades_posibles.extend(base_conocimiento[sintoma])

    enfermedades_posibles = list(set(enfermedades_posibles))  # Eliminar duplicados

    return enfermedades_posibles

# Síntomas del paciente
sintomas_paciente = ["Fiebre", "Tos"]

# Diagnosticar enfermedades basadas en los síntomas del paciente
enfermedades_diagnosticadas = diagnosticar_enfermedad(sintomas_paciente)

# Imprimir las enfermedades diagnosticadas
if enfermedades_diagnosticadas:
    print("El paciente podria tener las siguientes enfermedades:")
    for enfermedad in enfermedades_diagnosticadas:
        print(enfermedad)
else:
    print("No se encontraron enfermedades que coincidan con los sintomas del paciente.")
