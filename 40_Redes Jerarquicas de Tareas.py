class Task:
    def __init__(self, name, subtasks=None):
        self.name = name
        self.subtasks = subtasks if subtasks is not None else []

    def add_subtask(self, subtask):
        self.subtasks.append(subtask)

    def execute(self):
        print(f"Ejecutando tarea: {self.name}")
        for subtask in self.subtasks:
            subtask.execute()

# Crear las tareas
tarea_principal = Task("Tarea Principal")
subtarea1 = Task("Subtarea 1")
subtarea2 = Task("Subtarea 2")
subsubtarea1 = Task("Subsubtarea 1")
subsubtarea2 = Task("Subsubtarea 2")

# Construir la jerarquía de tareas
tarea_principal.add_subtask(subtarea1)
tarea_principal.add_subtask(subtarea2)
subtarea1.add_subtask(subsubtarea1)
subtarea1.add_subtask(subsubtarea2)

# Ejecutar la tarea principal
tarea_principal.execute()
