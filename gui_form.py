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
from sqlite import *

class Form():
	'''
	Creacion de la clase madre, de las cuales los demas forms heredaran sus funciones y definiciones.
	Se setea la imagen de fondo en donde se aplicaran los demas forms.
	'''
	forms_dict = {}
	def __init__(self,name,master_surface,x,y,active):
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
		# self.grupo_enemigos = pygame.sprite.Group()
		# self.grupo_monedas = pygame.sprite.Group()
		# self.grupo_puertas = pygame.sprite.Group()

	#me activa el forms con el mismo nombre y desactiva los demas
	def set_active(self,name):
		'''
		Se chequea si el forms se encuntra activo o no, para ser mostrado o no.
		'''
		for aux_form in self.forms_dict.values():
			aux_form.active = False
		self.forms_dict[name].active = True


	def draw(self):
		'''
		Se dibuja el forms correspondiente en la pantalla
		'''
		self.master_surface.blit(self.surface,self.slave_rect)


class FormMenu(Form):
	def __init__(self,name,master_surface,x,y,active):
		super().__init__(name,master_surface,x,y,active)
		'''
		Se crean los botones a ser mostrados y ejecutados en el menu principal del juego
		'''

		self.start = Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2,text='START GAME',screen=master_surface,on_click=self.click_start,on_click_param="form_start_nivel",font_size=60)
		self.option = Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2-100,text='SETTINGS',screen=master_surface,on_click=self.click_start,on_click_param="form_opciones",font_size=60)
		self.puntajes = Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2+200,text='HIGHSCORES',screen=master_surface,on_click=self.click_puntajes,on_click_param="form_puntajes",font_size=60)
		self.seleccion_nivel = Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2+100,text='SELECT LEVEL',screen=master_surface,on_click=self.click_seleccion_nivel,on_click_param="form_seleccion_nivel",font_size=60)
		self.lista_widget = [self.start,self.option,self.puntajes,self.seleccion_nivel]
		

	def click_seleccion_nivel(self, parametro):
		'''
		Recibe como parametro, si el mismo fue activado con el click o no.
		Funcion que se activa al apretar el boton de selecíon de nivel, y que nos lleva al form de selecíon de nivel.
		Devuelve el forms a ser ejecutado
		'''
		click_sound.play(0,450,0)
		self.set_active(parametro)

	def click_options(self, parametro):
		'''
		Recibe como parametro, si el mismo fue activado con el click o no.
		Funcion que activa el boton de opciones, y nos lleva al form de opciones.
		Devuelve el forms a ser ejecutado
		'''
		click_sound.play(0,450,0)
		self.set_active(parametro)

	def click_start(self,parametro):
		'''
		Recibe como parametro, si el mismo fue activado con el click o no.
		Funcion que se activa con el boton de start game, y ejecuta por defecto el primer nivel del juego.
		Devuelve como parametro el nivel 1, que esta seteado para ser ejecutado
		'''
		click_sound.play(0,450,0)
		self.set_active(parametro)
		
	def click_puntajes(self, parametro):
		self.set_active(parametro)
		click_sound.play(0,450,0)

	def update(self, lista_eventos):
		'''
		detecta el evento del click y procede asi a ejecutar la funcion del boton.
		'''
		for aux_boton in self.lista_widget:
			aux_boton.update(lista_eventos)

	def draw(self): 
		'''
		dibuja los botones en la pantalla
		'''
		super().draw()
		for aux_boton in self.lista_widget:    
			aux_boton.draw()


