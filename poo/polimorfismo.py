'''
Polimorfismo é o principio que permite que classes
derivadas de uma mesma superclasse tenham métodos iguais
(de mesma assinatura) mas comportamentos diferentes.
Mesma assinatura = Mesma quantidade e tipo de marâmetros.
'''

from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def falar(self, msg):
        pass


class B(A):
    def falar(self, msg):
        print(f"B está falando {msg}")
    

class C(A):
    def falar(self, msg):
        print(f"C está falando {msg}")


b1 = B()
c1 = C()


b1.falar("Um assunto.")
c1.falar("Outro assunto")