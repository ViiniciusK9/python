"""
No Python, o comportamento dos operadores é definido por métodos especiais.
Vamos alterar o comportamento de operadores com classes definidas pelo usuário.

Operador    Método          Operação
------------------------------------------------------
+           __add__         adição
-           __sub__         subtração
*           __mul__         multiplicação
/           __div__         divisão
//          __floordiv__    divisão inteira
%           __mod__         Módulo
**          __pow__         Potência
+           __pos__         Positivo
-           __neg__         Negativo
<           __lt__          Menor que
>           __gt__          Maior que
<=          __le__          Menor ou igual a
>=          __ge__          Maior ou igual a
==          __eq__          Igual a
!=          __ne__          Diferente de
<<          __lshift__      Deslocamento para a esquerda
>>          __rshift__      Deslocamento para a direita
&           __and__         E bit-a-bit
|           __or__          OU bit-a-bit
^           __xor__         OU exclusivo bit-a-bit
~           __inv__         inversão
"""

class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura 
    

    def get_area(self):
        return self.altura * self.largura
    

    def __repr__(self): # Muda o retorno que apare ao printar um objeto da classe Retangulo
        return f"class Retangulo({self.altura}, {self.largura})"


    def __add__(self, other):
        nova_altura = self.altura + other.altura
        nova_largura = self.largura + other.largura
        return Retangulo(nova_altura, nova_largura)


    def __gt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()
        if a1 > a2:
            return True
        else:
            return False


    def __lt__(self, other):
        a1 = self.get_area()
        a2 = other.get_area()
        if a1 < a2:
            return True
        else:
            return False


    def __eq__(self, other):
        if self.largura == other.largura and self.altura == other.altura:
            return True 
        else:
            return False 



r1 = Retangulo(10, 20)
r2 = Retangulo(10, 20)

r3 = r1 + r2 

print(f"r1: {r1}")
print(f"r2: {r1}")
print(f"r3: {r3}")
print(f"r1 + r2: {r1 + r2}")
print(f"r1 > r2: {r1 > r2}")
print(f"r1 == r2: {r1 == r2}")
print(f"r1 == r3: {r1 == r3}")
print(f"r3 < r1: {r3 < r1}")
