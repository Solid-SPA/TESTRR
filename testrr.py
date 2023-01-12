class Canino:
    def __init__(self, patas, aullido):
        self.patas = patas
        self.aullido = aullido

class Animal(Canino):
    def __init__(self, patas, aullido,tipo,color,raza):
        super().__init__(patas, aullido)
        self.color = color
        self.raza = raza
        self.tipo = tipo

    def TipoAnimal(self):
        print(f"""El canino {self.tipo} y tiene {self.patas} patas de color {self.color}
        De raza {self.raza}""")
    

animalP = Animal("4", 'Guau Guau', "Perro",'negro', 'Golden')
animalL = Animal("4", 'Auuuuuu', "Lobo",'Gris', 'Golden')
# imprimir
print(animalP.TipoAnimal())
print(animalL.TipoAnimal())