import re

# Definir gramática regular para números binarios
gramatica_binaria = re.compile(r'[01]+')

# Ejemplos de números binarios
numeros_binarios = ['1010', '110011', '0101010', '111']

# Validar números binarios utilizando la gramática
for numero in numeros_binarios:
    if gramatica_binaria.fullmatch(numero):
        print(numero, "es un numero binario valido.")
    else:
        print(numero, "no es un numero binario valido.")
