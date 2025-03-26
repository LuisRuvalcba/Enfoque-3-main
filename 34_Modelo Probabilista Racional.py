class SistemaRecomendacion:
    def __init__(self):
        self.probabilidad_gusto = 0.5

    def train(self, usuarios):
        gusto_total = sum(usuario["gusto"] for usuario in usuarios)
        total_usuarios = len(usuarios)
        self.probabilidad_gusto = gusto_total / total_usuarios

    def predict(self, usuario):
        return self.probabilidad_gusto * usuario["gusto"]

# Ejemplo de uso
sistema = SistemaRecomendacion()

# Entrenar el sistema con ejemplos de usuarios
usuarios_entrenamiento = [
    {"gusto": 0.8},  # Usuario que suele gustarle las películas
    {"gusto": 0.3},  # Usuario que rara vez le gustan las películas
    {"gusto": 0.6}   # Usuario con gustos intermedios
]
sistema.train(usuarios_entrenamiento)

# Predecir la preferencia de un nuevo usuario
nuevo_usuario = {"gusto": 0.7}  # Usuario con gusto moderado
probabilidad_gusto = sistema.predict(nuevo_usuario)
print("Probabilidad de gustarle la pelicula:", probabilidad_gusto)
