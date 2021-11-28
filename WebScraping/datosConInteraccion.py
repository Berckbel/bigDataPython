from selenium import webdriver
import os

chromedriver = 'misRecursos\chromedriver.exe'
os.environ['webdriver.chrome.driver'] = chromedriver
driver = webdriver.Chrome(executable_path=chromedriver)

"""
la pagina https://www1.sedecatastro.gob.es/CYCBienInmueble/OVCBusqueda.aspx ha sido modificada 
para que los text input de coordenadas no sean utilizados agno 2020
"""

url = 'https://www1.sedecatastro.gob.es/CYCBienInmueble/OVCBusqueda.aspx'
driver.get(url)

#driver.find_element_by_link_text('COORDENADAS').click()

ref = driver.find_element_by_id('ctl00_Contenido_txtRC2')

referencia = '38026A035000010000EI'
ref.send_keys(referencia)

datos = driver.find_element_by_id('ctl00_Contenido_btnDatos')
datos.click()

#print("Element is visible? " + str(buscar.is_displayed()))


#driver.execute_script('window.history.go(-1)')

html = driver.find_element_by_xpath('/html')

print(html.text)