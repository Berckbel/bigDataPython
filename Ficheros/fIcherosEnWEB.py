import requests
import csv
import matplotlib.pyplot as plt


url = 'http://www.mambiente.munimadrid.es/opendata/horario.txt'
resp = requests.get(url)
print(resp)

path = 'BigDataPythonSolucionario\Cap1\ '
with open(path + 'horario.txt', 'wb') as output:
    output.write(resp.content)

with open(path + 'horario.txt') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if (row[0] + row[1] + row[2] == '28079004' and row[3] == '12'):
            plt.title('Oxido de nitrogeno: ' + row[8] + '/' + row[7] + row[6])
            hora = 0
            desp = 9
            vs = []
            horas = []
            while hora <= 23:
                if row[desp + 2 * hora + 1] == 'V':
                    vs.append(row[desp+2*hora])
                    horas.append(hora)
                    hora += 1

                    plt.plot(horas, vs)
                    plt.show()