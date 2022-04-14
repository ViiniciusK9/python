'''
class Arquivo:
    def __init__(self, arquivo, modo):
        print("Abrindo arquivo.")
        self.arquivo = open(arquivo, modo)
    

    def __enter__(self):
        return self.arquivo
    


    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Fechando arquivo.")
        self.arquivo.close()

        # Caso haja tratamento de exceções devem ser resolvidas antes e depois retornar true
        return True



with Arquivo('teste.txt', 'w') as ar:
    ar.write("Teste de escrita.\n")
    ar.testeexcecao("teste de excecao.\n")
'''


from contextlib import contextmanager


@contextmanager
def abrir(arquivo, modo):
    try:
        print("Abrindo arquivo")
        arquivo = open(arquivo, modo)
        yield arquivo 
    finally:
        print("Fechando arquivo.")
        arquivo.close()


with abrir("teste2.txt", "w") as ar:
    ar.write("Testando escrita em arquivo.")
    