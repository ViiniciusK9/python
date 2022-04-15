"""Documentação deste módulo

Typing - https://docs.python.org/3/library/typing.html
"""
from typing import Union

x: int = 10
y: float = 10.5
z: bool = False


def funcao(p1: float, p2: str, p3: dict) -> Union(float, list):
    return []


class MinhaClasse:
    """Documentação normal

    Conforme qualquer outra documentação que você tenha usado anteriormente.
    """

    atributo1 = 1
    atriburo2 = "valor"


    def __init__(self, texto: str):
        """Inicializa os dados

        :param texto: o parametro que vai virar atributo da instância
        :type texto: str
        """
        self.texto: str = texto
        self.exibe_texto(texto)

    
    @staticmethod
    def exibe_texto(texto: str) -> str:
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


    def outro_metodo(self, inteiro: int, flutuante: float = 0.0) -> bool:
        """Retorna um valor booleano sem motivo aparente

        :param inteiro: um número inteiro
        :type inteiro: int
        :param flutuante: um número de ponto flutuante
        :type flutuante: float

        :return: Um booleano
        :rtype: bool
        """
        return True