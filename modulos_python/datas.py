# https://docs.python.org/3.0/library/datetime.html

from datetime import datetime, timedelta

data_0 = datetime(2022, 10, 22, 12, 50, 23) # criar datas: Ano, mes, dia, hora, minuto e segundo.
print()
print(f'data_0 formato padrão: {data_0}')
print(f'data_0 formato customizado: {data_0.strftime("%d/%m/%Y %H:%M:%S")}') # mudar a formato para printar uma data.
print()

data_1 = datetime.strptime('25/01/2000', '%d/%m/%Y') # criar data em formato customizado, podendo fazer a partir de uma string.
print(f'data_1: {data_1}')
print(f'Timestamp da data_1: {data_1.timestamp()}') # obtendo o timestamp de uma data.

print()
data_2 = datetime.fromtimestamp(948769200.0) # criando uma data a partir de um timestamp.
print(f'data_2: {data_2}')
print()

print("#"*50)

data_3 = datetime.strptime('25/01/2000 20:00:10', "%d/%m/%Y %H:%M:%S")
print(f'data_3: {data_3.strftime("%d/%m/%Y %H:%M:%S")}')
data_3 = data_3 + timedelta(days = 5, seconds= 5) # fazendo operações aritimeticas de tempo com as datas.
print(f'data_3 + 5 dias e 5 segundos: {data_3.strftime("%d/%m/%Y %H:%M:%S")}')
print()

data_4 = datetime.strptime('28/11/2000 04:22:09', "%d/%m/%Y %H:%M:%S")
print(f'data_4: {data_4.strftime("%d/%m/%Y %H:%M:%S")}')
dif_data = data_4 - data_3 # fazendo operações aritimeticas entre datas.
print(f'Diferença entre data_4 - data_3: {dif_data}')
print(f'Diferença entre data_4 - data_3 em segundos: {dif_data.total_seconds()}')
print(f'Diferença entre data_4 - data_3 em dias: {dif_data.days}')

print("#"*50)

data_5 = datetime(2022, 12, 19, 22, 23, 57)

print(f'hora da data_5: {data_5.time()}') # mostrando apenas as horas de uma data.
print(f'data da data_5: {data_5.date()}') # mostrando apenas a data de uma data.
print(f'dia da semana da data_5: {data_5.weekday()}') # mostrando apenas o dia da semana de uma data; 0 - segunda -> 6 - domingo.