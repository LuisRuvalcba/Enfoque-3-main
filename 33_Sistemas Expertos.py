class MotorInferencia:
    def __init__(self):
        self.reglas = []

    def agregar_regla(self, antecedente, consecuente):
        self.reglas.append((antecedente, consecuente))

    def inferir(self, hechos):
        inferido = False
        while not inferido:
            inferido = True
            for antecedente, consecuente in self.reglas:
                if all(item in hechos for item in antecedente) and consecuente not in hechos:
                    hechos.append(consecuente)
                    inferido = False

# Crear un motor de inferencia basado en reglas y cadena de inferencia
motor_experto = MotorInferencia()

# Definir reglas
motor_experto.agregar_regla(["Es mamifero", "Tiene pelo"], "Es un mamífero")
motor_experto.agregar_regla(["Pone huevos", "Es mamifero"], "Es un ave")
motor_experto.agregar_regla(["Tiene aletas", "Vive en el agua"], "Es un pez")

# Consultar al sistema experto
hechos = ["Tiene aletas", "Vive en el agua"]
motor_experto.inferir(hechos)

# Mostrar resultado
print("El animal inferido es:", hechos[-1])
