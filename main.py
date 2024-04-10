'''
Este codigo es para el jugo de Space Invaders que se realizara en el curso de Python Total de Udemy 
(Ruta N) en la clase 10, se realiza a medida que da los conceptos de clase, por lo que no hay mas 
ejercicios como en los dias anteriores.
requiere pip install pygame
'''
import os # Para poder usar el path de la imagen
import random # Para generar numeros aleatorios
import math # Para usar la funcion sqrt para distancia entre puntos
import pygame # Para poder usar pygame
from pygame import mixer # Para poder usar sonidos
RUTA_10 = 'D:\\Miguel\\ITM\Programación Avanzada\\Space Invaders' # Ruta de la carpeta del dia 10
os.chdir(RUTA_10) # Cambiamos el directorio de trabajo a la carpeta del dia 10
#La importacion os y sus modulos no hacen parte del curso, lo hago para poder trabajar con la
# carpeta del dia 10 como directorio activo y no tener que usar la ruta cada vez que requiera
# una imagen o archivo de sonido


# Inicializar pygame
pygame.init()

# Establecer el tamaño de la ventana
pantalla = pygame.display.set_mode((800, 600)) # Tamaño de la ventana

# Titulo, Icono y Fondo
pygame.display.set_caption("Space Invaders MAS") # Titulo de la ventana
icono = pygame.image.load('icon.png') # Cargamos el icono en una variable
pygame.display.set_icon(icono) # Icono de la ventana
fondo = pygame.image.load('fondo.png') # Cargamos el fondo en una variable

# Agregar musica
mixer.music.load('MusicaFondo.mp3') # Cargamos la musica de fondo en una variable
mixer.music.set_volume(0.1) # Establecemos el volumen de la musica de fondo
mixer.music.play(-1) # Reproducimos la musica de fondo en un loop infinito

#Variables del Jugador
img_jugador = pygame.image.load('nave.png') # Cargamos la imagen de la nave en una variable
jugadorX = 368 # Posicion inicial en X de la nave (800/2 - 64/2) = 368 (centrado)
jugadorY = 526 # Posicion inicial en Y de la nave (600 - 64 - 10) = 526 (abajo con un margen de 10)
jugadorX_cambio = 0 # Variable para el cambio de posicion en X de la nave

#Variables de la bala
balas = [] # Creamos una lista de balas para poder disparar mas de una bala
img_bala = pygame.image.load('bullet.png') # Cargamos la imagen de la bala en una variable
balaX = 0 # Posicion inicial en X de la bala
balaY = 526 # Posicion inicial en Y de la bala
balaX_cambio = 0 # Variable para el cambio de posicion en X de la bala
balaY_cambio = -3 # Variable para el cambio de posicion en Y de la bala
bala_visible = False # Variable para saber si la bala esta visible o no

#Variables del enemigo 
img_enemigo = [] # Cargamos la imagen del enemigo en una variable
enemigoX = [] # Posicion inicial en X del enemigo (aleatorio entre 0 y 736)
enemigoY = [] # Posicion inicial en Y del enemigo
enemigoX_cambio = [] # Variable para el cambio de posicion en X del enemigo
enemigoY_cambio = [] # Variable para el cambio de posicion en Y del enemigo
cantidad_enemigos = 6 # Cantidad de enemigos

#Puntaje
puntaje = 0 # Variable para el puntaje
fuente = pygame.font.Font('PressStart2P-Regular.ttf', 32) # Cargamos la fuente en una variable
textoX = 10 # Posicion inicial en X del texto del puntaje
textoY = 10 # Posicion inicial en Y del texto del puntaje

#Texto final
fuente_final = pygame.font.Font('PressStart2P-Regular.ttf', 64) # Cargamos la fuente en una variable

# Funcion para mostrar el puntaje en pantalla
def mostrar_puntaje(x, y):
    puntaje_mostrar = fuente.render(f'Puntaje: {puntaje}', True, (255, 255, 255)) # Cargamos el texto en una variable 
    pantalla.blit(puntaje_mostrar, (x, y)) # Mostramos el texto en pantalla

