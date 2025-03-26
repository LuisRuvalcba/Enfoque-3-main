# Ejemplo de lógica por defecto en Python

# Definir reglas y hechos
reglas = [
    ("puede_volar(X)", ["es_un_pajaro(X)"], True),  # Regla por defecto: Todos los pájaros pueden volar
    ("no_puede_volar(X)", ["es_un_pingüino(X)"], False)  # Regla por defecto: Los pingüinos no pueden volar
]

# Función para verificar si una afirmación es válida según las reglas y hechos dados
def verificar_afirmacion(afirmacion, reglas, hechos):
    for regla, condiciones, valor_defecto in reglas:
        if afirmacion == regla:
            for condicion in condiciones:
                if condicion not in hechos:
                    return valor_defecto  # Valor por defecto si las condiciones no se cumplen
            return True  # Si todas las condiciones se cumplen, la afirmación es verdadera
    return False  # Si no se encuentra una regla que coincida con la afirmación, es falsa

# Ejemplo de uso de la lógica por defecto
print("Ejemplo de lógica por defecto:")
print("Un pajaro puede volar?:", verificar_afirmacion("puede_volar(Tweety)", reglas, ["es_un_pajaro(Tweety)"]))
print("Un pingüino puede volar?:", verificar_afirmacion("puede_volar(Pingu)", reglas, ["es_un_pingüino(Pingu)"]))
