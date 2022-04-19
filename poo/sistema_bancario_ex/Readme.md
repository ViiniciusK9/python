<h1 align="center">Sistema bancário simples</h1>

Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (Extremamente simples) que tem clientes, conta e um banco. 
A ideia é que o cliente tenha uma conta (Poupança ou corrente) e que possa sacar/depositar 
nessa conta. Contas corrente tem um limite extrar. Banco tem clientes e contas.

## Dicas:

## Criar classe Cliente que herda da classe Pessoa (Herança):
- Pessoa tem nome e idade (Com getters e setters).
- Cliente tem conta (Agregação da classe ContaCorrente ou ContaPoupanca).
## Criar classes ContaPoupanca e ContaCorrente que herdam de Conta:
- ContaCorrente deve ter um limite extra.
- Contas têm agência, número da conta e saldo.
- Contas devem ter método para depósito.
- Conta (Super classe) deve ter o método sacar abstrato (Abstração e polimorfismo - As subclasses que implementam o metódo sacar).
## Criar classe Banco para agregar classes de clientes e de contas (Agregação).
## Banco será responsável autenticar o cliente e as contas da seguite maneira: 
- Banco tem contas e clientes (Agregação).
- Checar se a agência é daquele banco.
- Checar se o cliente é daquele banco.
- Checar se a conta é daquele banco.
## Só será possivel sacar se passar na autenticação do banco (descrita acima).