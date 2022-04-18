from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta 
        self.saldo = saldo
    

    def depositar(self, valor):
        if valor < 0:
            raise ValueError("O valor a ser depositado precisa ser positivo.")

        if not isinstance(valor, (float, int)):
            raise TypeError("O valor precisa ser do tipo Int ou Float.")

        self.saldo += valor
        self.detalhes()


    def detalhes(self):
        print(f"Agência: {self.agencia}\nConta: {self.conta}\nSaldo: {self.saldo}")


    @abstractmethod
    def sacar(self, valor): pass


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if not isinstance(valor, (float, int)):
            raise TypeError("O valor precisa ser do tipo Int ou Float.")

        if (self.saldo - valor) < 0:
            print("Saldo insuficiente.")
            return

        self.saldo -= valor
        print("Valor sacado som sucesso.")
        self.detalhes()


class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite 
    
    
    def sacar(self, valor):
        if not isinstance(valor, (float, int)):
            raise TypeError("O valor precisa ser do tipo Int ou Float.")

        if (self.saldo + self.limite) < valor:
            print("Saldo insuficiente.")
            return

        self.saldo -= valor
        print("Valor sacado som sucesso.")
        self.detalhes()