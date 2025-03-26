# Ejemplo de unificación de predicados en lógica de primer orden

def unificar_predicados(predicado1, predicado2):
    # Verificar si los predicados tienen el mismo nombre y la misma cantidad de argumentos
    if predicado1[0] != predicado2[0] or len(predicado1) != len(predicado2):
        return False, {}

    # Unificar los argumentos de los predicados
    unificacion = {}
    for arg1, arg2 in zip(predicado1[1:], predicado2[1:]):
        unificacion_exitosa, sustitucion = unificar(arg1, arg2)
        if not unificacion_exitosa:
            return False, {}
        unificacion.update(sustitucion)

    return True, unificacion

# Ejemplo de unificación de predicados
predicado1 = ['P', 'x', 'y']
predicado2 = ['P', 'a', 'b']

resultado, sustitucion = unificar_predicados(predicado1, predicado2)
print("Unificacion exitosa:", resultado)
if resultado:
    print("Sustitucion:", sustitucion)
