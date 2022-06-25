from datetime import datetime
import pandas as pd
import shutil
import os




def formata_tamanho(tamanho): # função que converte de bytes para a representação inteira menor possivel.
    kilo = 1024
    mega = kilo ** 2
    giga = kilo ** 3
    tera = kilo ** 4
    peta = kilo ** 5

    if tamanho < kilo:
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo 
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega 
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga 
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera 
        texto = 'T'
    else:
        tamanho /= peta 
        texto = 'P'
    
    return f'{tamanho:.2f} {texto}'

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


caminho_procura = r"C:\Users\vinic\OneDrive\Área de Trabalho\fotos_aulas"
#termo_procura = input("Digite o termo de busca: ")
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

conta = 0

for raiz, diretorios, arquivos in os.walk(caminho_procura):
    #for arquivo in arquivos:
        #if termo_procura in arquivo:
    for arquivo in arquivos:
        conta+=1
        antigo = f"{raiz}\{arquivo}"
        #print(f"{raiz}\{arquivo}")
        _, data, horas = arquivo.split("_")
        
        dia = data[6:8]
        mes = data[4:6]        
        ano = data[0:4]
        hora = horas[0:2]
        minuto = horas[2:4]
        segundo = horas[4:6]
        
        #print(dia, mes, ano)
        #print(hora, minuto, segundo)
        
        temp = pd.Timestamp(f"{ano}-{mes}-{dia}")
        materia = get_materia(temp.dayofweek, hora)

        novo = f"{caminho_salvar}\{materia} {mes}-{dia}\{arquivo}"
        if not os.path.exists(f"{caminho_salvar}\{materia} {mes}-{dia}"):
            os.makedirs(f"{caminho_salvar}\{materia} {mes}-{dia}")
        
        #print(novo)
        shutil.copy(antigo, novo) 
        
        

print()
print(f'{conta} arquivo(s) encontrado(s).')