class FormNivelStart(Form):
	def __init__(self,name,master_surface,x,y,active,nivel):
		super().__init__(name,master_surface,x,y,active)
		'''
		Se setean los elementos y valores iniciales de los niveles.
		Se setea el fondo de pantalla, se dibujan a los enemigos, items, tiles, trampas, etc. dentro de la pantalla.
		A su vez se setean los valores correspondientes a la vida del jugador, el score del nivel y el tiempo para completarlo.
		'''
		grupo_enemigo.empty()
		grupo_monedas.empty()
		grupo_puertas.empty()
		grupo_trampas.empty()
		grupo_balas.empty()
		self.nivel = nivel
		self.seteo = MapCreator(self.nivel)
		self.level = Level(self.seteo.get_items())
		self.nivel_timer = self.seteo.get_timer_sec()
		self.last_timer = pygame.time.get_ticks()
		self.screen = master_surface
		self.vidas = 5
		self.puntos = 0
		self.higscore = 0
		self.shoot_cooldown = 0
		self.clock = pygame.time.Clock()
		self.imagen_fondo = pygame.image.load("Recursos/Background/Green.png").convert_alpha()
		self.imagen_fondo = pygame.transform.scale(self.imagen_fondo,(ANCHO_PANTALLA,ALTO_PANTALLA))
		#ENEMIGOS
		# self.grupo_enemigo = pygame.sprite.Group.remove(grupo_enemigo)
		# self.grupo_enemigo = grupo_enemigo
		# self.image = pygame.image.load("Recursos/files/blob.png")
		#MONEDAS
		# self.score = 0
		# self.grupo_monedas = pygame.sprite.Group.remove(grupo_monedas)
		# self.grupo_monedas = grupo_monedas
		# self.imagen_moneda = pygame.image.load("Recursos/files/coin.png")
		#PLAYER
		self.jugador = Player(50,670)
		#PUERTAS
		# self.grupo_puertas = pygame.sprite.Group.remove(grupo_puertas)
		# self.grupo_puertas = grupo_puertas
		# self.imagen_puerta = pygame.image.load("Recursos/files/exit.png")

	def update(self):
		'''
		Se actualizan los valores de los niveles, en relacion con el desarrollo del nivel jugado.
		Se actualizan los jugadores y los enemigos con los movimeintos correspondientes a estos, como a su vez la colision entre estos.
		Ademas, se chequean las colisiones con los demas elementos del nivel, modificando el valor que corresponda en cada caso.
		Ademas se agregan los efectos de sonido correspondientes a cada colision.
		'''
		self.game_over = 0 
		self.score = 0
		self.shoot = False
		if self.game_over == 0:
			grupo_enemigo.update()
			#self.jugador.disparo()
			self.jugador.update(self.game_over,self.level.lista_items)
			#updatear score
			# if self.shoot:
			# 	self.jugador.disparo()
			if(self.nivel_timer > 0 ):
				timer_sec = pygame.time.get_ticks()
				if(timer_sec - self.last_timer > SEGUNDO):
					self.last_timer = timer_sec
					self.nivel_timer -= 1
			if pygame.sprite.spritecollide(self.jugador,grupo_trampas,False):
				self.vidas -= 1
				self.jugador.reset(50,670)
				musica_game_over.play()
			if pygame.sprite.spritecollide(self.jugador, grupo_enemigo, False):
				#agregar musica
				musica_game_over.play()
				self.vidas -= 1
				self.jugador.reset(50,670)
				grupo_monedas.draw(screen)
				grupo_enemigo.draw(screen)
			if self.vidas == 0 or self.nivel_timer == 0:
				self.game_over = -1
				self.reinicio()
				self.set_active("form_death")
				self.vidas = 5
				self.nivel_timer = self.seteo.get_timer_sec()
			elif pygame.sprite.spritecollide(self.jugador,grupo_monedas,True):
				self.puntos += 10
				musica_moneda.play()
			elif pygame.sprite.spritecollide(self.jugador,grupo_puertas,False):
				self.game_over = 1
				self.set_active("form_win")
				self.nivel += 1
				win_sound.play(0,4000,0)
				#self.set_active("form_name")
				#self.reinicio()
			for enemy in grupo_enemigo:
				if pygame.sprite.spritecollide(enemy, grupo_balas, False):
					enemy.kill()
					self.puntos += 10
					enemy_death_sound.play(0,4000,0)
			for bala in grupo_balas:
				pygame.sprite.spritecollide(bala,grupo_enemigo,False)
			# elif pygame.sprite.spritecollide(self.jugador,grupo_monedas,True):
			# 	musica_moneda.play()
			# 	self.score += 10
			# 	escribir("SCORE:" + str(self.score),fuente_score,white,item_size-10,10)
		self.game_over = self.jugador.update(self.game_over, self.level.lista_items)
		if self.game_over==-1:
			self.jugador.reset(50,670)
			escribir("GAME OVER",fuente_game_over,black,(ANCHO_PANTALLA/2)-330,ALTO_PANTALLA/2)
			self.game_over = 0
		
		# if self.nivel == 1:
		# 	if self.higscore < self.puntos:
		# 		sql.agregar_score(self.nivel,self.vidas,self.puntos,self.last_timer)
		# 		sql.select()
		# if self.nivel == 2:
		# 	if self.higscore < self.puntos:
		# 		sql.agregar_score(self.nivel,self.vidas,self.puntos,self.last_timer)
		# 		sql.select()
		# if self.nivel == 3:
		# 	if self.higscore < self.puntos:
		# 		sql.agregar_score(self.nivel,self.vidas,self.puntos,self.last_timer)
		# 		sql.select()		


		self.screen.blit(self.imagen_fondo,self.imagen_fondo.get_rect())
	def reinicio(self):
		self.__init__(name="form_start_nivel",master_surface=screen,x=0,y=0,active=True,nivel=self.nivel)

	def draw(self):
		'''
		Se dibujan los elementos que corresponden a cada nivel, como a su vez los textos que corresponden a la vida, score y tiempo.
		'''
		self.score = 0
		self.level.draw_items(screen)
		grupo_puertas.draw(screen)
		grupo_monedas.draw(screen)
		grupo_enemigo.draw(screen)
		grupo_trampas.draw(screen)
		#grupo_balas.draw(screen)
		#self.enemy.draw()
		if pygame.sprite.spritecollide(self.jugador,grupo_monedas,True):
			musica_moneda.play()
			self.score += 10
		escribir("VIDAS: " + str(self.vidas),fuente_score,white,item_size+300,10)
		escribir("SCORE:" + str(self.puntos),fuente_score,white,item_size-10,10)
		escribir("TIEMPO:" + str(self.nivel_timer),fuente_score,white,item_size+600,10)
		self.jugador.draw()

