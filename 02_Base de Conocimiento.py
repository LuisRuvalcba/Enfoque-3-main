# Ejemplo de sistema de recomendación basado en base de conocimiento en Python
class SistemaRecomendacion:
    def __init__(self):
        self.base_conocimiento = {}

    def agregar_item(self, item, atributos):
        self.base_conocimiento[item] = atributos

    def recomendar(self, usuario):
        recomendaciones = []
        for item, atributos in self.base_conocimiento.items():
            if all(usuario.get(atributo) == valor for atributo, valor in atributos.items()):
                recomendaciones.append(item)
        return recomendaciones

# Crear un sistema de recomendación
sistema = SistemaRecomendacion()

# Agregar items y sus atributos al sistema de recomendación
sistema.agregar_item("Libro1", {"Genero": "Ficcion", "Autor": "Autor1"})
sistema.agregar_item("Libro2", {"Genero": "Fantasía", "Autor": "Autor2"})
sistema.agregar_item("Libro3", {"Genero": "Ficcion", "Autor": "Autor3"})

# Definir perfil de usuario
perfil_usuario = {"Genero": "Ficcion"}

# Obtener recomendaciones para el usuario
recomendaciones = sistema.recomendar(perfil_usuario)

# Imprimir recomendaciones
print("Recomendaciones para el usuario:")
for recomendacion in recomendaciones:
    print(recomendacion)
