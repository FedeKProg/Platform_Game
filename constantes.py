import pygame
from pygame import mixer

pygame.mixer.pre_init()
mixer.init()

#dimension pantalla
ANCHO_PANTALLA = 1000
ALTO_PANTALLA = 800

FPS=15
#tamaño de la imagen del items
item_size = 40

game_over = 0
menu_principal = True
# shoot = False
max_niveles = 3
vidas = 5
fuente_score = pygame.font.SysFont("Futura", 40)
fuente_game_over = pygame.font.SysFont("Futura",150)
SEGUNDO = 1000



#sonidos
musica_moneda = pygame.mixer.Sound("Recursos/files/coin.wav")
musica_moneda.set_volume(0.5)
musica_salto = pygame.mixer.Sound("Recursos/files/jump.wav")
musica_salto.set_volume(0.5)
musica_game_over= pygame.mixer.Sound("Recursos/files/game_over.wav")
musica_game_over.set_volume(0.5)
musica_fondo = pygame.mixer.music.load("Recursos/files/music.wav")
musica_fondo = pygame.mixer.music.play(0,0,4000)
musica_fondo = pygame.mixer.music.set_volume(0.4)
click_sound = pygame.mixer.Sound('Recursos/mixkit-select-click-1109.wav')
click_sound.set_volume(0.2)
win_sound = pygame.mixer.Sound('Recursos\success-fanfare-trumpets-6185.wav')
win_sound.set_volume(0.6)
enemy_death_sound = pygame.mixer.Sound('Recursos\Explosion14.wav')
enemy_death_sound.set_volume(0.6)

#Se setean los distintos grupos de elementos del juego
grupo_enemigo = pygame.sprite.Group()
grupo_monedas = pygame.sprite.Group()
grupo_puertas = pygame.sprite.Group()
grupo_balas = pygame.sprite.Group() 
grupo_trampas = pygame.sprite.Group() 


#define colours
white = (255, 255, 255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0, 0, 255)