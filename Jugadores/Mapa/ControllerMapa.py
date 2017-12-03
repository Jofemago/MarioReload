
import pygame
from MapaNivel1 import *


class MakeMapa:

    def __init__(self,mapa, sabana,suelos,general):

        self.mapa = mapa
        self.sabana = sabana
        self.filas = len(self.mapa)
        self.col = len(self.mapa[0])
        self.suelos = suelos
        self.general = general
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
