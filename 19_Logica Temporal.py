# Ejemplo de lógica temporal dinámica en Python

# Definir algunos estados del sistema
estados = ["s0", "s1", "s2"]

# Definir relaciones temporales entre estados
relaciones_temporales = {
    ("s0", "s1"): True,
    ("s1", "s2"): True
}

# Verificar si una relación temporal es válida en un momento dado
def relacion_temporal_valida(estado_actual, estado_futuro, relaciones_temporales):
    return (estado_actual, estado_futuro) in relaciones_temporales

# Ejemplo de uso de la lógica temporal dinámica
print("Ejemplo de logica temporal dinamica:")
print("s0 precede a s1?:", relacion_temporal_valida("s0", "s1", relaciones_temporales))
print("s1 precede a s2?:", relacion_temporal_valida("s1", "s2", relaciones_temporales))
print("s0 precede a s2?:", relacion_temporal_valida("s0", "s2", relaciones_temporales))