# Funcion para mostrar los enemigos en pantalla
for e in range(cantidad_enemigos): # Para cada enemigo
    img_enemigo.append(pygame.image.load('enemigo.png')) # Cargamos la imagen del enemigo en una variable
    enemigoX.append(random.randint(0, 736)) # Posicion inicial en X del enemigo (aleatorio entre 0 y 736)
    enemigoY.append(50) # Posicion inicial en Y del enemigo
    enemigoX_cambio.append(0.7) # Variable para el cambio de posicion en X del enemigo
    enemigoY_cambio.append(40) # Variable para el cambio de posicion en Y del enemigo

# Funcion para mostrar al jugador en pantalla
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y)) # Mostramos la imagen del jugador en pantalla

# Funcion para mostrar al enemigo en pantalla
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y)) # Mostramos la imagen del enemigo en pantalla

# Funcion para mostrar la bala en pantalla
def disparar_bala(x, y):
    global bala_visible # Variable global para saber si la bala esta visible o no
    bala_visible = True # La bala esta visible
    pantalla.blit(img_bala, (x + 20, y + 10)) # Mostramos la imagen de la bala en pantalla

# Funcion para detectar colisiones
def hay_colision(x_1,y_1,x_2,y_2):
    distancia = math.sqrt((math.pow(x_1-x_2,2))+(math.pow(y_1-y_2,2))) # Formula de distancia
    if distancia < 27: # Si la distancia es menor a 27
        return True # Hay colision
    else: # Si la distancia es mayor a 27
        return False # No hay colision
    
# Funcion para mostrar el texto final
def Texto_Final():
    mi_fuente_final = fuente_final.render('GAME OVER', True, (255, 255, 255)) # Cargamos el texto en una variable
    pantalla.blit(mi_fuente_final, (125, 250)) # Mostramos el texto en pantalla


