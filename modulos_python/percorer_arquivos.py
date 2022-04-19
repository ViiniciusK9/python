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

caminho_procura = input("Digite o caminho inicial: ")
termo_procura = input("Digite o termo de busca: ")

conta = 0
for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
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

print()
print(f'{conta} arquivo(s) encontrado(s).')
