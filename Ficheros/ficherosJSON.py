import json

ruta1 = 'BigDataPython\data\Cap1\subvenciones.json'
ruta2 = 'BigDataPythonSolucionario\Cap1\subvenciones_esc.json'

with open(ruta1, encoding='utf-8') as fich_lect, open(ruta2, 'w', encoding='utf-8') as fich_escr:
    datos = json.load(fich_lect)

    asoc_str = 'Asociación'
    act_str = 'Actividad Subvencionada'
    imp_str = 'Importe en euros'
    lista = []
    list_act = []
    asoc_actual = ''
    dicc = {}

    for elem in datos:
        asoc = elem[asoc_str]
        act = elem[act_str]
        imp = elem[imp_str]

        if asoc_actual != asoc:
            dicc['Actividades'] = list_act
            list_act = []
            dicc = {'Asociacion': asoc}
            lista.append(dicc)
        
        list_act.append({
            act_str : act,
            imp_str : imp
        })
        asoc_actual = asoc

    json.dump(lista, fich_escr, ensure_ascii=False, indent=4)