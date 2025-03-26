import random

# Definir una gramática simple para generar secuencias numéricas
gramatica_numeros = {
    'S': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'S S']
}

# Función para generar una secuencia numérica utilizando inducción gramatical
def generar_secuencia(gramatica, simbolo_inicial, iteraciones):
    secuencia = simbolo_inicial
    for _ in range(iteraciones):
        nueva_secuencia = ''
        for simbolo in secuencia.split():
            if simbolo in gramatica:
                nueva_secuencia += random.choice(gramatica[simbolo]) + ' '
            else:
                nueva_secuencia += simbolo + ' '
        secuencia = nueva_secuencia.strip()
    return secuencia

# Generar una secuencia numérica utilizando la gramática
secuencia_generada = generar_secuencia(gramatica_numeros, 'S', 5)
print("Secuencia numerica generada:", secuencia_generada)