# Loop del juego
se_ejecuta = True
while se_ejecuta:
    # 'Todo lo que necesito que se actualice dentro del juego debe ir dentro del loop del juego
    pantalla.blit(fondo, (0,0)) # imagen de fondo de la ventana, al iniciar no se ve a menos que
    # actualicemos la pantalla es lo primero que debemos cambiar ya que si lo ponemos luego de
    # poner otra figura, esta se va a ver por encima

    #Iterar eventos
    for evento in pygame.event.get():
        #Evento para cerrar la ventana
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        #Evento presionar teclas
        if evento.type == pygame.KEYDOWN: # Si se presiona una tecla
            if evento.key == pygame.K_LEFT: # Si la tecla presionada es la flecha izquierda
                jugadorX_cambio = -1 # Cambio de posicion en X de la nave
            if evento.key == pygame.K_RIGHT: # Si la tecla presionada es la flecha derecha
                jugadorX_cambio = 1 # Cambio de posicion en X de la nave
            if evento.key == pygame.K_SPACE:
                sonidodisparo = mixer.Sound('disparo.mp3')
                sonidodisparo.set_volume(0.2)
                sonidodisparo.play()
                nueva_bala = {
                    'x': jugadorX, # Posicion en X de la bala
                    'y': jugadorY, # Posicion en Y de la bala
                    'velocidad': balaY_cambio # Velocidad de la bala
                }
                balas.append(nueva_bala) # Agregamos la bala a la lista de balas

        #Evento soltar teclas
        if evento.type == pygame.KEYUP: # Si se deja de presionar una tecla
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT: # Si la tecla es una
                # flecha
                jugadorX_cambio = 0 # Cambio de posicion en X de la nave

    #Modificar informacion del jugador
    jugadorX += jugadorX_cambio # Cambio de posicion en X de la nave

    # Limitar movimiento de la nave para que no se salga de la pantalla
    if jugadorX <= 0: # Si la posicion en X de la nave es menor o igual a 0
        jugadorX = 0 # La posicion en X de la nave es 0
    elif jugadorX >= 736: # Si la posicion en X de la nave es mayor o igual a 736
        jugadorX = 736 # La posicion en X de la nave es 736

    #Modificar informacion del enemigo
    for e in range(cantidad_enemigos): # Para cada enemigo

        # Detectar colisiones entre el enemigo y la nave
        if enemigoY[e] > 526:
            for k in range(cantidad_enemigos): # Para cada enemigo
                enemigoY[k] = 1000 # La posicion en Y del enemigo es 1000
            Texto_Final()
            break

        enemigoX[e] += enemigoX_cambio[e] # Cambio de posicion en X del enemigo
        # Limitar movimiento del enemigo para que no se salga de la pantalla
        if enemigoX[e] <= 0: # Si la posicion en X del enemigo es menor o igual a 0
            enemigoX_cambio[e] = 0.7 # El cambio de posicion en X del enemigo es 0.3
            enemigoY[e] += enemigoY_cambio[e] # El cambio de posicion en Y del enemigo es 40
        elif enemigoX[e] >= 736: # Si la posicion en X del enemigo es mayor o igual a 736
            enemigoX_cambio[e] = -0.7 # El cambio de posicion en X del enemigo es -0.3
            enemigoY[e] += enemigoY_cambio[e] # El cambio de posicion en Y del enemigo es 40
        # Detectar colisiones
        for bala in balas: # Para cada bala
            colision_bala_enemigo = hay_colision(enemigoX[e], enemigoY[e], bala['x'], bala['y']) # Llamamos a la funcion hay_colision
            if colision_bala_enemigo: # Si hay colision
                sonidocolision = mixer.Sound('Golpe.mp3')
                sonidocolision.set_volume(0.2)
                sonidocolision.play() # Sonido de colision
                balas.remove(bala) # Eliminamos la bala de la lista de balas
                puntaje += 1 # Aumentamos el puntaje en 1
                enemigoX[e] = random.randint(0, 736) # Posicion inicial en X del enemigo (aleatorio entre 0 y 736)
                enemigoY[e] = 50 # Posicion inicial en Y del enemigo
                break # Salimos del for
        # Llamamos a la funcion enemigo para que muestre al enemigo en pantalla
        enemigo(enemigoX[e], enemigoY[e], e)

    #Movimiento de la bala
    for bala in balas: # Para cada bala
        bala['y'] += bala['velocidad'] # Cambio de posicion en Y de la bala
        pantalla.blit(img_bala, (bala['x'] + 20, bala['y'] + 10)) # Mostramos la imagen de la bala en pantalla

        if bala['y'] <= -64: # Si la posicion en Y de la bala es menor o igual a -64
            balas.remove(bala) # Eliminamos la bala de la lista de balas



    

    # Llamamos a la funcion jugador para que muestre al jugador en panatalla
    jugador(jugadorX, jugadorY)
    #mostrar puntae en pantalla
    mostrar_puntaje(textoX, textoY)



    # Actualizar la pantalla
    pygame.display.update() # Actualizamos la pantalla













