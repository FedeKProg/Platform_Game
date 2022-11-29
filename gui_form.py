import pygame
from pygame.locals import *
from gui_widget import Widget
from gui_boton import Button
from auxiliar import Auxiliar
from constantes import *
from player import Player
from map_data import *
from Level_setup import *
from interacciones import *
from botones import *

 

class Form():
	forms_dict = {}
	def __init__(self,name,master_surface,x,y,active,lvl):
		self.forms_dict[name] = self
		self.master_surface = master_surface
		self.x = x
		self.y = y

		self.active = active
		self.surface = pygame.image.load("Recursos/Background/Green.png").convert_alpha()
		self.surface = pygame.transform.scale(self.surface,(ANCHO_PANTALLA,ALTO_PANTALLA))
		self.slave_rect = self.surface.get_rect()
		self.slave_rect.x = x
		self.slave_rect.y = y
		self.lvl = lvl
		self.grupo_enemigos = pygame.sprite.Group()
		self.grupo_monedas = pygame.sprite.Group()
		self.grupo_puertas = pygame.sprite.Group()

	#me activa el forms con el mismo nombre y desactiva los demas
	def set_active(self,name):
		for aux_form in self.forms_dict.values():
			aux_form.active = False
		self.forms_dict[name].active = True

	# def render(self):
	#     pass

	# def update(self,lista_eventos):
	#     pass

	def draw(self):
		self.master_surface.blit(self.surface,self.slave_rect)


class FormMenu(Form):
	def __init__(self,name,master_surface,x,y,active,lvl):
		super().__init__(name,master_surface,x,y,active,lvl)
		#self.main_menu_ttl = 

		self.start = Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2,text='START GAME',screen=master_surface,on_click=self.click_start,on_click_param="from_start_nivel",font_size=60)
		self.option = Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2-100,text='SETTINGS',screen=master_surface,on_click=self.click_start,on_click_param="form_opciones",font_size=60)
		self.lista_widget = [self.start,self.option]
		

	def click_options(self, parametro):
		self.set_active(parametro)

	def click_start(self,parametro):
		self.set_active(parametro)


	def update(self, lista_eventos):
		for aux_boton in self.lista_widget:
			aux_boton.update(lista_eventos)

	def draw(self): 
		super().draw()
		for aux_boton in self.lista_widget:    
			aux_boton.draw()


class FormNivelStart(Form):
	def __init__(self,name,master_surface,x,y,active,lvl):
		super().__init__(name,master_surface,x,y,active,lvl)
		self.screen = master_surface
		self.seteo = MapCreator(1)
		self.level = Level(self.seteo.get_items())
		self.clock = pygame.time.Clock()
		self.imagen_fondo = pygame.image.load("Recursos/Background/Green.png").convert_alpha()
		self.imagen_fondo = pygame.transform.scale(self.imagen_fondo,(ANCHO_PANTALLA,ALTO_PANTALLA))
		#ENEMIGOS
		self.grupo_enemigo = pygame.sprite.Group()
		self.image = pygame.image.load("Recursos/files/blob.png")
		#MONEDAS
		self.grupo_monedas = pygame.sprite.Group()
		self.imagen_moneda = pygame.image.load("Recursos/files/coin.png")
		#PLAYER
		self.jugador = Player(50,670)
		#PUERTAS
		self.grupo_puertas = pygame.sprite.Group()
		self.imagen_puerta = pygame.image.load("Recursos/files/exit.png")


	def update(self):
		self.game_over = 0 
		self.score = 0
		if self.game_over == 0:
			grupo_enemigo.update()
			#updatear score
			if pygame.sprite.spritecollide(self.jugador, grupo_enemigo, False):
				#agregar musica
				musica_game_over.play()
				self.game_over = -1
			if pygame.sprite.spritecollide(self.jugador,grupo_monedas,True):
				musica_moneda.play()
				self.score += 10
				escribir("SCORE:" + str(self.score),fuente_score,white,item_size-10,10)
		self.game_over = self.jugador.update(self.game_over)
		if self.game_over==-1:
			self.jugador.reset(100,670)
			escribir("GAME OVER",fuente_game_over,black,(ANCHO_PANTALLA/2)-330,ALTO_PANTALLA/2)
			self.game_over = 0

		self.screen.blit(self.imagen_fondo,self.imagen_fondo.get_rect())

	def draw(self):
		self.score = 0
		self.level.draw_items(screen)
		self.grupo_puertas.draw(screen)
		self.grupo_monedas.draw(screen)
		self.grupo_enemigo.draw(screen)
		self.jugador.draw()



class FormOpciones(Form):
	def __init__(self,name,master_surface,x,y,active,lvl):
		super().__init__(name,master_surface,x,y,active,lvl)

	#self.main_menu_ttl = 

		self.music_on = Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2,text='Music ON',screen=master_surface,on_click=self.click_music_on,font_size=40)
		self.music_off = Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2-100,text='Music OFF',screen=master_surface,on_click=self.click_music_off,font_size=40)
		self.volver = Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2-200,text='Back to Menu',screen=master_surface,on_click=self.click_back,on_click_param="main_menu_form",font_size=40)
		self.lista_widget = [self.music_off,self.music_on,self.volver]
		

	def click_music_on(self, parametro):
		pygame.mixer.music.unpause()

	def click_music_off(self, parametro):
		pygame.mixer.music.pause()

	def click_back(self,parametro):
		self.set_active(parametro)
	

	def update(self, lista_eventos):
		for aux_boton in self.lista_widget:
			aux_boton.update(lista_eventos)

	def draw(self): 
		super().draw()
		for aux_boton in self.lista_widget:    
			aux_boton.draw()

class FormPausa(Form):
	def __init__(self,name,master_surface,x,y,active,lvl):
		super().__init__(name,master_surface,x,y,active,lvl)

	#self.main_menu_ttl = 

		self.music_on = Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2+100,text='Music ON',screen=master_surface,on_click=self.click_music_on,font_size=40)
		self.music_off= Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2,text='Music OFF',screen=master_surface,on_click=self.click_music_off,font_size=40)
		self.volver = Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2-100,text='Back to Menu',screen=master_surface,on_click=self.click_back,on_click_param="main_menu_form",font_size=40)

		self.resume_btn = Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2-200,text='Back to Game',screen=master_surface,on_click=self.click_resume,on_click_param="from_start_nivel",font_size=40)
		self.lista_widget = [self.music_off,self.music_on,self.volver,self.resume_btn]

	
	def click_resume(self,parametro):
		self.set_active(parametro)

	def click_music_on(self, parametro):
		pygame.mixer.music.unpause()

	def click_music_off(self, parametro):
		pygame.mixer.music.pause()

	def click_back(self,parametro):
		self.set_active(parametro)
	

	def update(self, lista_eventos):
		for aux_boton in self.lista_widget:
			aux_boton.update(lista_eventos)

	def draw(self): 
		super().draw()
		for aux_boton in self.lista_widget:    
			aux_boton.draw()