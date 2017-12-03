import json


def ConfiguracionJson(archivo):

    mapa = None
    with open(archivo) as archivo_json:
        mapa = json.load(archivo_json)

    #print mapa['layers'][0]

    capa = mapa['layers'][0]

    num_filas = capa['height']
    num_col = capa['width']
    linea = capa['data']

    print  num_col, num_filas

    mapa = []
    for i in range(num_filas):
        fila = []
        for j in range(num_col):
            fila.append(0)
        mapa.append(fila)


    k = 0
    for i in range(num_filas):
        for j in range(num_col):
            mapa[i][j] = linea[k]
            k+=1


    #print len(linea)
    #for i in range(len(linea)):
    #    print i/15 , i%15

        #mapa[i/15][i%15] = linea[i]


    #print mapa
    #print len(mapa), len(mapa[0])
    return mapa
