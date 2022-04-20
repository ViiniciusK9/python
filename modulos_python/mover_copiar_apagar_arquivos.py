
import os
import shutil 

caminho_original = r'C:\Users\green\Documents\teste'
caminho_novo = r'C:\Users\green\Documents\teste_2'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'A pasta {caminho_novo} já existe.')

for raiz, diretorios, arquivos in os.walk(caminho_original):
    for arquivo in arquivos:
        antigo_caminho_arquivo = os.path.join(raiz, arquivo)
        novo_caminho_arquivo = os.path.join(caminho_novo, arquivo)

        if 'nome_arquivo_mover' in arquivo:  
            shutil.move(antigo_caminho_arquivo, novo_caminho_arquivo) # Usado para mover arquivos de um diretorio para outro.
            print(f'Arquivo {arquivo} movido com sucesso.')

        if 'nome_arquivo_copiar' in arquivo:  
            shutil.copy(antigo_caminho_arquivo, novo_caminho_arquivo) # Usado para copiar arquivos de um diretorio para outro.
            print(f'Arquivo {arquivo} copiado com sucesso.')


for raiz, diretorios, arquivos in os.walk(caminho_novo):
    for arquivo in arquivos:
        antigo_caminho_arquivo = os.path.join(raiz, arquivo)
        novo_caminho_arquivo = os.path.join(caminho_novo, arquivo)

        if 'nome_arquivo_copiar' in arquivo:
            print(f'Arquivo {arquivo} apagado com sucesso.')
            os.remove(novo_caminho_arquivo) # Usado para apagar arquivos de um diretorio.
