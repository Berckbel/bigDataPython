from bs4 import BeautifulSoup

url = 'misRecursos\mini.html'
with open(url, 'r') as f:
    page = f.read()

soup = BeautifulSoup(page, 'html.parser')
print('------------------------------Navegacion Absoluta---------------------------------------')
print(soup.prettify())

hijosDoc = list(soup.children)
print('----------------------------------------------------------------------------------------')
print([type(item) for item in hijosDoc])
print('----------------------------------------------------------------------------------------')
print(hijosDoc)

html = hijosDoc[2]
print('----------------------------------------------------------------------------------------')
print(list(html.children))

body = list(html.children)[3]
print('----------------------------------------------------------------------------------------')
print(list(body.children))
print('----------------------------------------------------------------------------------------')
divDate = list(body.children)[1]
print('----------------------------------------------------------------------------------------')
print(divDate.get_text())

print('--------------------------------Navegacion Relativa--------------------------------------')
divs = soup.find_all('div')

print(divs[0].get_text())

print(soup.find('div').get_text())

print(soup.find('div', id='date').get_text())

print(soup.select('html div')[0].get_text())