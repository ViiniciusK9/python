class CarrinhoDeCompras:
    def __init__(self):
        self.__produtos = []
    

    def inserir_produto(self, produto):
        self.__produtos.append(produto)


    def listar_produtos(self):
        for produto in self.__produtos:
            print(produto.nome, produto.valor)


    def somar_total(self):
        total = 0
        for produto in self.__produtos:
            total += produto.valor
        return total

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor



"""
from agregacao import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto("Mouse", 120)
p2 = Produto("Teclado", 450)
p3 = Produto("Microfone", 100)
p4 = Produto("Monitor", 1290)

carrinho.listar_produtos()
carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p4)
carrinho.listar_produtos()
print(carrinho.somar_total())
"""