class MotorInferenciaNoMonotónico:
    def __init__(self):
        self.hechos = []

    def agregar_hecho(self, hecho):
        self.hechos.append(hecho)

    def inferir(self, pregunta):
        for hecho in self.hechos:
            if pregunta in hecho:
                if "¿?" in hecho:
                    return "Desconocido"
                elif "¡!" in hecho:
                    return "No"
                elif "¡?" in hecho:
                    return "Desconocido"
                else:
                    return "Sí"
        return "Desconocido"

# Crear un motor de inferencia no monotónico
motor_nm = MotorInferenciaNoMonotónico()

# Establecer hechos
motor_nm.agregar_hecho(["Pajaros", "Pueden volar"])
motor_nm.agregar_hecho(["Pingüinos", "Son pajaros", "¡!"])

# Consultar si los pingüinos pueden volar
resultado_nm = motor_nm.inferir(["Pingüinos", "Pueden volar"])

# Mostrar resultado
if resultado_nm == "Sí":
    print("Los pingüinos pueden volar (monotonico)")
elif resultado_nm == "No":
    print("Los pingüinos no pueden volar (no monotonico)")
else:
    print("Se desconoce si los pingüinos pueden volar (no monotonico)")
