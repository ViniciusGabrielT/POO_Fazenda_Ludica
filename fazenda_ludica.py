# Abstração e Classe Base (Animal)

class Animal:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def emitir_som(self):
        return "O animal emite um som."
    
    def apresentar(self):
        return f"Olá, sou {nome} e tenho {idade} anos."