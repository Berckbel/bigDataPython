import csv

ruta = 'BigDataPython\data\Cap1\subvenciones.csv'

with open(ruta, encoding='latin1') as fichero_csv:
    lector = csv.reader(fichero_csv)
    next(lector, None) #se salta la cabecera
    importe_total = 0
    for linea in lector:
        importe_str = linea[2]
        importe = float(importe_str)
        importe_total = importe_total + importe
    print(importe_total)

with open(ruta, encoding='latin1') as fichero_csv:
    dict_lector = csv.DictReader(fichero_csv)
    asocs = {}
    for linea in dict_lector:
        centro = linea['Asociación']
        subvencion = float(linea['Importe'])
        if centro in asocs:
            asocs[centro] = asocs[centro] + subvencion
        else:
            asocs[centro] = subvencion
    print(asocs)

#----------------------------------------------------------------------------------------------------

#import csv

ruta1 = 'BigDataPython\data\Cap1\subvenciones.csv'
ruta2 = 'BigDataPythonSolucionario\Cap1\subvenciones_esc.csv'

with open(ruta1, encoding='latin1') as fich_lect, open(ruta2, 'w', encoding='latin1') as fich_escr:
    dict_lector = csv.DictReader(fich_lect)

    campos = dict_lector.fieldnames + ['Justificacion requerida', 'Justificacion recibida']
    escritor = csv.DictWriter(fich_escr, fieldnames=campos)

    escritor.writeheader()
    for linea in dict_lector:
        if float(linea['Importe']) > 300:
            linea['Justificacion requerida'] = "Si"
        else:
            linea['Justificacion requerida'] = "No"
        linea['Justificacion recibida'] = "No"

        escritor.writerow(linea)