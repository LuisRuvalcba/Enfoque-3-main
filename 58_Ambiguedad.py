import nltk

# Definir gramática libre de contexto ambigua para expresiones aritméticas
gramatica_ambigua = nltk.CFG.fromstring("""
    E -> E SUMA E | E RESTA E | E MULTIPLICACION E | E DIVISION E | NUMERO
    SUMA -> '+'
    RESTA -> '-'
    MULTIPLICACION -> '*'
    DIVISION -> '/'
    NUMERO -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
""")

# Crear un analizador sintáctico basado en la gramática ambigua
analizador_sintactico = nltk.ChartParser(gramatica_ambigua)

# Ejemplo de expresión aritmética ambigua
expresion_ambigua = "2 + 3 * 4"

# Analizar sintácticamente la expresión aritmética ambigua
tokens = nltk.word_tokenize(expresion_ambigua)
arboles = list(analizador_sintactico.parse(tokens))
print("Arboles de analisis sintactico:")
for arbol in arboles:
    print(arbol)
