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
from gui_form import *
from gui_widget import *

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("El juego de Fede")
clock = pygame.time.Clock()

#setear imagenes del juego
# imagen_fondo = pygame.image.load("Recursos/Background/Green.png")
# imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_PANTALLA,ALTO_PANTALLA))
# imagen_reinicio = pygame.image.load("Recursos/files/restart_btn.png")
# imagen_inicio = pygame.image.load("Recursos/start_btn.png") 
# imagen_salir = pygame.image.load("Recursos/exit_btn.png")

#setear elementos
# seteo = MapCreator(1)
# level = Level(seteo.get_items())
#boton_reinicio = Boton(ANCHO_PANTALLA//2 - 80, ALTO_PANTALLA // 2 +100, imagen_reinicio)
jugador = Player(50,670)
main_menu_form = FormMenu(name="main_menu_form",master_surface=screen,x=0,y=0,active=True,lvl=1)
form_opciones = FormOpciones(name="form_opciones",master_surface=screen,x=0,y=0,active=True,lvl=1)
from_start_nivel = FormNivelStart(name="from_start_nivel",master_surface=screen,x=0,y=0,active=True,lvl=1)
form_pausa = FormPausa(name="form_pausa",master_surface=screen,x=0,y=0,active=True,lvl=1)


while True:     

	lista_eventos = pygame.event.get()
	for event in lista_eventos:
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if(event.key == pygame.K_ESCAPE):
				form_pausa.set_active("form_pausa")


	keys = pygame.key.get_pressed()

	if(main_menu_form.active):
		main_menu_form.update(lista_eventos)
		main_menu_form.draw()
	elif(from_start_nivel.active):
		from_start_nivel.update()
		from_start_nivel.draw()
		level.draw_items(screen)
		grupo_puertas.draw(screen)
		grupo_monedas.draw(screen)
		grupo_enemigo.draw(screen)
		if pygame.sprite.spritecollide(jugador,grupo_monedas,True):
			score += 10
		escribir("SCORE:" + str(score),fuente_score,white,item_size-10,10)
	elif(form_opciones.active):
		form_opciones.update(keys)
		form_opciones.draw()
	elif(form_pausa.active):
		form_pausa.update(keys)
		form_pausa.draw()


	# screen.blit(imagen_fondo,(0,0))
	# if menu_principal == True:
	# 	if boton_salir.draw():
	# 		run = False
	# 	if boton_inicio.draw():
	# 		menu_principal = False
	# else:
	# 	level.draw_items()
	# 	grupo_puertas.draw(screen)
	# 	grupo_monedas.draw(screen)
	# 	grupo_enemigo.draw(screen)
	# 	if game_over == 0:
	# 		grupo_enemigo.update()
	# 		#updatear score
	# 		if pygame.sprite.spritecollide(jugador,grupo_monedas,True):
	# 			musica_moneda.play()
	# 			score += 10
	# 		escribir("SCORE:" + str(score),fuente_score,white,item_size-10,10)
	# 	jugador.draw()
	# 	game_over = jugador.update(game_over)

	# 	if game_over==-1:
	# 		escribir("GAME OVER",fuente_game_over,black,(ANCHO_PANTALLA/2)-330,ALTO_PANTALLA/2)
	# 		if boton_reinicio.draw():
	# 			jugador.reset(50,670)
	# 			#grupo_monedas.draw(screen)
	# 			game_over = 0
	# 			score = 0


	
	pygame.display.update()
pygame.quit()
