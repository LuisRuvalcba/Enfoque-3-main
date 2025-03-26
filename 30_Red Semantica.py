class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = []

    def agregar_conexion(self, nodo):
        self.conexiones.append(nodo)

# Crear nodos
juan = Nodo("Juan")
pedro = Nodo("Pedro")
luis = Nodo("Luis")
sofia = Nodo("Sofia")

# Establecer conexiones
juan.agregar_conexion(pedro)
pedro.agregar_conexion(sofia)
pedro.agregar_conexion(luis)

# Consultar conexiones
print("Conexiones de Pedro:")
for conexion in pedro.conexiones:
    print("- ", conexion.nombre)
