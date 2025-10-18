# Abstração e Classe Base (Animal)

class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        return "O animal emite um som."
    
    def apresentar(self):
        return "Olá, sou {nome} e tenho {idade} anos."
    
# Herança e Especialização

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def emitir_som(self):
        return "Au! Au!"
    
class Gato(Animal):
    def __init__(self, nome, idade, cor_pelo):
        super().__init__(nome, idade)
        self.cor_pelo = cor_pelo

    def emitir_som(self):
        return "Miau!"
    
class Vaca(Animal):
    def __init__(self, nome, idade, producao_leite_litros):
        super().__init__(nome, idade)
        self.__producao_leite_litros = producao_leite_litros

    def emitir_som(self):
        return "Muuu!"
    
    def obter_producao_leite(self): # getter
        return self.__producao_leite_litros
    
    def registrar_ordenha(self, litros): # setter
        self.__producao_leite_litros = litros

# Teste e Demonstração

cachorro = Cachorro("Rex", 3, "Labrador")
gato = Gato("Mimi", 5, "Branco")
vaca = Vaca("Mimosa", 7, 25.5)

lista_animais = [cachorro, gato, vaca]

for animais in lista_animais:
    print(animais.apresentar())
    print(animais.emitir_som())