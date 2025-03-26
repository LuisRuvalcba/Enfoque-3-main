class MotorInferenciaCerteza:
    def __init__(self):
        self.hechos = []

    def agregar_hecho(self, hecho, certeza):
        self.hechos.append((hecho, certeza))

    def inferir(self, pregunta):
        certeza_total = 1.0
        for hecho, certeza in self.hechos:
            if pregunta in hecho:
                certeza_total *= certeza
        return certeza_total

# Crear un motor de inferencia con factores de certeza
motor_certeza = MotorInferenciaCerteza()

# Establecer hechos con certeza
motor_certeza.agregar_hecho(["Pajaros", "Pueden volar"], 0.9)
motor_certeza.agregar_hecho(["Pingüinos", "Son pajaros"], 0.7)

# Consultar la certeza de que los pingüinos pueden volar
certeza_volar = motor_certeza.inferir(["Pingüinos", "Pueden volar"])

# Mostrar certeza
print("Certeza de que los pingüinos pueden volar:", certeza_volar)