#En la case 1: Crear pantalla se realizo el codigo para la ventana, y se explica la forma de que no
# se cierre automaticamente, sino que espera el evento QUIT de pygame para que se cierre.
#En la clase 2: Cambiar Titulo, Icono y Color, se cambio el icono de la ventana, el titulo y el
# color de fondo.
#En la clase 3: Agregar al protagonista (nave) se agrego la imagen de la nave y se la hizo aparecer
# en pantalla.
#En la clase 4: Mover al personaje se explica como es el procedimiento para movel al jugador,
# sin embargo, no se agrego la funcionalidad de mover la nave con las flechas del teclado.
#En la clase 5: Controlar el movimiento, se agrego la funcionalidad de mover la nave con las
# flechas del teclado.
#En la clase 6: Limitar el movimiento, se agrego la funcionalidad de limitar el movimiento de la
# nave para que no se salga de la pantalla.
#En la clase 7: Crear Enemigos se agrego la imagen del enemigo y se la hizo aparecer en pantalla.
#En la clase 8: Generar Movimientos del Enemigo se agrego la funcionalidad de mover al enemigo
#En la clase 9: Agregar imagen de fondo se agrego la imagen de fondo y se la hizo aparecer en
# pantalla.
#En la clase 10: Disparar balas se agrego la funcionalidad de disparar balas con la barra espaciadora
#En la clase 11: Movimiento de la bala se resuelven dos problemas que teniamos (solo existe una bala 
# (se arregle reiniciando la posicion de la bala una vez que sale de la pantalla) y esta se mueve
# depende de donde esta la nave (se modifica el evento de la barra espaciadora para que no dependa
# de la posicion de la nave, ademas se valida que la bala sea visible o no para que no se mueva de su
# posicion x hasta que desaparaezca de la pantalla))
#En la clase 12: Detectar coliisiones se agrega la funcionalidad de detectar colisiones entre la bala
# y el enemigo con la formula de distancia entre puntos (geometria vectorial), y se agrega la
# funcionalidad de que el enemigo reaparezca en una posicion aleatoria
#En la clase 13: Agregar enemigos, se agrega la funcionalidad de que aparezcan varios enemigos
#En la clase 14: Agregar puntaje, se agrega la funcionalidad de que el puntaje aumente cuando se
# dispara a un enemigo
#En la clase 15: Agregar musica y sonidos, se agrega la funcionalidad de que suene musica de fondo
# y sonidos cuando se dispara y cuando se destruye un enemigo
#En la clase 16: Terminar el juego, se agrega la funcionalidad de que el juego termine cuando un
# enemigo toque la nave

'''Clase Adicional: Convierte tu Juego en un Archivo Ejecutable (.exe)
Muchos estudiantes me han estado preguntando cómo transformar el juego Invasores Espaciales (o cualquier otro programa creado con Python en general) en un programa independiente, que se pueda ejecutar por fuera del IDE.

Entonces, a pedido, aquí va este pequeño manual paso a paso para hacerlo:



Básicamente el proceso consta de 2 grandes pasos:

Convertir las fuentes de tipo Sting a objetos Bytes

Utilizar pyinstaller

Entonces vamos por partes:

Convertir las fuentes de tipo Sting a objetos Bytes

Descarga la o las fuentes empleadas en el juego, en este caso FreeSansBold.ttf (https://www.download-free-fonts.com/details/2045/free-sans-bold). Luego guárdala en la carpeta donde se encuentra Invasión_Espacial.py como se muestra en la imagen siguiente:


Crea una función que transforme el nombre de la fuente (“FreeSansBold.ttf”) de string a objeto Bytes. Para eso importamos la librería io, y pasamos como parámetro el nombre de la fuente al almacenar la función en una variable.


Almacena la función en una variable que luego se pasará como objeto Bytes a pygame.font.Font.


Utilizar pyinstaller

Instala pyinstaller usando:

pip installer pyinstaller

Abre CMD en la carpeta donde se encuentra el archivo Invasión_Espacial.py


Escribe el siguiente comando:

pyinstaller --clean --onefile --windowed Invasión_Espacial.py



Donde cada expresión significa lo siguiente:

· --clean: elimina todos los archivos temporales y directorios creados por pyinstaller durante la construcción del archivo ejecutable.

· --onefile: crea un archivo ejecutable que contiene todos los archivos necesarios para ejecutar el script, incluyendo los módulos y bibliotecas utilizadas por el script.

· --windowed: crea un archivo ejecutable que se ejecuta en una ventana en lugar de en pantalla completa.

· Invasión_Espacial.py: es el nombre del script Python que se va a convertir en un archivo ejecutable.

Luego de unos segundos se terminará de correr el comando y la consola mostrará el siguiente mensaje:


Se van a generar dos carpetas, una llamada built y otra llamada dist. En esta última se deberán copiar todos los archivos que son referencias para que el juego funcione:




¡Y eso es todo! ¡Espero que te sea de gran ayuda para que peudas compartir tus programas con el mundo!'''