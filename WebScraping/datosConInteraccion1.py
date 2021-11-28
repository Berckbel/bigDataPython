from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


#chrome_options = Options()
#chrome_options.add_argument('---headless')
#chrome_options.add_argument('--window-size=1920x1080')

chromedriver = 'misRecursos\chromedriver.exe'
os.environ['webdriver.chrome.driver'] = chromedriver
#driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)
zdriver = webdriver.Chrome(executable_path=chromedriver)

url = 'https://www1.sedecatastro.gob.es/CYCBienInmueble/OVCBusqueda.aspx'
driver.get(url)


ref = driver.find_element_by_id('ctl00_Contenido_txtRC2')

referencia = '38026A035000010000EI'
ref.send_keys(referencia)

datos = driver.find_element_by_id('ctl00_Contenido_btnDatos')
datos.click()


print('------------------------------------------XPATH------------------------------------------')
print('------------------------------------------Componente / ------------------------------------------')
html = driver.find_element_by_xpath('/html')
print(html.text)
head = driver.find_element_by_xpath('/html/head')
body = driver.find_element_by_xpath('/html/body')
print('----------------------------------------HEAD------------------------------------------------')
print(head.text)
print('-----------------------------------------BODY------------------------------------------------')
print(body.text)
print('----------------------------------SEÑALA ELEMENTOS WEBELEMENT--------------------------------------------------')
html2 = body.find_element_by_xpath('/html')
print(html2.text)
print('----------------------------------Componente * --------------------------------------------------')
hijos = driver.find_elements_by_xpath('/html/body/*')
for element in hijos:
    print(element.tag_name)

print('----------------------------------Cuantos div son nietos de body --------------------------------------------------')
divs = driver.find_elements_by_xpath('/html/body/*/div')
print(len(divs))
print('------------------------------------------Componente . ------------------------------------------')
print('----------------------------------Cuantos div son nietos de body --------------------------------------------------')
divs = body.find_elements_by_xpath('./*/div')
print(len(divs))
print('------------------------------------------Componente // ------------------------------------------')
print('----------------------------------Cuantos div estan en body --------------------------------------------------')
divs = driver.find_elements_by_xpath('/html/body//div')
print(len(divs))
print('----------------------------------Todos lo elemento label del documento--------------------------------------------------')
labels = driver.find_elements_by_xpath('//label')
print(len(labels))
print('----------------------------------Encontrar la referecia del contenido inmueble--------------------------------------------------')
id = 'ctl00_Contenido_tblInmueble'
div = driver.find_element_by_id(id)
label = div.find_element_by_xpath('//label')
print(label.text)
print('----------------------------------FILTROS [ ... ]--------------------------------------------------')
e = driver.find_elements_by_xpath(
    '(//label)[position()=5]'
)
print(e[0].text)
print('------------------------------------------------------------------------------------')
e = driver.find_elements_by_xpath(
    '(//label)[5]'
)
print(e[0].text)
print('-------------------------------Notacion python----------------------------------------')
etiqs = driver.find_elements_by_xpath('//label')
print(etiqs[4].text)
print('-------------------------------Ultima etiqueta----------------------------------------')
ulti = driver.find_elements_by_xpath(
    '(//label)[last()]'
)
print(ulti[0].text)
print('-------------------------------Penultima etiqueta----------------------------------------')
penulti = driver.find_elements_by_xpath(
    '(//label)[last()-1]'
)
print(penulti[0].text)
print('-------------------------------Valores concretos para un atrubuto @----------------------------------------')
xpath = '//label[@class="control-label black text-left"]'
etiqs = driver.find_elements_by_xpath(xpath)
print(etiqs[0].text)
print('-------------------------------Consulta mas compleja para valores concretos para un atrubuto @----------------------------------------')
xpath = '//*[./span/text()="Referencia catastral"]//label'
etiq = driver.find_elements_by_xpath(xpath)
print(etiq[0].text)

driver.close()