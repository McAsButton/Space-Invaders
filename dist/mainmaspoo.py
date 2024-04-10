'''Este es el código del día 10 del curso de Python de la Ruta N
    En este código se implementa el juego Space Invaders con programación orientada a objetos
    A pesar de que el curso no lo hace POO
    Se agregan los siguientes elementos:
    - Clase Jugador
    - Clase Bala
    - Clase Enemigo
    - Clase SpaceInvaders
    '''
import os
import random
import math
import io
import pygame
from pygame import mixer

RUTA_10 = '.\\Udemy (Ruta N)\\Python TOTAL\\Día 10' # Ruta de la carpeta del dia 10
os.chdir(RUTA_10)

# La clase "Jugador" representa a un jugador en un juego de Space Invaders, con métodos para moverse
# actualizar y mostrar la imagen del jugador en la pantalla.
class Jugador:
    """
    Esta es una clase que representa una nave espacial en un juego y le permite moverse hacia la
    izquierda y hacia la derecha en la pantalla.
    
    :param space_invaders: El parámetro "space_invaders" es una referencia al objeto 
    SpaceInvaders al que pertenece esta instancia de la clase Ship. Se utiliza para acceder e 
    interactuar con otros componentes del juego, como la pantalla del juego y otros objetos del
    juego
    """
    def __init__(self, space_invaders):

        self.imagen = pygame.image.load('nave.png')
        self.x = 368
        self.y = 526
        self.cambio_x = 0
        self.space_invaders = space_invaders

    def mover(self, evento):
        """
        La función "mover" se utiliza para manejar eventos de teclado y actualizar el valor de
        "cambio_x" en consecuencia.
        
        :param evento: El parámetro "evento" es un objeto que representa un evento de pygame. Se 
        utiliza para manejar eventos de teclado en este código
        """
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                self.cambio_x = -1
            elif evento.key == pygame.K_RIGHT:
                self.cambio_x = 1
        if evento.type == pygame.KEYUP:
            if evento.key in (pygame.K_LEFT, pygame.K_RIGHT):
                self.cambio_x = 0

    def actualizar(self):
        """
        La función "actualizar" actualiza el valor de "self.x" agregando "self.cambio_x" y asegura 
        que "self.x" se mantenga dentro del rango de 0 a 736.
        """
        self.x += self.cambio_x
        if self.x < 0:
            self.x = 0
        elif self.x > 736:
            self.x = 736

    def mostrar(self, pantalla):
        """
        La función "mostrar" toma un parámetro "pantalla" y muestra la imagen en las coordenadas
        especificadas en la pantalla.
        
        :param pantalla: El parámetro "pantalla" representa la pantalla o superficie donde se 
        mostrará la imagen. Suele ser un objeto Surface de pygame
        """
        pantalla.blit(self.imagen, (self.x, self.y))

class Bala:
    """
    Esta es una clase que representa una bala en un juego, con métodos para disparar, actualizar 
    su posición y mostrarla en pantalla.
    """
    def __init__(self):
        self.imagen = pygame.image.load('bullet.png')
        self.x = 0
        self.y = 526
        self.cambio_y = -3
        self.visible = False

    def disparar(self, jugador):
        """
        La función "disparar" establece que las coordenadas de un objeto estén ligeramente 
        desplazadas de las coordenadas de un objeto del jugador y hace que el objeto sea visible.
        
        :param jugador: El parámetro "jugador" representa una instancia de un objeto jugador
        """
        self.x = jugador.x + 20
        self.y = jugador.y
        self.visible = True

    def actualizar(self):
        """
        La función actualiza la coordenada y de un objeto y establece su visibilidad en Falso si cae 
        por debajo de un cierto umbral.
        """
        if self.y <= -64:
            self.visible = False
        self.y += self.cambio_y

    def mostrar(self, pantalla):
        """
        La función "mostrar" muestra una imagen en una pantalla determinada si está configurada para
        ser visible.
        
        :param pantalla: El parámetro "pantalla" representa la superficie o pantalla donde se 
        mostrará la imagen. Suele ser un objeto Surface de pygame
        """
        if self.visible:
            pantalla.blit(self.imagen, (self.x + 20, self.y + 10))

