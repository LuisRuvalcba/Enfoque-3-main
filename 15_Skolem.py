# Ejemplo de resolución Skolem con una cláusula universal en lógica de primer orden

# Supongamos la cláusula universal: ∀x P(x) → Q(x)
# Queremos demostrar ¬Q(a), donde 'a' es una constante introducida por Skolemización

# Definir la cláusula universal
clausula_universal = {'P(x)': True, 'Q(x)': True}

# Skolemización: Introducir una constante 'a'
constante_skolem = 'a'
clausula_skolemizada = {'¬Q(a)': True}

# Verificar si la negación de la cláusula skolemizada implica la negación de la premisa
def resolucion_skolem(clausula_universal, clausula_skolemizada):
    for literal in clausula_universal:
        if literal in clausula_skolemizada and clausula_universal[literal] != clausula_skolemizada[literal]:
            return True  # La resolución es exitosa
    return False  # No se puede inferir la negación de la conclusión

# Realizar la resolución Skolem
resultado = resolucion_skolem(clausula_universal, clausula_skolemizada)

# Imprimir el resultado
if resultado:
    print("La negacion de la conclusion ¬Q(a) se puede inferir utilizando resolucion Skolem.")
else:
    print("La negacion de la conclusion ¬Q(a) no se puede inferir utilizando resolucion Skolem.")
