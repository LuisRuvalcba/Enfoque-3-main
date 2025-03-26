import nltk

# Definir la gramática causal definida
gramatica_causal = nltk.CFG.fromstring("""
    S -> Evento 'causo' Causa
    Evento -> 'accidente' | 'incendio' | 'explosion' | 'desastre'
    Causa -> 'por' 'falla_humana' | 'por' 'error_mecánico' | 'por' 'condiciones_climaticas' | 'por' 'negligencia'
""")

# Ejemplo de texto con relación causal
texto = "El incendio fue causado por negligencia."

# Crear un analizador sintáctico basado en la gramática causal
analizador_sintactico = nltk.ChartParser(gramatica_causal)

# Analizar sintácticamente el texto para identificar la relación causal
tokens = nltk.word_tokenize(texto)
for arbol in analizador_sintactico.parse(tokens):
    print("Relacion causal identificada:")
    print(arbol)
