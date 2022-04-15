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

class MinhaClasse:
    """Descrição simples e curta da classe

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

    atributo_classe_1 = 1
    atributo_classe_2 = "Valor"

    def __init__(self, texto):
        """Inicializa os dados

        :param texto: o parametro que vai virar atributo da instância
        :type texto: str
        """
        self.texto = texto
        self.exibe_texto(texto)

    
    @staticmethod
    def exibe_texto(texto):
        """ Método que exibe um texto de 100 caracteres na tela

        :param texto: Um texto de 100 caracteres
        :type texto: str

        :return: O texto de 100 caracteres
        :rtype: str

        :raises ValueError: Se o texto tiver mais que 100 caracteres
        :raises TypeError: Se o texto não for uma String
        """

        if not isinstance(texto, str):
            raise TypeError("texto precisa ser uma string.")
        
        if len(texto) > 100:
            raise ValueError("Texto precisa ter 100 caracteres ou menos.")
        
        return texto