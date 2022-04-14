class CriandoUmError(Exception):
    pass


def testar():
    raise CriandoUmError("Mensagem do erro criado.")


try:
    testar()
except CriandoUmError as error:
    print(f"Erro: {error}")
