import pygame


ALTO = 700
ANCHO = 700
CENTRO = [ANCHO/2,ALTO/2]

BLANCO = [255,255,255]
NEGRO = [0,0,0]
ROJO = [255,0,0]
VERDE = [0,255,0]
AZUL = [0,0,255]



def cut(archivo, an , al):
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


class Peach(pygame.sprite.Sprite):

    def __init__(self,imgSprite):
        pygame.sprite.Sprite.__init__(self)
        self.m = imgSprite
        self.image = self.m[0][0]
        self.rect = self.image.get_rect()
        self.dir = 0
        self.i = 0
        self.dx = 0
        self.dy = 0

    def update(self):
        if self.dx != 0 or self.dy != 0 or self.dir == 2 or self.dir == 3:
            if self.i < 3:
                self.i += 1
            else:
                self.i = 0
        self.image = self.m[self.i][self.dir]
        if self.rect.right <= ANCHO and self.rect.left >= 0:
            self.rect.x += self.dx

        if self.rect.right >= ANCHO and self.dx < 0:
            self.rect.x += self.dx

        if self.rect.left <= 0 and self.dx > 0:
            self.rect.x += self.dx

        if self.rect.top >= 0 and self.rect.bottom <= ALTO:
            self.rect.y += self.dy

        if self.rect.top <= 0 and self.dy > 0:
            self.rect.y += self.dy

        if self.rect.bottom >= ALTO and self.dy < 0:
            self.rect.y += self.dy




        self.gravity()


    def gravity(self):

        if self.dy >= 0:
            self.dy += 1.5

        if self.rect.bottom >= ALTO:
            self.dy = 0
            self.rect.bottom = ALTO


if (__name__ == '__main__'):
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    pygame.display.flip()
    jugadores = pygame.sprite.Group()
    cuts = cut('Imagenes/Peach/peach.png',4,4)
    jugador = Peach(cuts)
    jugador.rect.x = CENTRO[0]
    jugador.rect.y = CENTRO[1]
    jugadores.add(jugador)
    clock = pygame.time.Clock()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    jugador.dir = 1
                    jugador.dx = -5

                if event.key == pygame.K_RIGHT:
                    jugador.dir = 0
                    jugador.dx = 5

                if event.key == pygame.K_UP:
                    jugador.dy = -5

                if event.key == pygame.K_SPACE:
                    if jugador.dir == 0:
                        jugador.dir = 2

                    if jugador.dir == 1:
                        jugador.dir = 3


            if event.type == pygame.KEYUP:

                jugador.dx = 0
                jugador.dy = 0


        jugadores.update()
        pantalla.fill(NEGRO)
        jugadores.draw(pantalla)
        pygame.display.flip()
        clock.tick(30)
