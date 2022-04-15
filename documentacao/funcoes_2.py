"""Descrição rapida e simples

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean sit
amet faucibus erat. Maecenas eu arcu lectus. Morbi et nunc leo.
Integer sodales elementum dui vitae condimentum. Integer enim 
orci, cursus sed magna eu, semper lobortis arcu. Nullam 
sollicitudin erat eget risus posuere dictum. In pulvinar 
tincidunt neque, quis vestibulum orci imperdiet et.


Etiam risus elit, aliquet vitae nisl eu, venenatis feugiat nunc. 
Maecenas tempus risus urna, vitae ullamcorper lacus tincidunt ac. 
Pellentesque habitant morbi tristique senectus et netus et 
malesuada fames ac turpis egestas. Donec et aliquet dui. Etiam vel 
tincidunt est. Nulla sed fringilla purus. Integer sit amet rutrum 
dolor, sed aliquam nulla. Quisque et metus massa. Vestibulum ac 
justo lacus. Suspendisse fringilla ac mauris vitae pulvinar. 
Suspendisse volutpat at risus at iaculis. Maecenas ac dictum magna.
"""

variavel_1 = 'valor 1'

def soma(x, y):
    """
    Soma x e y
    
    :param x: Primeiro número
    :type x: int ou float
    :param y: Segundo número
    :type y: int ou float

    :return: A soma entre x e y
    :rtype: int ou float
    """
    return x + y


def multiplica(x, y, z=None):
    """
    Multiplica x, y e z

    Multiplica x, y e z. O programador pode omitir a variável z caso não
    tenha necessidade de usá-la.

    :param x: Primeiro número
    :type x: int ou float
    :param y: Segundo número
    :type y: int ou float
    :param z: Terceiro número (Opcional)
    :type z: int, float ou None

    :return: A multiplicação entre x, y e z
    :rtype: int or float
    """
    if z:
        return x * z
    else:
        return x * y * z 


variavel_2 = "valor 2"
variavel_3 = "valor 3"
variavel_4 = "valor 4"