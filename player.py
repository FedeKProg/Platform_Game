import pygame
from constantes import *
from auxiliar import Auxiliar
from map_data import *
from Level_setup import *

pygame.mixer.pre_init()


class Player():
	def __init__(self,x,y):
		self.walk_r_list = []
		self.walk_l_list = []
		self.attack_r_list = []
		self.attack_l_list = []
		self.index = 0
		self.vidas = 5
		self.contador = 0
		#self.contador_attack = 0
		#lista animacion de caminata
		for frame in range(0,5):
			walk_r = pygame.image.load(f"Recursos/warrior_woman_01/2_WALK_00{frame}.png")
			walk_r = pygame.transform.scale(walk_r,(80,80))
			walk_l = pygame.transform.flip(walk_r,True,False)
			self.walk_r_list.append(walk_r)
			self.walk_l_list.append(walk_l)
		#lista animacion golpe
		# for frame in range(0,5):
		# 	attack_r = pygame.image.load(f"Recursos/warrior_woman_01/5_ATTACK_00{frame}.png")
		# 	attack_r = pygame.transform.scale(attack_r,(80,80))
		# 	attack_l = pygame.transform.flip(attack_r,True,False)
		# 	self.attack_r_list.append(attack_r)
		# 	self.attack_l_list.append(attack_l)
		self.death_image = pygame.image.load("Recursos/warrior_woman_01/7_DIE_005.png")
		self.walk = self.walk_r_list[self.index]
		self.rect = self.walk.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.ancho = self.walk.get_width()
		self.alto = self.walk.get_height()
		# self.attack = self.attack_r_list[self.index]
		# self.attack.rect = self.attack.get_rect()
		# self.attack_rect.x = x
		# self.attack_rect.y = y
		# self.ancho_attack = self.attack.get_width()
		# self.alto_attack = self.attack.get_height()
		self.jump_speed = 0
		self.jump = False
		#self.shoot= False
		self.shoot_cooldown = 0
		self.direccion = 0
		self.on_platform = True

	def update(self,game_over,lista_items):
		updt_x = 0
		updt_y = 0
		animation_cooldown = 10
		attack_cooldown = 40
		#acciones y movimientos del personaje
		if game_over == 0:
			key = pygame.key.get_pressed()
			if key[pygame.K_LEFT]:
				updt_x -= 2
				self.contador += 1
				self.direccion = -1
			if key[pygame.K_RIGHT]:
				updt_x += 2
				self.contador += 1
				self.direccion = 1
			# if key[pygame.K_UP]:
			# 	self.contador_attack += 1
			# 	self.direccion_attack = 1
			if key[pygame.K_s]:	
				self.shoot = True
			if key[pygame.K_s] == False:	
				self.shoot = False
			if key[pygame.K_SPACE] and self.jump == False and self.on_platform==True:
				#agrega musica
				musica_salto.play()
				self.jump_speed = -18
				self.jump = True
			if key[pygame.K_SPACE] == False:
				self.jump = False
			if key[pygame.K_RIGHT] == False and key[pygame.K_LEFT] == False:
				self.contador = 0
				self.index = 0
				if self.direccion == 1:
					self.walk = self.walk_r_list[self.index]
				if self.direccion == -1:
					self.walk = self.walk_l_list[self.index]
			# if key[pygame.K_UP] == False:
			# 	self.contador_attack = 0
			# 	self.index = 0
			# 	if self.direccion == 1:
			# 		self.attack = self.attack_r_list[self.index]
			# 	if self.direccion == -1:
			# 		self.attack = self.attack_l_list[self.index]				

			#animacion caminata
			if self.contador > animation_cooldown:
				self.contador = 0
				self.index += 1
				if self.index >= len(self.walk_r_list):
					self.index = 0
				if self.direccion == 1:
					self.walk = self.walk_r_list[self.index]
				if self.direccion == -1:
					self.walk = self.walk_l_list[self.index]
			#animacion ataque
			# if self.contador_attack > attack_cooldown:
			# 	self.contador_attack = 0
			# 	self.index += 1
			# 	if self.index >= len(self.attack_r_list):
			# 		self.index = 0
			# 	if self.direccion == 1:
			# 		self.attack = self.attack_r_list[self.index]
			# 	if self.direccion == -1:
			# 		self.attack = self.attack_l_list[self.index]

			#manejar gravedad
			self.jump_speed += 1   
			if self.jump_speed > 2:
				self.jump_speed = 2

			updt_y += self.jump_speed

			#chequear colisiones
			self.on_platform = False
			for item in lista_items:
				if item[1].colliderect(self.rect.x + updt_x, self.rect.y, self.ancho, self.alto):
					updt_x = 0
				if item[1].colliderect(self.rect.x, self.rect.y + updt_y, self.ancho,self.alto):
					#colision desde abajo
					if self.jump_speed <= 0:
						updt_y = item[1].bottom - self.rect.top
						self.jump_speed = 0
					elif self.jump_speed >= 0:
						updt_y = item[1].top - self.rect.bottom
						self.jump_speed = 0
						self.on_platform = True
			#colision con el enemigo
			if pygame.sprite.spritecollide(self, grupo_enemigo, False):
				#agregar musica
				musica_game_over.play()
				self.vidas -= 1
				if self.vidas == 0:
					game_over = -1

			#colision con la puerta
			if pygame.sprite.spritecollide(self, grupo_puertas, False):
				game_over = 1

			#updatear las coordenada del jugador
			self.rect.x += updt_x
			self.rect.y += updt_y

		elif game_over == -1:
			self.image = self.death_image
			if self.rect.y > 200:
				self.rect.y += 5
		return game_over

	# def score_jugador(self):
	# 	self.score = 0
	# 	if pygame.sprite.spritecollide(self,grupo_monedas,True):
	# 		self.score +=10
	# 	escribir("SCORE:" + str(score),fuente_score,white,item_size-10,10)

	
	def shoot(self):
		if self.shoot_cooldown == 0:
			self.shoot_cooldown = 20
			bullet = Balas(self.rect.centerx + (0.75 * self.rect.size[0] * self.direction), self.rect.centery, self.direction)
			grupo_balas.add(bullet)
			#reduce ammo
			self.ammo -= 1
			#shot_fx.play()


	def reset(self,x,y):
		#para resetear el jugador despues del game over
		self.__init__(x,y)

	def draw(self):
		screen.blit(self.walk,self.rect)
		#pygame.draw.rect(screen,(255,255,255),self.rect,2)