class Enemigo:
    """
    Esta es una clase que representa a un enemigo en un juego de Space Invaders, con métodos 
    para actualizar su posición, mostrarla en la pantalla y verificar si hay colisiones con el 
    jugador.
    
    :param space_invaders: El parámetro "space_invaders" es una referencia al objeto principal 
    del juego Space Invaders. Se utiliza para acceder e interactuar con otros componentes del 
    juego, como la nave espacial del jugador y la pantalla del juego
    """
    def __init__(self, space_invaders):
        self.imagen = pygame.image.load('enemigo.png')
        self.x = random.randint(0, 736)
        self.y = 50
        self.cambio_x = 0.7
        self.cambio_y = 50
        self.space_invaders = space_invaders

    def actualizar(self):
        """
        La función actualiza la posición de un objeto incrementando su coordenada x y cambiando la
        dirección si alcanza los límites.
        """
        self.x += self.cambio_x
        if self.x <= 0:
            self.cambio_x = 0.7
            self.y += self.cambio_y
        elif self.x >= 736:
            self.cambio_x = -0.7
            self.y += self.cambio_y

    def mostrar(self, pantalla):
        """
        La función "mostrar" toma un parámetro "pantalla" y muestra la imagen en las coordenadas
        especificadas en la pantalla.
        
        :param pantalla: El parámetro "pantalla" representa la pantalla o superficie donde se 
        mostrará la imagen. Suele ser un objeto Surface de pygame
        """
        pantalla.blit(self.imagen, (self.x, self.y))

    def hay_colision(self, jugador):
        """
        La función comprueba si hay una colisión entre dos objetos en función de sus coordenadas.
        
        :param jugador: El parámetro "jugador" representa un objeto o instancia de un jugador en el
        juego
        :return: un valor booleano. Si la distancia entre el objeto (yo) y el jugador (jugador) es 
        menor a 27, devuelve Verdadero indicando una colisión. De lo contrario, devuelve False 
        indicando que no hay colisión.
        """
        distancia = math.sqrt((math.pow(self.x - jugador.x, 2)) + (math.pow(self.y - jugador.y, 2)))
        if distancia <= 26:
            valor = True
        else:
            valor = False
        return valor

