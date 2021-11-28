import csv

ruta1 = 'BigDataPython\data\Cap1\subvenciones.csv'
ruta2 = 'BigDataPythonSolucionario\Cap1\subvenciones_esc.tsv'

with open(ruta1, encoding='latin1') as fich_lect, open(ruta2, 'w', encoding='latin1') as fich_escr:
    dict_lector = csv.DictReader(fich_lect)
    campos = dict_lector.fieldnames
    escritor = csv.DictWriter(fich_escr, delimiter='\t', fieldnames=campos)
    escritor.writeheader()
    for linea in dict_lector:
        escritor.writerow(linea)

with open(ruta2, encoding='latin1') as  fich:
    dict_lector = csv.DictReader(fich, delimiter='\t')
    asocs = {}
    for linea in dict_lector:
        centro = linea['Asociación']
        subvencion = float(linea['Importe'])
        if centro in asocs:
            asocs[centro] = asocs[centro] + subvencion
        else:
            asocs[centro] = subvencion
    print(asocs)