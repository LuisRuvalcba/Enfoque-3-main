import re

# Definir patrones para tokens de la expresión aritmética
patrones = [
    ('NUMERO', r'\d+'),
    ('SUMA', r'\+'),
    ('RESTA', r'\-'),
    ('MULTIPLICACION', r'\*'),
    ('DIVISION', r'\/'),
    ('PARENTESIS_IZQ', r'\('),
    ('PARENTESIS_DER', r'\)')
]

# Función para analizar léxicamente una expresión aritmética
def analizar_expresion(expresion, patrones):
    tokens = []
    while expresion:
        encontrado = False
        for token, patron in patrones:
            match = re.match(patron, expresion)
            if match:
                valor = match.group(0)
                tokens.append((token, valor))
                expresion = expresion[len(valor):].strip()
                encontrado = True
                break
        if not encontrado:
            raise ValueError('Expresion no valida: ' + expresion)
    return tokens

# Ejemplo de expresión aritmética a analizar
expresion_aritmetica = "3 + (4 * 5) - 6 / 2"

# Analizar léxicamente la expresión aritmética
tokens = analizar_expresion(expresion_aritmetica, patrones)
print("Tokens de la expresion aritmetica:")
for token in tokens:
    print(token)
