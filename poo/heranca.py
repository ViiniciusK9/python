class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    
    def falar(self):
        print(f"{self.nome} está falando...")


class Aluno(Pessoa):
    def estudar(self):
        print(f"{self.nome} está estudando...")


class Cliente(Pessoa):
    def comprar(self):
        print(f"{self.nome} está comprando...")



"""
from heranca import *

a1 = Aluno("Vinicius", 19)
print(a1.nome)
a1.estudar()
a1.falar()

c1 = Cliente("Maria", 22)
print(c1.nome)
c1.comprar()
c1.falar()

p1 = Pessoa("Joao", 32)
p1.falar()
"""