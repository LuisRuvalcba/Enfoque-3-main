# Definir datos de ejemplo: características de diferentes animales
datos = [
    {"pelo": "si", "garras": "no", "cola": "si", "clase": "mamifero"},
    {"pelo": "no", "garras": "si", "cola": "si", "clase": "mamifero"},
    {"pelo": "si", "garras": "no", "cola": "no", "clase": "mamifero"},
    {"pelo": "no", "garras": "si", "cola": "no", "clase": "reptil"},
]

# Definir función para generar reglas de FOIL
def foil(datos):
    regla = "IF "
    caracteristicas = datos[0].keys()
    for caracteristica in caracteristicas:
        valores = set([dato[caracteristica] for dato in datos])
        for valor in valores:
            if valor != "si":
                regla += caracteristica + "=" + valor + " AND "
    regla = regla[:-5] + " THEN clase=" + datos[0]["clase"]
    return regla

# Generar reglas de FOIL
regla_foil = foil(datos)
print("Regla de FOIL:", regla_foil)
