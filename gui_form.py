import pygame
from pygame.locals import *
from gui_widget import Widget
from gui_boton import *
from auxiliar import Auxiliar
from constantes import *
from player import Player
from map_data import *
from Level_setup import *
from interacciones import *
from botones import *

 

class Form():
	forms_dict = {}
	def __init__(self,name,master_surface,x,y,active,nivel):
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
		self.grupo_enemigos = pygame.sprite.Group()
		self.grupo_monedas = pygame.sprite.Group()
		self.grupo_puertas = pygame.sprite.Group()
		self.nivel = nivel

	#me activa el forms con el mismo nombre y desactiva los demas
	def set_active(self,name):
		for aux_form in self.forms_dict.values():
			aux_form.active = False
		self.forms_dict[name].active = True


	def draw(self):
		self.master_surface.blit(self.surface,self.slave_rect)


class FormMenu(Form):
	def __init__(self,name,master_surface,x,y,active,lvl):
		super().__init__(name,master_surface,x,y,active,lvl)
		#self.main_menu_ttl = 

		self.start = Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2,text='START GAME',screen=master_surface,on_click=self.click_start,on_click_param="from_start_nivel",font_size=60)
		self.option = Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2-100,text='SETTINGS',screen=master_surface,on_click=self.click_start,on_click_param="form_opciones",font_size=60)
		self.seleccion_nivel = Button(x=ANCHO_PANTALLA/2,y=ALTO_PANTALLA//2+100,text='Seleccionar Nivel',screen=master_surface,on_click=self.click_seleccion_nivel,on_click_param="form_seleccion_nivel",font_size=60)
		self.lista_widget = [self.start,self.option,self.seleccion_nivel]
		

	def click_seleccion_nivel(self, parametro):
		click_sound.play(0,450,0)
		self.set_active(parametro)

	def click_options(self, parametro):
		click_sound.play(0,450,0)
		self.set_active(parametro)

	def click_start(self,parametro):
		click_sound.play(0,450,0)
		self.set_active(parametro)


	def update(self, lista_eventos):
		for aux_boton in self.lista_widget:
			aux_boton.update(lista_eventos)

	def draw(self): 
		super().draw()
		for aux_boton in self.lista_widget:    
			aux_boton.draw()


class FormNivelStart(Form):
	def __init__(self,name,master_surface,x,y,active,nivel):
		super().__init__(name,master_surface,x,y,active,nivel)
		self.screen = master_surface

		self.seteo = MapCreator(nivel)
		self.level = Level(self.seteo.get_items())
		self.clock = pygame.time.Clock()
		self.imagen_fondo = pygame.image.load("Recursos/Background/Green.png").convert_alpha()
		self.imagen_fondo = pygame.transform.scale(self.imagen_fondo,(ANCHO_PANTALLA,ALTO_PANTALLA))
		#ENEMIGOS
		if grupo_enemigo != None:
			self.grupo_enemigo = pygame.sprite.Group()
		self.image = pygame.image.load("Recursos/files/blob.png")
		#MONEDAS
		self.score = 0
		if grupo_monedas != None:
			self.grupo_monedas = pygame.sprite.Group()
		self.imagen_moneda = pygame.image.load("Recursos/files/coin.png")
		#PLAYER
		self.jugador = Player(50,670)
		#PUERTAS
		if grupo_puertas != None:
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
			elif pygame.sprite.spritecollide(self.jugador,grupo_monedas,True):
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
		if pygame.sprite.spritecollide(self.jugador,grupo_monedas,True):
			self.score += 10	
			musica_moneda.play()	



class FormOpciones(Form):
	def __init__(self,name,master_surface,x,y,active,lvl):
		super().__init__(name,master_surface,x,y,active,lvl)

	#self.main_menu_ttl = 

		self.music_on = Button(x=ANCHO_PANTALLA//2-80,y=ALTO_PANTALLA//2,text='Music ON',screen=master_surface,on_click=self.click_music_on,font_size=40)
		self.music_off = Button(x=ANCHO_PANTALLA//2+ 120,y=ALTO_PANTALLA//2,text='OFF',screen=master_surface,on_click=self.click_music_off,font_size=40)
		self.volver = Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2-150,text='Back to Menu',screen=master_surface,on_click=self.volver,on_click_param="main_menu_form",font_size=40)
		self.lista_widget = [self.music_off,self.music_on,self.volver]
		

	def click_music_on(self,paramentro):
		click_sound.play(0,450,0)
		pygame.mixer.music.unpause()

	def click_music_off(self,parametro):
		click_sound.play(0,450,0)
		pygame.mixer.music.pause()

	def volver(self,parametro):
		click_sound.play(0,450,0)
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

		self.music_on = Button(x=ANCHO_PANTALLA//2-80,y=ALTO_PANTALLA//2,text='Music ON',screen=master_surface,on_click=self.click_music_on,font_size=40)
		self.music_off = Button(x=ANCHO_PANTALLA//2+ 120,y=ALTO_PANTALLA//2,text='OFF',screen=master_surface,on_click=self.click_music_off,font_size=40)
		self.volver = Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2-100,text='Back to Menu',screen=master_surface,on_click=self.click_back,on_click_param="main_menu_form",font_size=40)

		self.resume_btn = Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2-200,text='Back to Game',screen=master_surface,on_click=self.click_resume,on_click_param="from_start_nivel",font_size=40)
		self.lista_widget = [self.music_off,self.music_on,self.volver,self.resume_btn]

	
	def click_resume(self,parametro):
		click_sound.play(0,450,0)
		self.set_active(parametro)

	def click_music_on(self, parametro):
		click_sound.play(0,450,0)
		pygame.mixer.music.unpause()

	def click_music_off(self, parametro):
		click_sound.play(0,450,0)
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

class FormDeath(Form):
	def __init__(self,name,master_surface,x,y,active,lvl):
		super().__init__(name,master_surface,x,y,active,lvl)
		
		self.music_on_btn = Button(x=ANCHO_PANTALLA/1.2-10,y=ALTO_PANTALLA//2-100,text='Music ON',screen=master_surface,on_click=self.click_music_on,font_size=40)
		self.music_off_btn = Button(x=ANCHO_PANTALLA/1.2-10,y=ALTO_PANTALLA//2-200,text='Music OFF',screen=master_surface,on_click=self.click_music_off,font_size=40)
		self.back_btn = Button(x=ANCHO_PANTALLA/1.2-10,y=ALTO_PANTALLA//2-300,text='Volver al menu',screen=master_surface,on_click=self.click_back,on_click_param="menu_form",font_size=40)
		self.perdiste_txt = Textos(x=ANCHO_PANTALLA/1.2-10,y=ALTO_PANTALLA//2+50,text='Perdiste',screen=master_surface,font_size=40)
		self.retry_btn = Button(x=ANCHO_PANTALLA/1.2-15,y=ALTO_PANTALLA//2+100,text='Reintentar',screen=master_surface,on_click=self.click_retry,on_click_param="menu_form",font_size=25)
																																							#form_start_nivel
		self.lista_widget = [self.music_off_btn,self.music_on_btn,self.back_btn,self.retry_btn]

	def click_retry(self,parametro):
		self.set_active(parametro)
		click_sound.play(0,450,0)
	def click_music_on(self, parametro):
		pygame.mixer.music.unpause()
		click_sound.play(0,450,0)
	def click_music_off(self, parametro):
		pygame.mixer.music.pause()
		click_sound.play(0,450,0)
	def click_back(self,parametro):
		self.set_active(parametro)
		pygame.mixer.music.unpause()

	def update(self, lista_eventos):
		for aux_boton in self.lista_widget:
			aux_boton.update(lista_eventos)

	def draw(self): 
		super().draw()
		for aux_boton in self.lista_widget:    
			aux_boton.draw()
	

class FormWin(Form):
	def __init__(self,name,master_surface,x,y,active,lvl):
		super().__init__(name,master_surface,x,y,active,lvl)

		self.music_on_btn = Button(x=ANCHO_PANTALLA/1.2-10,y=ALTO_PANTALLA//2,text='Music ON',screen=master_surface,on_click=self.click_music_on,font_size=40)
		self.music_off_btn = Button(x=ANCHO_PANTALLA/1.2-10,y=ALTO_PANTALLA//2-100,text='Music OFF',screen=master_surface,on_click=self.click_music_off,font_size=40)
		self.back_btn = Button(x=ANCHO_PANTALLA/1.2-10,y=ALTO_PANTALLA//2-200,text='Volver al menu',screen=master_surface,on_click=self.click_back,on_click_param="menu_form",font_size=40)
		self.ganaste_txt = Textos(x=ANCHO_PANTALLA/1.2-10,y=ALTO_PANTALLA//2-300,text='Ganaste',screen=master_surface,font_size=70)
		
																																					 
		self.lista_widget = [self.music_off_btn,self.music_on_btn,self.back_btn,self.ganaste_txt]


	def click_music_on(self, parametro):
		click_sound.play(0,450,0)
		pygame.mixer.music.unpause()

	def click_music_off(self, parametro):
		click_sound.play(0,450,0)
		pygame.mixer.music.pause()

	def click_back(self,parametro):
		click_sound.play(0,450,0)
		self.set_active(parametro)
		pygame.mixer.music.unpause()
		

	def update(self, lista_eventos):
		for aux_boton in self.lista_widget:
			aux_boton.update(lista_eventos)

	def draw(self): 
		super().draw()
		for aux_boton in self.lista_widget:    
			aux_boton.draw()

class FormLvlSelect(Form):
	def __init__(self,name,master_surface,x,y,active,lvl):
		super().__init__(name,master_surface,x,y,active,lvl)
		self.selected_lvl = lvl
		self.is_selected = False
		self.lvl1_btn = Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2-300,text='Nivel 1',screen=master_surface,on_click=self.seleccion_nivel_1,on_click_param="form_start_nivel",font_size=40)
		self.lvl2_btn = Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2-200,text='Nivel 2',screen=master_surface,on_click=self.seleccion_nivel_2,on_click_param="form_start_nivel",font_size=40)
		self.lvl3_btn = Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2-100,text='Nivel 3',screen=master_surface,on_click=self.seleccion_nivel_3,on_click_param="form_start_nivel",font_size=40)
		self.back_btn = Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2,text='Volver',screen=master_surface,on_click=self.volver,on_click_param="menu_form",font_size=40)
																																					
		self.lista_widget = [self.lvl1_btn,self.lvl2_btn,self.back_btn,self.lvl3_btn]
	
	
	def seleccion_nivel_1(self,parametro):
		self.set_active(parametro)
		click_sound.play(0,450,0)
		self.selected_lvl = 1
		self.is_selected = True
	def seleccion_nivel_2(self, parametro):
		self.set_active(parametro)
		click_sound.play(0,450,0)
		self.selected_lvl = 2

		self.is_selected = True
	def seleccion_nivel_3(self, parametro):
		self.set_active(parametro)
		click_sound.play(0,450,0)
		self.seteo.get_items
		self.selected_lvl = 3
		self.is_selected = True
	def volver(self,parametro):
		self.set_active(parametro)
	

	def update(self, lista_eventos):
		for aux_boton in self.lista_widget:
			aux_boton.update(lista_eventos)

	def draw(self): 
		super().draw()
		for aux_boton in self.lista_widget:    
			aux_boton.draw()