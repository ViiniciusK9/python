from cp import ContaPoupanca
from cc import ContaCorrente


cp = ContaPoupanca(12, 21, 0)
cp.depositar(500)
cp.sacar(100)
cp.sacar(500)
cp.sacar(400)

print("##############################")

cc = ContaCorrente(111, 222, 0, 400)
cc.depositar(500)
cc.sacar(100)
cc.sacar(500)
cc.sacar(1000)