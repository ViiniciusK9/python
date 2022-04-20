"""
Comma Separated Values - CSV (Valores separados por vírgula)
É um formato de dados muito usado em tabelas (Excel, Google Sheets), bases de
dados, clientes de e-mail, etc...
"""
import csv


def ler_csv_list():
    with open('clientes.csv', 'r') as arquivo:
        dados = csv.reader(arquivo)
        next(dados) # Pular primeira linha do iterador para não pegar o nome das colunas.

        for dado in dados:
            print(dado)

def ler_csv_dict():
    with open('clientes.csv', 'r') as arquivo:
        dados = csv.DictReader(arquivo)

        for dado in dados:
            print(dado)

def ler_csv_dict_return_dados():
    with open('clientes.csv', 'r') as arquivo:
        return [x for x in csv.DictReader(arquivo)]


dados = ler_csv_dict_return_dados()


def escrever_csv():
    with open('cliente2.csv', 'w', newline='') as arquivo:
        escreve = csv.writer(
            arquivo,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_ALL
        )

        chaves = list(dados[0].keys())
        
        escreve.writerow(
                [
                    chaves[0],
                    chaves[1],
                    chaves[2],
                    chaves[3]
                ]
            )


        for dado in dados:
            escreve.writerow(
                [
                    dado['Nome'],
                    dado['Sobrenome'],
                    dado['E-mail'],
                    dado['Telefone']
                ]
            )





#escrever_csv()
#ler_csv_dict()
#ler_csv_list()