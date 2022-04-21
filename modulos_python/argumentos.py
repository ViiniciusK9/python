import sys
import os

# Exemplo: python argumentos.py -a -b -c -d 

argumentos = sys.argv
print(argumentos)  # ['argumentos.py', '-a', '-b', '-c', '-d']
qtd_arg = len(argumentos)

if qtd_arg <= 1:
    print('Faltando argumentos: ')
    print('-a', 'Para listar todos os arquivos neste diretorio', sep='\t')
    print('-d', 'Para listar todos os diretorios neste diretorio', sep='\t')
    sys.exit()


f_arquivos = False
f_diretorios = False

if '-a' in argumentos:
    f_arquivos = True

if '-d' in argumentos:
    f_diretorios = True 

for arquivo in os.listdir('.'):
    if f_arquivos:
        if os.path.isfile(arquivo):
            print(arquivo)
    
    if f_diretorios:
        if os.path.isdir(arquivo):
            print(arquivo)
