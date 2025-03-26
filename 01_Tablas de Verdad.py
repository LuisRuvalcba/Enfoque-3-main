# Ejemplo de generación de tabla de verdad a partir de una expresión lógica en Python
import itertools

# Expresión lógica y variables
expresion = "(p or q) and (not p)"
variables = ["p", "q"]

# Generar todas las combinaciones posibles de valores para las variables
combinaciones = list(itertools.product([True, False], repeat=len(variables)))

# Evaluar la expresión lógica para cada combinación de valores
resultados = []
for combinacion in combinaciones:
    valores = dict(zip(variables, combinacion))
    resultado = eval(expresion, valores)
    resultados.append(resultado)

# Imprimir tabla de verdad
print("Tabla de Verdad:")
for i, combinacion in enumerate(combinaciones):
    print(f"{combinacion} -> {resultados[i]}")
