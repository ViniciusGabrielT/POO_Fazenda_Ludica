# Abstração e Classe Base (Animal)

class Animal:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    def emitir_som(self):
        return "O animal emite um som."
    
    def apresentar(self):
        return "Olá, sou {nome} e tenho {idade} anos."
    
# Herança e Especialização

class Cachorro(Animal):
    def __init__(self, raca):
        super().__init__()
        self.raca = raca

    def emitir_som(self):
        return "Au! Au!"
    
class Gato(Animal):
    def __init__(self, cor_pelo):
        super().__init__()
        self.cor_pelo = cor_pelo

    def emitir_som(self):
        return "Miau!"
    
class Vaca(Animal):
    def __init__(self, producao_leite_litros):
        super().__init__()
        self.producao_leite_litros = producao_leite_litros

    def emitir_som(self):
        return "Muuu!"