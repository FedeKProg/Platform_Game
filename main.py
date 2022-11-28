import pygame
from pygame import mixer
import sys
from map_data import *
from constantes import *
from Level_setup import *
from player import *
from enemy import *
from botones import *
from interacciones import *
from os import path

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("El juego de Fede")
clock = pygame.time.Clock()

#setear imagenes del juego
imagen_fondo = pygame.image.load("practica_tp/Recursos/Background/Green.png")
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_PANTALLA,ALTO_PANTALLA))
imagen_reinicio = pygame.image.load("practica_tp/Recursos/files/restart_btn.png")
imagen_inicio = pygame.image.load("practica_tp/Recursos/start_btn.png") 
imagen_salir = pygame.image.load("practica_tp/Recursos/exit_btn.png")

#setear elementos
seteo = MapCreator(1)
level = Level(seteo.get_items())
jugador = Player(50,670)
boton_reinicio = Boton(ANCHO_PANTALLA//2 - 80, ALTO_PANTALLA // 2 +100, imagen_reinicio)
boton_inicio = Boton(ANCHO_PANTALLA//2 -280, ALTO_PANTALLA // 2 , imagen_inicio)
boton_salir = Boton(ANCHO_PANTALLA//2 + 100, ALTO_PANTALLA // 2 , imagen_salir)

# #seteo de niveles
# def pasar_niveles(nivel):
# 	'''

# 	'''
# 	jugador.reset(50,670)
# 	grupo_enemigo.empty()
# 	grupo_monedas.empty()
# 	grupo_puertas.empty()

# 	nivel_data = seteo.get_items()

# 	# if path.exists(f'practica_tp/nivel_{nivel}.json'):
# 	# 	subir_file = open(f'practica_tp/nivel_{nivel}.json', 'r')
# 	# 	nivel = json.load(subir_file)
# 	# nivel_data = level.draw_items 
# 	return nivel_data


run = True
while run:

	delta_ms = clock.tick(FPS)
	keys = pygame.key.get_pressed()
	screen.blit(imagen_fondo,(0,0))
	if menu_principal == True:
		if boton_salir.draw():
			run = False
		if boton_inicio.draw():
			menu_principal = False
	else:
		level.draw_items()
		grupo_puertas.draw(screen)
		grupo_monedas.draw(screen)
		grupo_enemigo.draw(screen)
		if game_over == 0:
			grupo_enemigo.update()
			#updatear score
			if pygame.sprite.spritecollide(jugador,grupo_monedas,True):
				musica_moneda.play()
				score += 10
			escribir("SCORE:" + str(score),fuente_score,white,item_size-10,10)
		jugador.draw()
		game_over = jugador.update(game_over)

		if game_over==-1:
			escribir("GAME OVER",fuente_game_over,black,(ANCHO_PANTALLA/2)-330,ALTO_PANTALLA/2)
			if boton_reinicio.draw():
				jugador.reset(50,670)
				#grupo_monedas.draw(screen)
				game_over = 0
				score = 0


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			run = False
	
	pygame.display.update()
pygame.quit()