# def reseteo_grupos():
# 	grupo_enemigo = pygame.sprite.Group.remove(grupo_enemigo)
# 	grupo_monedas = pygame.sprite.Group.remove(grupo_monedas)


class FormNivelStart_2(FormNivelStart):
	def __init__(self,name,master_surface,x,y,active,nivel):
		super().__init__(name,master_surface,x,y,active,nivel)
		self.nivel = nivel
		self.seteo = MapCreator(self.nivel)
		self.level = Level(self.seteo.get_items())
		self.screen = master_surface
		self.clock = pygame.time.Clock()
		self.imagen_fondo = pygame.image.load("Recursos/Background/Green.png").convert_alpha()
		self.imagen_fondo = pygame.transform.scale(self.imagen_fondo,(ANCHO_PANTALLA,ALTO_PANTALLA))
		#ENEMIGOS
		self.grupo_enemigo = pygame.sprite.Group()
		self.image = pygame.image.load("Recursos/files/blob.png")
		#MONEDAS
		self.score = 0
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
			self.jugador.update(game_over,self.level.lista_items)
			#updatear score
			if pygame.sprite.spritecollide(self.jugador, grupo_enemigo, False):
				#agregar musica
				musica_game_over.play()
				self.game_over = -1
				self.set_active("form_death")
				#self.reinicio()
			elif pygame.sprite.spritecollide(self.jugador,grupo_puertas,False):
				self.game_over = 1
				self.set_active("form_win")
				self.nivel += 1
				win_sound.play(0,4000,0)
				#self.reinicio()
			# elif pygame.sprite.spritecollide(self.jugador,grupo_monedas,True):
			# 	musica_moneda.play()
			# 	self.score += 10
			# 	escribir("SCORE:" + str(self.score),fuente_score,white,item_size-10,10)
		self.game_over = self.jugador.update(self.game_over, self.level.lista_items)
		if self.game_over==-1:
			self.jugador.reset(50,670)
			escribir("GAME OVER",fuente_game_over,black,(ANCHO_PANTALLA/2)-330,ALTO_PANTALLA/2)
			self.game_over = 0

		self.screen.blit(self.imagen_fondo,self.imagen_fondo.get_rect())

	def draw(self):
		self.score = 0
		self.level.draw_items(screen)
		grupo_puertas.draw(screen)
		grupo_monedas.draw(screen)
		grupo_enemigo.draw(screen)
		if pygame.sprite.spritecollide(self.jugador,grupo_monedas,True):
			musica_moneda.play()
			self.score += 10
		escribir("SCORE:" + str(self.score),fuente_score,white,item_size-10,10)
		self.jugador.draw()

