# Ejemplo de backtracking para resolver el problema de las N reinas en Python
def es_seguro(tablero, fila, columna):
    # Verificar si hay una reina en la misma columna
    for i in range(fila):
        if tablero[i] == columna:
            return False

    # Verificar diagonales
    for i in range(fila):
        if abs(i - fila) == abs(tablero[i] - columna):
            return False

    return True

def backtracking_n_reinas(tablero, fila):
    n = len(tablero)

    if fila >= n:
        return True

    for columna in range(n):
        if es_seguro(tablero, fila, columna):
            tablero[fila] = columna
            if backtracking_n_reinas(tablero, fila + 1):
                return True
            tablero[fila] = -1

    return False

# Número de reinas
N = 4

# Inicializar tablero
tablero = [-1] * N

# Resolver el problema de las N reinas utilizando backtracking
if backtracking_n_reinas(tablero, 0):
    print("Solucion encontrada:")
    for fila in range(N):
        print(tablero[fila])
else:
    print("No se encontro solucion.")
