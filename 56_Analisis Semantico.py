import ast

# Función para realizar el análisis semántico y evaluar una expresión aritmética
def evaluar_expresion(expresion):
    try:
        # Utilizamos ast.literal_eval para evaluar la expresión aritmética de forma segura
        resultado = ast.literal_eval(expresion)
        return resultado
    except (SyntaxError, ValueError):
        return None

# Ejemplo de expresión aritmética a analizar semánticamente
expresion_aritmetica = "3 * (4 + 5) - 6 / 2"

# Realizar el análisis semántico y evaluar la expresión aritmética
resultado = evaluar_expresion(expresion_aritmetica)
if resultado is not None:
    print("El resultado de la expresion aritmetica es:", resultado)
else:
    print("La expresion aritmetica no es valida.")