class FormNivelStart_3(FormNivelStart):
	def __init__(self,name,master_surface,x,y,active,nivel):
		super().__init__(name,master_surface,x,y,active,nivel)
		self.nivel = nivel
		self.seteo = MapCreator(self.nivel)
		Level(self.seteo.vaciar_lista())
		self.level = Level(self.seteo.get_items())
		self.screen = master_surface
		self.clock = pygame.time.Clock()
		self.imagen_fondo = pygame.image.load("Recursos/Background/Green.png").convert_alpha()
		self.imagen_fondo = pygame.transform.scale(self.imagen_fondo,(ANCHO_PANTALLA,ALTO_PANTALLA))
		#ENEMIGOS
		self.grupo_enemigo = pygame.sprite.Group()
		self.image = pygame.image.load("Recursos/files/blob.png")
		#MONEDAS
		self.score = 0
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
			self.jugador.update(game_over,self.level.lista_items)
			#updatear score
			if pygame.sprite.spritecollide(self.jugador, grupo_enemigo, False):
				#agregar musica
				musica_game_over.play()
				self.game_over = -1
				self.set_active("form_death")
				#self.reinicio()
			elif pygame.sprite.spritecollide(self.jugador,grupo_puertas,False):
				self.game_over = 1
				self.set_active("form_win")
				self.nivel += 1
				win_sound.play(0,4000,0)
				#self.reinicio()
			# elif pygame.sprite.spritecollide(self.jugador,grupo_monedas,True):
			# 	musica_moneda.play()
			# 	self.score += 10
			# 	escribir("SCORE:" + str(self.score),fuente_score,white,item_size-10,10)
		self.game_over = self.jugador.update(self.game_over, self.level.lista_items)
		if self.game_over==-1:
			self.jugador.reset(50,670)
			escribir("GAME OVER",fuente_game_over,black,(ANCHO_PANTALLA/2)-330,ALTO_PANTALLA/2)
			self.game_over = 0

		self.screen.blit(self.imagen_fondo,self.imagen_fondo.get_rect())

	def draw(self):
		self.score = 0
		self.level.draw_items(screen)
		grupo_puertas.draw(screen)
		grupo_monedas.draw(screen)
		grupo_enemigo.draw(screen)
		if pygame.sprite.spritecollide(self.jugador,grupo_monedas,True):
			musica_moneda.play()
			self.score += 10
		escribir("SCORE:" + str(self.score),fuente_score,white,item_size-10,10)
		self.jugador.draw()

