import random 
import string

# Gera um número inteiro entre A e B.
inteiro = random.randint(10, 20)
print(f'Inteiro: {inteiro}')

# Gera um número de ponto flutuante entre A e B.
flutuante_1 = random.uniform(10, 20)
print(f'Flutuante_1: {flutuante_1}')

# Gera um número de ponto flutuante entre 0 e 1.
flutuante_2 = random.random()
print(f'Flutuante_2: {flutuante_2}')

# Gera um número utilizando o range(inicio, final, passo).
num_range = random.randrange(100, 901, 50)
print(f'Num_range: {num_range}')

# Seleciona aleatóriamente um nome em uma lista de nomes.
lista_nomes = ['aaaaaaa', 'bbbbbbbbbb', 'cccccccc', 'ddddddddd', 'eeeeeeee', 'fffffffff', 'gggggg', 'hhhhhh', 'iiiiiii', 'jjjjjj']
sorteio_nome = random.choice(lista_nomes)
print(f'Sorteio_nome: {sorteio_nome}')

# Seleciona aleatóriamente k nomes em uma lista de nomes (OBS: podendo repetir o mesmo nome).
sorteio_nomes = random.choices(lista_nomes, k=2)
print(f'Sorteio_nomes: {sorteio_nomes}')

# Seleciona aleatóriamente n nomes em uma lista de nomes (OBS: sem repetir nome).
sorteio_nomes_sample = random.sample(lista_nomes, 2)
print(f'Sorteio_nomes_sample: {sorteio_nomes_sample}')

# Embaralha a lista
random.shuffle(lista_nomes)
print(f'Lista_nomes_aleatoria: {lista_nomes}')


# Gera senha aleatória

letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%&*'
geral = letras + digitos + caracteres
senha = ''.join(random.choices(geral, k=20))

print(f'Senha_aleatoria: {senha}')
