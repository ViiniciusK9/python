class Escritor:
    def __init__(self, nome, ferramenta=None):
        self.__nome = nome
        self.__ferramenta = ferramenta


    @property
    def nome(self):
        return self.__nome
    

    @nome.setter
    def nome(self, valor):
        self.__nome = valor
    

    @property
    def ferramenta(self):
        return self.__ferramenta


    @ferramenta.setter
    def ferramenta(self, valor):
        self.__ferramenta = valor
    


class Caneta:
    def __init__(self, nome):
        self.__nome = nome

    
    @property
    def nome(self):
        return self.__nome


    @nome.setter
    def nome(self, valor):
        self.__nome = valor


    def escrever(self):
        print("A caneta está escrevendo...")




"""
from classes import Escritor, Caneta

escritor = Escritor("Luiz")
caneta = Caneta("Bic")

escritor.ferramenta = caneta

print(escritor.ferramenta.nome)
escritor.ferramenta.escrever()
"""