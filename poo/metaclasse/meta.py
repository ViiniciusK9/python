'''
Em python tudo é um objeto: incluindo classes.
Metaclasse são as 'classes' que criam classes.
'''

'''
class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == "A":
            return type.__new__(mcs, name, bases, namespace)
        
        if "b_fala" not in namespace:
            print(f"Você precisa criar o mêtodo b_fala em {name}.")
        else:
            if not callable(namespace['b_fala']):
                print(f"b_fala precisa ser um mêtodo e não um atribulo em {name}.")
        
        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    def falar(self):
        self.b_fala()


class B(A):
    def b_fala(self):
        print("Tudo ok")


b1 = B()

b1.falar()
'''

class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == "A":
            return type.__new__(mcs, name, bases, namespace)
        
        if "attr_classe" in namespace:
            print(f"{name} tentou mudar o atributo.")
            del namespace["attr_classe"]
        
        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    attr_classe = "Valor A"


class B(A):
    attr_classe = "Valor B"


class C(B):
    attr_classe = "Valor C"


c1 = C()

print(c1.attr_classe)