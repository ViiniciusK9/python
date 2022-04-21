import requests
from bs4 import BeautifulSoup

url = 'https://pt.stackoverflow.com/questions/tagged/python'

response = requests.get(url)
#print(response.text)
html = BeautifulSoup(response.text, 'html.parser')

for pergunta in html.select('.s-post-summary.js-post-summary'):
    titulo = pergunta.select_one('.s-link')
    data = pergunta.select_one('.relativetime')
    votos = pergunta.select_one('.s-post-summary--stats-item-number')
    print(f'Titulo da pegunta: {titulo.text}')
    print(f'Data da pegunta: {data.text}')
    print(f'Votos da pegunta: {votos.text}')
    print()
