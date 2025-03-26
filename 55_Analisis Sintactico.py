import nltk

# Definir gramática libre de contexto para expresiones aritméticas
gramatica_aritmetica = nltk.CFG.fromstring("""
    E -> E SUMA T | E RESTA T | T
    T -> T MULTIPLICACION F | T DIVISION F | F
    F -> NUMERO | PARENTESIS_IZQ E PARENTESIS_DER
    NUMERO -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
    SUMA -> '+'
    RESTA -> '-'
    MULTIPLICACION -> '*'
    DIVISION -> '/'
    PARENTESIS_IZQ -> '('
    PARENTESIS_DER -> ')'
""")

# Crear un analizador sintáctico basado en la gramática
analizador_sintactico = nltk.ChartParser(gramatica_aritmetica)

# Ejemplo de expresión aritmética a analizar
expresion_aritmetica = "3 * (4 + 5) - 6 / 2"

# Analizar sintácticamente la expresión aritmética
tokens = nltk.word_tokenize(expresion_aritmetica)
arboles = list(analizador_sintactico.parse(tokens))
for arbol in arboles:
    print("Arbol Sintactico:")
    print(arbol)
