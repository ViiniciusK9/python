class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f"{self.nomeclasse} falando...")


class Cliente(Pessoa):
    def comprar(self):
        print(f"{self.nomeclasse} comprando...")

    def falar(self):
        print("Estou em CLIENTE.")


class ClienteVIP(Cliente):

    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade) #Pessoa.__init__(nome, idade)
        self.sobrenome = sobrenome


    def falar(self):
        super().falar()
        Pessoa.falar(self)
        Cliente.falar(self)
        print("Outra coisa")
        print(f"{self.nome} {self.sobrenome}")


"""
from sobreposicao_membros import *
from sobreposicao_membros import ClienteVIP

c1 = ClienteVIP("Vinicius", 19, "Silva")

c1.falar()
"""
