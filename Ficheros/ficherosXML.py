import xml.etree.ElementTree as ET

ruta = 'BigDataPython\data\Cap1\subvenciones.xml'
ruta1 = 'BigDataPythonSolucionario\Cap1\subvenciones_esc.xml'

arbol = ET.parse(ruta)
raiz = arbol.getroot()
asocs = {}

for fila in raiz:
    centro = fila[0].text
    subvencion = float(fila[2].text)
    if centro in asocs:
        asocs[centro] = asocs[centro] + subvencion
    else:
        asocs[centro] = subvencion

print(asocs)

#------------------------------------------------------------------------------------------------------

tree = ET.parse(ruta)
root = tree.getroot()


nuevo = ET.ElementTree()
raiz_nueva = ET.Element('Raiz')
nuevo._setroot(raiz_nueva)

elem_actual = ET.Element('Asociacion')
asoc_actual = ''
actividades = ET.SubElement(elem_actual, 'Actividades')
gasto = 0

for fila in root.findall('Row'):
    asoc = fila.find('Asociaci_n').text
    act = fila.find('Actividad_Subvencionada').text
    imp = float(fila.find('Importe').text)

    if asoc_actual != asoc:
        gas_total = ET.SubElement(elem_actual, 'Total')
        gas_total.text = str(gasto)
        elem_actual = ET.SubElement(raiz_nueva, 'Asociacion')
        elem_actual.set('nombre', asoc)
        actividades = ET.SubElement(elem_actual, 'Actividades')
        gasto = 0

    act_elem = ET.SubElement(actividades, 'Actividad')
    nom_elem = ET.SubElement(act_elem, 'Nombre')
    nom_elem.text = act
    imp_elem = ET.SubElement(act_elem, 'Subvencion')
    imp_elem.text = str(imp)
    gasto = gasto + imp
    asoc_actual = asoc

nuevo.write(ruta1)
