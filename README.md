# POO_Fazenda_Ludica
Aplicar os conceitos de Classe, Objeto, Herança e Polimorfismo, além de iniciar a prática de Encapsulamento, criando um sistema simples de gerenciamento de animais em uma fazenda lúdica.


### Abstração e Classe Base (Animal)

Esta classe abstrai as características e comportamentos comuns a todos os animais da fazenda.

````python
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        return "O animal emite um som."
    
    def apresentar(self):
        print(f"Olá, sou {self.nome} e tenho {self.idade} anos.")
````

### Herança e Especialização

Subclasses que herdam da classe Animal. Na classe Vaca, foi aplicado o encapsulamento no atributo ``producao_leite_litros``.

````python
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
````

### Teste e Demonstração
````python
cachorro = Cachorro("Rex", 3, "Labrador")
gato = Gato("Mimi", 5, "Branco")
vaca = Vaca("Mimosa", 7, 25.5)

lista_animais = [cachorro, gato, vaca]

for animais in lista_animais:
    print(animais.apresentar())
    print(animais.emitir_som())
````

### Teste de Encapsulamento
````python
# Para o objeto Vaca, imprima a produção atual utilizando o método getter:
print(f"Produção atual de leite: {vaca.obter_producao_leite()} litros")

# Chame o método registrar_ordenha() para mudar a produção de leite (ex: para 28.0 litros):
vaca.registrar_ordenha(28.0)

# Imprima novamente a produção de leite para confirmar a mudança:
print(f"Produção de leite após ordenha: {vaca.obter_producao_leite()} litros")
````