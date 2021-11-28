from bs4 import BeautifulSoup
import requests

url = 'https://www.boe.es/informacion/hora_oficial.php'
r = requests.get(url)
print(r)

soup = BeautifulSoup(r.content, 'html.parser')
cajaHora = soup.find('p', class_='centrador')
print(list(cajaHora.children)[0])