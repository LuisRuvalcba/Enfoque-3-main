class PIDController:
    def __init__(self, setpoint, kp, ki, kd):
        self.setpoint = setpoint
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.prev_error = 0
        self.integral = 0

    def compute(self, current_value):
        error = self.setpoint - current_value
        self.integral += error
        derivative = error - self.prev_error
        output = self.kp * error + self.ki * self.integral + self.kd * derivative
        self.prev_error = error
        return output

# Ejemplo de uso
pid_controller = PIDController(setpoint=25, kp=1, ki=0.1, kd=0.01)

# Simulación de proceso continuo
for _ in range(10):
    current_temp = 20  # Temperatura actual (por ejemplo)
    control_signal = pid_controller.compute(current_temp)
    # Aplicar el control_signal al sistema (por ejemplo, ajustar el calentador)
    print(f"Control signal: {control_signal}")
