# Ejemplo de encadenamiento hacia atrás en lógica de primer orden

# Base de conocimiento: Reglas de inferencia
base_conocimiento = {
    "Regla1": (("P", "Q"), ("R",)),
    "Regla2": (("R",), ("S",))
}

# Meta a probar
meta = ("S",)

# Función para realizar encadenamiento hacia atrás
def encadenamiento_hacia_atras(meta, base_conocimiento):
    if meta in base_conocimiento:
        return True
    for regla, (premisas, conclusion) in base_conocimiento.items():
        if meta[0] in conclusion:
            nuevas_metas = [premisa for premisa in premisas if premisa not in base_conocimiento]
            resultados_metas = [encadenamiento_hacia_atras((nueva_meta,), base_conocimiento) for nueva_meta in nuevas_metas]
            if all(resultados_metas):
                return True
    return False

# Realizar encadenamiento hacia atrás
resultado = encadenamiento_hacia_atras(meta, base_conocimiento)

# Imprimir el resultado de la prueba
if resultado:
    print("La meta se puede probar.")
else:
    print("La meta no se puede probar.")