class SpaceInvaders:
    """
    El código anterior es una implementación en Python de un juego de Space Invaders.
    """
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Space Invaders MAS")
        icono = pygame.image.load('icon.png')
        pygame.display.set_icon(icono)
        self.fondo = pygame.image.load('fondo.png')
        self.jugador = Jugador(self.pantalla)
        self.enemigos = [Enemigo(self.pantalla) for _ in range(6)]
        self.fuente_como_bytes = self.fuente_bytes('PressStart2P-Regular.ttf')
        self.fuente = pygame.font.Font(self.fuente_como_bytes, 32)
        #self.fuente = pygame.font.Font('PressStart2P-Regular.ttf', 32)
        self.mixer_init()
        self.variables_init()

    def mixer_init(self):
        """
        La función inicializa el módulo mezclador en pygame, carga un archivo de música de fondo,
        establece el volumen en 0,1 y reproduce la música en bucle.
        """
        mixer.music.load('MusicaFondo.mp3')
        mixer.music.set_volume(0.1)
        mixer.music.play(-1)
    def variables_init(self):
        """
        La función inicializa las variables del juego.
        """
        self.texto_x = 10
        self.texto_y = 10
        self.se_ejecuta = True
        self.game_over = False  # Agregar atributo game_over
        self.victoria = False
        self.puntaje = 0
        self.balas = []

    def fuente_bytes(self, fuente):
        with open(fuente, 'rb') as f:
            ttf_bytes = f.read()
        return io.BytesIO(ttf_bytes)

    def mostrar_puntaje(self):
        """
        La función "mostrar_puntaje" renderiza y muestra la puntuación actual en la pantalla.
        """
        puntaje_mostrar = self.fuente.render(f'Puntaje: {self.puntaje}', True, (255, 255, 255))
        self.pantalla.blit(puntaje_mostrar, (self.texto_x, self.texto_y))

    def mostrar_game_over(self):
        """
        La función "mostrar_game_over" muestra el texto "GAME OVER" en la pantalla usando una fuente 
        y posición específicas.
        """
        fuente_final = pygame.font.Font(self.fuente_como_bytes, 64)
        mi_fuente_final = fuente_final.render('GAME OVER', True, (255, 255, 255))
        self.pantalla.blit(mi_fuente_final, (125, 250))

    def mostrar_victoria(self):
        """
        La función "mostrar_victoria" muestra la palabra "VICTORIA" en pantalla usando una fuente y
        posición específica.
        """
        fuente_victoria = pygame.font.Font(self.fuente_como_bytes, 64)
        mi_fuente_victoria = fuente_victoria.render('VICTORIA', True, (255, 255, 255))
        self.pantalla.blit(mi_fuente_victoria, (150, 250))

    def hay_colision(self, x1, y1, x2, y2):
        """
        La función "hay_colision" calcula la distancia entre dos puntos (x1, y1) y (x2, y2) y 
        devuelve True si la distancia es menor que 27, lo que indica una colisión.
        
        :param x1: La coordenada x del primer objeto
        :param y1: El parámetro `y1` representa la coordenada y del primer punto
        :param x2: El parámetro x2 representa la coordenada x del segundo punto
        :param y2: El parámetro `y2` representa la coordenada y del segundo punto
        :return: un valor booleano que indica si hay una colisión o no.
        """
        distancia = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))
        return distancia < 27

    def main_loop(self):
        """
        La función main_loop es el bucle principal del juego que maneja eventos, actualiza los 
        objetos del juego y los muestra en la pantalla.
        """
        while self.se_ejecuta:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.se_ejecuta = False
                self.jugador.mover(evento)
                if not self.game_over:
                    if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                        nueva_bala = Bala()
                        nueva_bala.disparar(self.jugador)
                        sonido_disparo = mixer.Sound('disparo.mp3')
                        sonido_disparo.set_volume(0.2)
                        sonido_disparo.play()
                        self.balas.append(nueva_bala)

            self.jugador.actualizar()
            for enemigo in self.enemigos:
                enemigo.actualizar()

            self.pantalla.blit(self.fondo, (0, 0))

            for enemigo in self.enemigos:
                if enemigo.hay_colision(self.jugador):
                    self.game_over = True
                    self.mostrar_game_over()

            if not self.game_over:
                for bala in self.balas:
                    bala.actualizar()
                    bala.mostrar(self.pantalla)
                    if not bala.visible:
                        self.balas.remove(bala)

                self.jugador.mostrar(self.pantalla)
                for enemigo in self.enemigos:
                    enemigo.mostrar(self.pantalla)

                for enemigo in self.enemigos:
                    for bala in self.balas:
                        if bala.visible:
                            colision_bala_enemigo = self.hay_colision(enemigo.x, enemigo.y, bala.x,
                                                                      bala.y)
                            if colision_bala_enemigo:
                                sonido_colision = mixer.Sound('Golpe.mp3')
                                sonido_colision.set_volume(0.2)
                                sonido_colision.play()
                                bala.visible = False
                                self.puntaje += 1
                                enemigo.x = random.randint(0, 736)
                                enemigo.y = 50
                                if self.puntaje >= 30:
                                    self.game_over = True
                                    self.victoria = True
                                    self.enemigos.clear()

            self.mostrar_puntaje()

            if self.game_over:
                if self.victoria:
                    self.mostrar_victoria()
                else:
                    self.mostrar_game_over()

            pygame.display.update()

    def ejecutar(self):
        """
        La función ejecuta el bucle principal de un programa pygame y luego sale de pygame.
        """
        self.main_loop()
        pygame.quit()

if __name__ == "__main__":
    juego = SpaceInvaders()
    juego.ejecutar()
