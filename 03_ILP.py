# Ejemplo de inferencia Modus Tollens en Python
def modus_tollens(premisa, implicacion):
    if not implicacion:
        if not premisa:
            return True
    return False

# Definir premisa y implicación
premisa = False
implicacion = False

# Realizar inferencia Modus Tollens
resultado = modus_tollens(premisa, implicacion)

# Imprimir resultado
if resultado:
    print("La implicacion es verdadera segun Modus Tollens.")
else:
    print("La implicacion no se puede validar segun Modus Tollens.")
