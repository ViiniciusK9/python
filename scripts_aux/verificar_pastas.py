from datetime import datetime
import pandas as pd
import shutil
import os


def mostrar_arquivo(arquivo):
    try:
        conta += 1
        caminho_completo = os.path.join(raiz, arquivo)
        nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
        tamanho_arquivo = os.path.getsize(caminho_completo)

        print()
        print(f'Encontrei o arquivo: {arquivo}')
        print(f'Caminho: {caminho_completo}')
        print(f'Nome: {nome_arquivo}')
        print(f'Extensão: {ext_arquivo}')
        print(f'Tamanho: {tamanho_arquivo}')
        print(f'Tamanho (Formatado): {formata_tamanho(tamanho_arquivo)}')
    except PermissionError as eerror:
        print(f'Sem permissões: {error}')
    except FileNotFoundError as error:
        print(f'Arquivo não encontrado: {error}')
    except Exception as error:
        print(f'Erro desconhecido: {error}')


caminho_procura = r"C:\Users\vinic\OneDrive\Imagens\aulas"
caminho_salvar = r"C:\Users\vinic\OneDrive\Área de Trabalho\pastas_aulas"

def get_materia(dia, hora):
    hora = int(hora)
    if(dia == 0):
        if(13 <= hora < 16):
            return "sistemas_digitais"
        else:
            return "mat_discreta"
    if(dia == 1):
        if(13 <= hora < 16):
            return "prog_1"
        else:
            return "sistemas_digitais"
    if(dia == 2):
        if(10 <= hora < 13):
            return "algebra_linear"
        else:
            return "mat_discreta"
    if(dia == 3):
        if(16 <= hora <= 19):
            return "calculo_2"
    if(dia == 4):
        if(10 <= hora < 13):
            return "algebra_linear"
        else:
            return "calculo_2"

conta_t = 0
conta = 0

copo = dict()

for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for diretorio in diretorios:
        #print(diretorio)
        conta = 0
        for root, dirs, files in os.walk(f"{caminho_procura}\{diretorio}"):
            for file in files:
                conta_t += 1
                conta += 1
        copo[diretorio] = conta
        #print(f'{conta} arquivo(s) encontrado(s).')
    

#print(copo)

for raiz, diretorios, arquivos in os.walk(caminho_salvar):
    for diretorio in diretorios:
        #print(diretorio)
        conta = 0
        for root, dirs, files in os.walk(f"{caminho_salvar}\{diretorio}"):
            for file in files:
                conta_t += 1
                conta += 1
        try:
            if(copo[diretorio] == conta):
                print("Ok")
            else:
                print(f"Erro: {diretorio}  diff_arquivos: {abs(copo[diretorio] - conta)}")
        except KeyError:
            pass
        
        

print()
print(f'{conta_t} arquivo(s) encontrado(s).')