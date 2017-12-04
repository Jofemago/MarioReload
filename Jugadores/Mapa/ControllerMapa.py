
import pygame
from MapaNivel1 import *


class MakeMapa:

    def __init__(self,mapa, sabana,suelos,fondos,general):

        self.mapa = mapa
        print mapa
        self.sabana = sabana
        self.filas = len(self.mapa)
        self.col = len(self.mapa[0])
        self.suelos = suelos#controlar donde el personaje solo puede pisar
        self.fondos = fondos #se guardaran los fonsdos aqui
        self.general = general#controlatodo
        print self.filas, self.col

    def dibujarmapa(self):


        for i in range(self.filas):
            for j in range(self.col):

                #se dibujan suelos
                if self.mapa[i][j] == 1 :
                    m = suelo(self.sabana[0][0])
                    m.setpos(j*40 , i*40)
                    self.suelos.add(m)
                    self.general.add(m)



                #TERCER NIVEL
                #Suelo
                if self.mapa[i][j] == 91:

                    m = suelo(self.sabana[0][9])
                    m.setpos(j*40 , i*40)
                    self.suelos.add(m)
                    self.general.add(m)

                #Pinta los fondos
                if self.mapa[i][j] == 92:

                    m = suelo(self.sabana[1][9])
                    m.setpos(j*40 , i*40)
                    self.fondos.add(m)
                    self.general.add(m)

                #Base del tercer mundo
                if self.mapa[i][j] == 94:

                    m = suelo(self.sabana[3][9])
                    m.setpos(j*40 , i*40)
                    self.suelos.add(m)
                    self.general.add(m)

                if self.mapa[i][j] == 95:

                    m = suelo(self.sabana[4][9])
                    m.setpos(j*40 , i*40)
                    self.suelos.add(m)
                    self.general.add(m)

                if self.mapa[i][j] == 96:

                    m = suelo(self.sabana[5][9])
                    m.setpos(j*40 , i*40)
                    self.suelos.add(m)
                    self.general.add(m)

                if self.mapa[i][j] == 97:

                    m = suelo(self.sabana[6][9])
                    m.setpos(j*40 , i*40)
                    self.suelos.add(m)
                    self.general.add(m)

                if self.mapa[i][j] == 98:

                    m = suelo(self.sabana[7][9])
                    m.setpos(j*40 , i*40)
                    self.suelos.add(m)
                    self.general.add(m)

                if self.mapa[i][j] == 99:

                    m = suelo(self.sabana[8][9])
                    m.setpos(j*40 , i*40)
                    self.suelos.add(m)
                    self.general.add(m)
