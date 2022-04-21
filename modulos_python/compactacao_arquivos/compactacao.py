from zipfile import ZipFile 
import os 

# Caminho de onde os arquivos que serão compactados estão.
caminho = r'C:/Users/green/Documents/git/python/modulos_python/compactacao_arquivos/arquivos_para_compactar/'

# Abrir arquivo zip no modo 'w' de escrita e salvar arquivos dentro.
with ZipFile('arquivo.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        zip.write(caminho_completo, arquivo) 

# Ler arquivo zip.
with ZipFile('arquivo.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

# Descompactar todos os arquivos que estão dentro do arquivo.zip.
with ZipFile('arquivo.zip', 'r') as zip:
    zip.extractall('descompactado')