class FormPuntuaciones(Form):
	'''
	Se crean y se setean los botones y las entradas a ser mostradas en el menu highscore
	Recibe como parametro la informacion del sql
	Devuelve esta informacion ordenada y formateda.
	'''
	def __init__(self,name,master_surface,x,y,active,ranks_db)->None:
		super().__init__(name,master_surface,x,y,active)

		self.show_ranks = []
		self.ranks_db=ranks_db

		self.puntuaciones_txt = Textos(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2-250,text="TOP 5 RANKING",screen=master_surface,font_size=50)
		self.back_btn = Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2+300,text="VOLVER AL MENU",screen=master_surface,on_click=self.click_back,on_click_param="main_menu_form")

		#if ranks_db != None :
		for i in range(len(ranks_db)):
			self.show_ranks.append(Textos(x=ANCHO_PANTALLA//2-700,y=ALTO_PANTALLA//2.5+i*25,text="{0}".format(i+1),screen=master_surface,font_size=18))
			self.show_ranks.append(Textos(x=ANCHO_PANTALLA//2-380,y=ALTO_PANTALLA//2.5+i*25,text="NOMBRE: {0}".format(ranks_db[i][1]),screen=master_surface,font_size=25))
			self.show_ranks.append(Textos(x=ANCHO_PANTALLA//2-150,y=ALTO_PANTALLA//2.5+i*25,text="VIDAS: {0}".format(ranks_db[i][2]),screen=master_surface,font_size=25))
			self.show_ranks.append(Textos(x=ANCHO_PANTALLA//2+200,y=ALTO_PANTALLA//2.5+i*25,text="PUNTAJE: {0}".format(ranks_db[i][3]),screen=master_surface,font_size=25))
			self.show_ranks.append(Textos(x=ANCHO_PANTALLA//2+400,y=ALTO_PANTALLA//2.5+i*25,text="TIEMPO: {0}".format(ranks_db[i][4]),screen=master_surface,font_size=25))
			self.show_ranks.append(Textos(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2.5+i*25,text="NIVEL: {0}".format(ranks_db[i][5]),screen=master_surface,font_size=25))

		print(self.show_ranks)
				 
		self.lista_widget = [self.puntuaciones_txt,self.back_btn]
	
	

	def click_back(self,parametro):
		self.set_active(parametro)
		click_sound.play(0,450,0)

	def update(self, lista_eventos):
		for aux_boton in self.lista_widget:
			aux_boton.update(lista_eventos)

	def draw(self): 
		super().draw()
		for aux_boton in self.lista_widget:    
			aux_boton.draw()
		for ranks in self.show_ranks:
			ranks.draw()

class FormOpciones(Form):
	'''
	Se crean y setean los botones correspondientes al menu de opciones del juego.
	'''
	def __init__(self,name,master_surface,x,y,active):
		super().__init__(name,master_surface,x,y,active)

	#self.main_menu_ttl = 

		self.music_on = Button(x=ANCHO_PANTALLA//2-80,y=ALTO_PANTALLA//2,text='Music ON',screen=master_surface,on_click=self.click_music_on,font_size=40)
		self.music_off = Button(x=ANCHO_PANTALLA//2+ 120,y=ALTO_PANTALLA//2,text='OFF',screen=master_surface,on_click=self.click_music_off,font_size=40)
		self.back = Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2-150,text='Back to Menu',screen=master_surface,on_click=self.volver,on_click_param="main_menu_form",font_size=40)
		self.lista_widget = [self.music_off,self.music_on,self.back]
		

	def click_music_on(self,paramentro):
		'''
		La accion de este boton activa la musica del juego.
		'''
		click_sound.play(0,450,0)
		pygame.mixer.music.unpause()

	def click_music_off(self,parametro):
		'''
		La accion de este boton pausa la reproduccion de la musica del juego.
		'''
		click_sound.play(0,450,0)
		pygame.mixer.music.pause()

	def volver(self,parametro):
		'''
		Con este boton podemos volver al menu principal, del cual vinimos previamente hacia este menu de opciones.
		'''
		click_sound.play(0,450,0)
		self.set_active(parametro)
	

	def update(self, lista_eventos):
		'''
		detecta el evento del click y procede asi a ejecutar la funcion del boton.
		'''
		for aux_boton in self.lista_widget:
			aux_boton.update(lista_eventos)

	def draw(self): 
		'''
		dibuja los botones en la pantalla
		'''
		super().draw()
		for aux_boton in self.lista_widget:    
			aux_boton.draw()

class FormPausa(Form):

	def __init__(self,name,master_surface,x,y,active):
		super().__init__(name,master_surface,x,y,active)
		'''
		Se setean y crean los botones correspondientes al menu de pausa del juego.
		'''
	#self.main_menu_ttl = 

		self.music_on = Button(x=ANCHO_PANTALLA//2-80,y=ALTO_PANTALLA//2,text='Music ON',screen=master_surface,on_click=self.click_music_on,font_size=40)
		self.music_off = Button(x=ANCHO_PANTALLA//2+ 120,y=ALTO_PANTALLA//2,text='OFF',screen=master_surface,on_click=self.click_music_off,font_size=40)
		self.volver = Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2-100,text='Back to Menu',screen=master_surface,on_click=self.click_back,on_click_param="main_menu_form",font_size=40)

		self.resume_btn = Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2-200,text='Back to Game',screen=master_surface,on_click=self.click_resume,on_click_param="form_start_nivel",font_size=40)
		self.lista_widget = [self.music_off,self.music_on,self.volver,self.resume_btn]

	
	def click_resume(self,parametro):
		'''
		Con este boton salimos del menu de pausa, y volvemos a la pantalla del juego.
		'''
		click_sound.play(0,450,0)
		self.set_active(parametro)

	def click_music_on(self, parametro):
		'''
		La accion de este boton activa la musica del juego.
		'''
		click_sound.play(0,450,0)
		pygame.mixer.music.unpause()

	def click_music_off(self, parametro):
		'''
		La accion de este boton pausa la reproduccion de la musica del juego.
		'''
		click_sound.play(0,450,0)
		pygame.mixer.music.pause()

	def click_back(self,parametro):
		'''
		Con este boton salimos del menu de pausa y regresamos al menu principal del juego.
		'''
		self.set_active(parametro)
	

	def update(self, lista_eventos):
		'''
		detecta el evento del click y procede asi a ejecutar la funcion del boton.
		'''
		for aux_boton in self.lista_widget:
			aux_boton.update(lista_eventos)

	def draw(self): 
		'''
		dibuja los botones en la pantalla
		'''
		super().draw()
		for aux_boton in self.lista_widget:    
			aux_boton.draw()

class FormDeath(Form):
	def __init__(self,name,master_surface,x,y,active):
		super().__init__(name,master_surface,x,y,active)
		'''
		Con este forms se setean los botones correspondientes a aparecer luego de la muerte del personaje principal. 
		'''
		self.music_on = Button(x=ANCHO_PANTALLA//2-80,y=ALTO_PANTALLA//2,text='Music ON',screen=master_surface,on_click=self.click_music_on,font_size=40)
		self.music_off = Button(x=ANCHO_PANTALLA//2+80,y=ALTO_PANTALLA//2,text='OFF',screen=master_surface,on_click=self.click_music_off,font_size=40)
		self.back_btn = Button(x=ANCHO_PANTALLA//2-10,y=ALTO_PANTALLA//2-100,text='BACK TO MENU',screen=master_surface,on_click=self.click_back,on_click_param="main_menu_form",font_size=40)
		self.perdiste_txt = Textos(x=ANCHO_PANTALLA//2-10,y=ALTO_PANTALLA//2-200,text='YOU LOSE :C',screen=master_surface,font_size=50)
		self.retry_btn = Button(x=ANCHO_PANTALLA//2-15,y=ALTO_PANTALLA//2+100,text='TRY AGAIN',screen=master_surface,on_click=self.click_retry,on_click_param="form_start_nivel",font_size=60)
																																							
		self.lista_widget = [self.music_off,self.music_on,self.back_btn,self.retry_btn,self.perdiste_txt]

	def click_retry(self,parametro):
		'''
		Con este boton se vuelve a reiniciar el nivel desde 0 luego de la muerte del personaje.
		'''
		self.set_active(parametro)
		click_sound.play(0,450,0)
		grupo_monedas.draw(screen)
	def click_music_on(self, parametro):
		'''
		La accion de este boton activa la musica del juego.
		'''
		pygame.mixer.music.unpause()
		click_sound.play(0,450,0)
	def click_music_off(self, parametro):
		'''
		La accion de este boton pausa la reproduccion de la musica del juego.
		'''
		pygame.mixer.music.pause()
		click_sound.play(0,450,0)
	def click_back(self,parametro):
		'''
		Con este boton salimos del menu de pausa y regresamos al menu principal del juego.
		'''
		self.set_active(parametro)
		pygame.mixer.music.unpause()

	def update(self, lista_eventos):
		'''
		detecta el evento del click y procede asi a ejecutar la funcion del boton.
		'''
		for aux_boton in self.lista_widget:
			aux_boton.update(lista_eventos)

	def draw(self): 
		'''
		dibuja los botones en la pantalla
		'''
		super().draw()
		for aux_boton in self.lista_widget:    
			aux_boton.draw()
	

class FormWin(Form):
	def __init__(self,name,master_surface,x,y,active):
		super().__init__(name,master_surface,x,y,active)
		self.music_on = Button(x=ANCHO_PANTALLA//2-80,y=ALTO_PANTALLA//2,text='Music ON',screen=master_surface,on_click=self.click_music_on,font_size=40)
		self.music_off = Button(x=ANCHO_PANTALLA//2+80,y=ALTO_PANTALLA//2,text='OFF',screen=master_surface,on_click=self.click_music_off,font_size=40)
		self.back_btn = Button(x=ANCHO_PANTALLA//2-10,y=ALTO_PANTALLA//2-200,text='BACK TO MENU',screen=master_surface,on_click=self.click_back,on_click_param="main_menu_form",font_size=40)
		self.continue_btn = Button(x=ANCHO_PANTALLA//2-10,y=ALTO_PANTALLA//2+200,text='NAME SELECTION',screen=master_surface,on_click=self.click_back,on_click_param="form_name",font_size=40)
		#self.next_btn = Button(x=ANCHO_PANTALLA//2-10,y=ALTO_PANTALLA//2-300,text='Siguiente nivel',screen=master_surface,on_click=self.click_next,on_click_param="form_start_nivel",font_size=40)
		self.ganaste_txt = Textos(x=ANCHO_PANTALLA//2-10,y=ALTO_PANTALLA//2-300,text='YOU WIN!',screen=master_surface,font_size=70)
		
																																					 
		self.lista_widget = [self.music_off,self.music_on,self.back_btn,self.ganaste_txt,self.continue_btn]


	def click_music_on(self, parametro):
		'''
		La accion de este boton activa la musica del juego.
		'''
		click_sound.play(0,450,0)
		pygame.mixer.music.unpause()

	def click_music_off(self, parametro):
		'''
		La accion de este boton pausa la reproduccion de la musica del juego.
		'''
		click_sound.play(0,450,0)
		pygame.mixer.music.pause()

	def click_back(self,parametro):
		'''
		Con este boton salimos del menu de pausa y regresamos al menu principal del juego.
		'''
		click_sound.play(0,450,0)
		self.set_active(parametro)
		pygame.mixer.music.unpause()
	
	# def click_next(self,parametro):
	# 	click_sound.play(0,450,0)
	# 	self.set_active(parametro)
		

	def update(self, lista_eventos):
		'''
		detecta el evento del click y procede asi a ejecutar la funcion del boton.
		'''
		for aux_boton in self.lista_widget:
			aux_boton.update(lista_eventos)

	def draw(self): 
		'''
		dibuja los botones en la pantalla
		'''
		super().draw()
		for aux_boton in self.lista_widget:    
			aux_boton.draw()

class FormLvlSelect(Form):

	def __init__(self,name,master_surface,x,y,active):
		super().__init__(name,master_surface,x,y,active)
		'''
		Con este form se setean los botones correspondientes a la seleccion de niveles del juego.
		'''
		self.is_selected = False
		self.lvl1_btn = Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2-300,text='NIVEL 1',screen=master_surface,on_click=self.seleccion_nivel_1,on_click_param="form_start_nivel",font_size=40)
		self.lvl2_btn = Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2-200,text='NIVEL 2',screen=master_surface,on_click=self.seleccion_nivel_2,on_click_param="form_start_nivel",font_size=40)
		self.lvl3_btn = Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2-100,text='NIVEL 3',screen=master_surface,on_click=self.seleccion_nivel_3,on_click_param="form_start_nivel",font_size=40)
		self.back_btn = Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2,text='VOLVER',screen=master_surface,on_click=self.volver,on_click_param="main_menu_form",font_size=40)
																																					
		self.lista_widget = [self.lvl1_btn,self.lvl2_btn,self.back_btn,self.lvl3_btn]
	
	
	def seleccion_nivel_1(self,parametro):
		'''
		Con este boton se ejecuta el nivel 1 del juego.
		Recibe como parametro si el boton fue presionado
		Devuelve el nivel en cuestion a ser ejecutado.
		'''
		self.set_active(parametro)
		click_sound.play(0,450,0)
		self.selected_lvl = 1
		self.is_selected = True
	def seleccion_nivel_2(self, parametro):
		'''
		Con este boton se ejecuta el nivel 2 del juego.
		Recibe como parametro si el boton fue presionado
		Devuelve el nivel en cuestion a ser ejecutado.
		'''
		self.set_active(parametro)
		click_sound.play(0,450,0)
		self.selected_lvl = 2

		self.is_selected = True
	def seleccion_nivel_3(self, parametro):
		'''
		Con este boton se ejecuta el nivel 3 del juego.
		Recibe como parametro si el boton fue presionado
		Devuelve el nivel en cuestion a ser ejecutado.
		'''
		self.set_active(parametro)
		click_sound.play(0,450,0)
		self.selected_lvl = 3
		self.is_selected = True
	def volver(self,parametro):
		'''
		Nos retorna al menu principal.
		Recibe como parametro si el boton fue presionado.
		Devuelve el forms de menu principal para ser ejecutado.
		'''
		self.set_active(parametro)
	

	def update(self, lista_eventos):
		'''
		detecta el evento del click y procede asi a ejecutar la funcion del boton.
		'''
		for aux_boton in self.lista_widget:
			aux_boton.update(lista_eventos)

	def draw(self): 
		'''
		dibuja los botones en la pantalla
		'''
		super().draw()
		for aux_boton in self.lista_widget:    
			aux_boton.draw()

class FormInsertName(Form):
	'''
	Se setea el botos y se crea el campo de texto dentro del menu de ingreso de nombre de jugador
	Recibe como parametro el nombre ingresado
	Lo devuelve hacia la base de datos, para aplicarlo junto a la informacion del nivel realizado
	'''
	def __init__(self,name,master_surface,x,y,active)->None:
		super().__init__(name,master_surface,x,y,active)

		self.name = False

		self.ingresar_nombre_txt = Textos(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2-250,text="INGRESE SU NOMBRE",screen=master_surface,font_size=50)
		self.text_box = TextBox(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2+250,text=" ",screen=master_surface,font_size=30)
		self.confirm_btn = Button(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2+300,text="CONFIRMAR NOMBRE",screen=master_surface,on_click=self.click_confirm,on_click_param="form_win")    
		self.lista_widget = [self.ingresar_nombre_txt,self.confirm_btn]
	
	

	def click_confirm(self,parametro):
		self.name = True

	def update(self, lista_eventos):
		self.text_box.update(lista_eventos)
		for aux_boton in self.lista_widget:
			aux_boton.update(lista_eventos)

	def draw(self): 
		super().draw()
		for aux_boton in self.lista_widget:    
			aux_boton.draw()
		self.text_box.draw()
		self.writing_text = Textos(x=ANCHO_PANTALLA//2,y=ALTO_PANTALLA//2-20,text="{0}".format(self.text_box._writing.upper()),screen=self.master_surface,font_size=25)
		self.writing_text.draw()

