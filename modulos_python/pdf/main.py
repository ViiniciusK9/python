"""
Documentação:
https://pythonhosted.org/PyPDF2/
Mais exemplos de uso:
https://www.blog.pythonlibrary.org/2018/06/07/an-intro-to-pypdf2/

pip install pypdf2
"""

import PyPDF2
import os

# Caminho de onde os pdf que serão manipulados estão
caminho_pdf = r'meus_pdf'


def juntar_arquivos():
    # Inicializando objeto que será o novo PDF.
    novo_pdf = PyPDF2.PdfFileMerger()

    # Percorrendo os arquivos que serão unidos.
    for root, dirs, files in os.walk(caminho_pdf):
        for file in files:
            # Criando o caminho completo do arquivo.
            caminho_completo_arquivo = os.path.join(root, file)

            # Abrindo o arquivo em modo de leitura binaria.
            arquivo_pdf = open(caminho_completo_arquivo, 'rb')

            # Adicionando arquivo no novo pdf.
            novo_pdf.append(arquivo_pdf)

    # Abrindo novo pdf em modo escrita binaria.
    with open(fr'{caminho_pdf}\novo_arquivo.pdf', 'wb') as meu_novo_pdf:
        # Escrevendo o novo pdf.
        novo_pdf.write(meu_novo_pdf)


def separar_arquivo_por_pagina():
    # Abrindo o pdf que será separado em modo leitura binaria.
    with open(fr'{caminho_pdf}\novo_arquivo.pdf', 'rb') as arquivo:
        # Instanciando o objeto no modo leitura do PDF aberto na linha acima.
        leitor = PyPDF2.PdfFileReader(arquivo)

        # Pegando o numero de paginas que possui o pdf.
        num_paginas = leitor.getNumPages()

        # Percorrendo as paginas para separar o pdf.
        for num_pagina in range(num_paginas):
            # Instanciando objeto que será escrito.
            escritor = PyPDF2.PdfFileWriter()

            # Pegando a pagina atual do pdf que será separado.
            pagina_atual = leitor.getPage(num_pagina)

            # Adicionando a pagina no pdf.
            escritor.addPage(pagina_atual)

            # Abrindo e escrevendo o novo pdf.
            with open(fr'novos_pdfs\{num_pagina}.pdf', 'wb') as novo_pdf:
                escritor.write(novo_pdf)

    


