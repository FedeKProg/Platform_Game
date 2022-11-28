import pygame
from pygame import mixer

pygame.mixer.pre_init()
mixer.init()

#dimension pantalla
ANCHO_PANTALLA = 1000
ALTO_PANTALLA = 800

FPS=60
#tamaño de la imagen del item
item_size = 40
nivel = 1
game_over = 0
menu_principal = True
score = 0
max_niveles = 3

fuente_score = pygame.font.SysFont("Futura", 40)
fuente_game_over = pygame.font.SysFont("Comis Sans MS",150)




#sonidos
musica_moneda = pygame.mixer.Sound("practica_tp/Recursos/files/coin.wav")
musica_moneda.set_volume(0.5)
musica_salto = pygame.mixer.Sound("practica_tp/Recursos/files/jump.wav")
musica_salto.set_volume(0.5)
musica_game_over= pygame.mixer.Sound("practica_tp/Recursos/files/game_over.wav")
musica_game_over.set_volume(0.5)
pygame.mixer.music.load("practica_tp/Recursos/files/music.wav")
pygame.mixer.music.play(0,0,4000)






#define colours
white = (255, 255, 255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0, 0, 255)