class Pessoa:
    def __init__(self, nome: str, idade: int):
        if not isinstance(nome, str):
            raise TypeError("Nome precisa ser do tipo String.")
        if not isinstance(idade, int):
            raise TypeError("Idade precisa ser do tipo Int.")
        self.__nome = nome
        self.__idade = idade 
    

    @property
    def nome(self):
        return self.__nome


    @nome.setter
    def nome(self, novo_nome: str):
        if not isinstance(novo_nome, str):
            raise TypeError("Nome precisa ser do tipo String.")

        self.__nome = novo_nome
    

    @property
    def idade(self):
        return self.__idade


    @idade.setter
    def idade(self, nova_idade: int):
        if not isinstance(nova_idade, int):
            raise TypeError("Idade precisa ser do tipo Int.")
            
        self.__idade = nova_idade


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int):
        super().__init__(nome, idade)
        self.__conta
    

    
        