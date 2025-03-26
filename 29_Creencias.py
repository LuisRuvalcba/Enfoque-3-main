# Crear un diccionario de creencias
creencias = {
    "Juan": {"El sol es una estrella": True, "El agua es un metal": False},
    "María": {"Los gatos pueden volar": False, "Las manzanas son verdes": True}
}

# Mostrar las creencias de cada persona
for persona, creencia_persona in creencias.items():
    print("Creencias de", persona + ":")
    for creencia, verdad in creencia_persona.items():
        print("- ", creencia, "- Verdad?", verdad)
