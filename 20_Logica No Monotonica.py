# Ejemplo de lógica defeasible en Python

# Definir algunas reglas defeasibles
reglas_defeasibles = [
    ("puede_volar(X)", ["es_un_pajaro(X)"]),
    ("no_puede_volar(X)", ["es_un_pingüino(X)"])
]

# Definir algunos hechos
hechos = ["es_un_pajaro(Tweety)", "es_un_pingüino(Pingu)"]

# Verificar si un hecho es verdadero de acuerdo con las reglas defeasibles
def verificar_hecho(hecho, reglas_defeasibles, hechos):
    for regla, condiciones in reglas_defeasibles:
        if hecho == regla:
            for condicion in condiciones:
                if condicion not in hechos:
                    return False
            return True
    return False

# Ejemplo de uso de la lógica defeasible
print("Ejemplo de lógica defeasible:")
print("Tweety puede volar?:", verificar_hecho("puede_volar(Tweety)", reglas_defeasibles, hechos))
print("Pingu puede volar?:", verificar_hecho("puede_volar(Pingu)", reglas_defeasibles, hechos))
