from conta import Conta


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self._saldo < valor:
            print("Saldo insuficiente.")
            return 
        
        self._saldo -= valor 
        self.detalhes()

