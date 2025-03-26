class Fruta:
    def __init__(self, nombre):
        self.nombre = nombre

class Manzana(Fruta):
    def __init__(self, nombre):
        super().__init__(nombre)

class Platano(Fruta):
    def __init__(self, nombre):
        super().__init__(nombre)

class Limon(Fruta):
    def __init__(self, nombre):
        super().__init__(nombre)

# Crear instancias
mi_manzana = Manzana("Golden")
mi_platano = Platano("Cavendish")
mi_limon = Limon("Verde")

# Mostrar información
print("Mi manzana es de tipo", mi_manzana.nombre)
print("Mi plotano es de tipo", mi_platano.nombre)
print("Mi limon es de tipo", mi_limon.nombre)
