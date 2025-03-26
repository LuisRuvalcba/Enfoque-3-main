# Ejemplo de encadenamiento hacia atrás (Backward Chaining) en Python
def backward_chaining(base_conocimiento, objetivo):
    def buscar_satisfaccion(hipotesis):
        for regla in base_conocimiento:
            antecedente, consecuente = regla

            if consecuente == hipotesis:
                if all(buscar_satisfaccion(premisa) for premisa in antecedente):
                    return True

        return hipotesis in hechos_iniciales

    hechos_iniciales = set()

    return buscar_satisfaccion(objetivo)

# Base de conocimiento: [([antecedentes], consecuente)]
base_conocimiento = [
    (["p", "q"], "r"),
    (["r"], "s"),
    (["s"], "t")
]

# Objetivo
objetivo = "t"

# Realizar encadenamiento hacia atrás
resultado = backward_chaining(base_conocimiento, objetivo)

# Imprimir resultado
if resultado:
    print("El objetivo se puede alcanzar.")
else:
    print("El objetivo no se puede alcanzar.")
