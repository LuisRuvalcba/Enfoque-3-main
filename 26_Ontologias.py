from owlready2 import *

# Crear una ontología básica
onto = get_ontology("http://www.ejemplo.com/ontologia#")

# Definir clases
with onto:
    class Persona(Thing):
        pass

    class Estudiante(Persona):
        pass

    class Profesor(Persona):
        pass

# Definir propiedades
class tieneNombre(Persona >> str):
    pass

# Crear instancias
juan = Estudiante()
juan.tieneNombre = ["Juan"]

# Guardar ontología
onto.save("ontologia_ejemplo.owl")

# Cargar ontología existente
onto = get_ontology("ontologia_ejemplo.owl").load()

# Consulta: Encontrar todos los estudiantes
for instancia in onto.search(type=onto.Estudiante):
    print("Estudiante:", instancia.tieneNombre)

# Consulta: Encontrar todos los profesores
for instancia in onto.search(type=onto.Profesor):
    print("Profesor:", instancia.tieneNombre)
