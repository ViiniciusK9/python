from abc import ABC, abstractmethod
from typing import Union

class Conta(ABC):
    def __init__(self, agencia: int, conta: int, saldo: Union(float, int)):
        self.__agencia = agencia
        self.__conta = conta 
        self.__saldo = saldo
    
    
    @property
    def saldo(self):
        return self.__saldo


    def depositar(self, valor: Union(float, int)):
        if valor < 0:
            raise ValueError("O valor a ser depositado precisa ser positivo.")

        if not isinstance(valor, (float, int)):
            raise TypeError("O valor precisa ser do tipo Int ou Float.")

        self.__saldo += valor


    @abstractmethod
    def sacar(self, valor):
        pass


class ContaPoupanca(Conta):
    def sacar(self, valor: Union(float, int)):
        if not isinstance(valor, (float, int)):
            raise TypeError("O valor precisa ser do tipo Int ou Float.")

        if (self.__saldo - valor) < 0:
            print("Saldo insuficiente.")
            return
        self.__saldo -= valor
        print("Valor sacado som sucesso.")


class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: Union(float, int), limite: Union(float, int)):
        super().__init__(agencia, conta, saldo)
        self.__limite = limite 
    
    
    def sacar(self, valor: Union(float, int)):
        pass