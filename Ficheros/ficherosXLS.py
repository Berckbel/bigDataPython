import xlrd
import xlwt

ruta = 'BigDataPython\data\Cap1\subvenciones.xls'
ruta2 = 'BigDataPythonSolucionario\Cap1\subvenciones_esc.xls'

with xlrd.open_workbook(ruta) as libro:
    asocs = {}

    for hoja in libro.sheets():

        for i in range(1,hoja.nrows):
            fila = hoja.row(i)

            asoc = fila[0].value
            subvencion = fila[2].value
            if asoc in asocs:
                asocs[asoc] = asocs[asoc] + subvencion
            else:
                asocs[asoc] = subvencion

    print(asocs)

with xlrd.open_workbook(ruta) as libro_lect:
    asocs = {}

    libro_escr = xlwt.Workbook()

    for nombre in libro_lect.sheet_names():
        hoja_lect = libro_lect.sheet_by_name(nombre)
        hoja_escr = libro_escr.add_sheet(nombre)

        for i in range(hoja_lect.nrows):
            for j in range(hoja_lect.ncols):
                valor = hoja_lect.cell(i,j).value
                hoja_escr.write(i, j, valor)

            if i != 0:
                fila = hoja_lect.row(i)
                centro = fila[0].value
                sub = fila[2].value
                if centro in asocs:
                    asocs[centro] = asocs[centro] + sub
                else:
                    asocs[centro] = sub

    hoja_escr = libro_escr.add_sheet('Totales')
    hoja_escr.write(0, 0, "Asociacion")
    hoja_escr.write(0, 1, "Importe total")
    hoja_escr.write(0, 2, "Importe justificado")
    hoja_escr.write(0, 3, "Restante")

    for i, clave in enumerate(asocs):
        fila = i + 1
        hoja_escr.write(fila, 0, clave)
        hoja_escr.write(fila, 1, asocs[clave])
        hoja_escr.write(fila, 2, 0)

        fila_form = i + 2
        fform_str = str(fila_form)
        form = "C" + fform_str + "-B" + fform_str
        hoja_escr.write(fila, 3, xlwt.Formula(form))
    
    libro_escr.save(ruta2)