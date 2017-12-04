'''
en este archivo se almacenaran todas las caracteristicas de la pantalla, como los colores ancho y alto

'''
import pygame
import json


ANCHO=800
ALTO=600
BLANCO=(255,255,255)
NEGRO=(0,0,0)
ROJO=(255,0,0)
AZUL=(0,0,255)
VERDE=(0,255,0)

CENTRO = (ANCHO//2,ALTO//2)


def recortar(archivo, an , al):
    fondo = pygame.image.load(archivo).convert_alpha()
    info = fondo.get_size()
    img_ancho = info[0]  #alto y ancho de cada sprite
    img_alto = info[1]
    corte_x = img_ancho /an
    corte_y = img_alto/al

    m = []
    for i in range(an):
        fila = []
        for j in range(al):
            cuadro = [i*corte_x,j*corte_y,corte_x,corte_y]
            recorte = fondo.subsurface(cuadro)
            fila.append(recorte)
        m.append(fila)

    return m


def crearArreglo(fila, columnas):

    """Funcion que crea un arreglo"""
    arreglo = []
    for i in range(fila):
        fila = []
        for j in range(columnas):
            fila.append(0)
        arreglo.append(fila)
    return arreglo

def ConfiguracionJson(archivo):

    mapa = None
    with open(archivo) as archivo_json:
        mapa = json.load(archivo_json)

    #print mapa['layers'][0]

    capa = mapa['layers'][0]

    num_filas = capa['height']
    num_col = capa['width']
    linea = capa['data']

    #print  num_col, num_filas

    mapa = crearArreglo(num_filas, num_col)



    k = 0
    for i in range(num_filas):
        for j in range(num_col):
            mapa[i][j] = linea[k]
            k+=1

    return mapa
