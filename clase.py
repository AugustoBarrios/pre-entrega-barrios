import random

class Clientes:
    def __init__(self, nombre, apellido, edad, nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nEdad: {self.edad}\nNacionalidad: {self.nacionalidad}"

    def generar_edad_aleatoria(self):
        self.edad = random.randint(18, 80)

    def generar_nacionalidad_aleatoria(self):
        nacionalidades = ["mexicana", "estadounidense", "canadiense", "española", "colombiana", "brasileña"]
        self.nacionalidad = random.choice(nacionalidades)

""" cliente_1 = Clientes("Juan", "Pérez", 25, "mexicana")

cliente_1.generar_edad_aleatoria()
cliente_1.generar_nacionalidad_aleatoria()

print(cliente_1) """
