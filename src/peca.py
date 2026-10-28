#peÇa peÇa peÇa peÇa peÇa peÇa peÇa 
class Peca:
    def __init__(self, color, posicio):
        self.color = color
        self.posicio = posicio
        self.primer_moviment = True

    def moure(self, nova_posicio):
        self.posicio = nova_posicio

    def mostrar(self):
        print(f"{self.color} - {self.posicio}")