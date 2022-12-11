import pygame
from constantes import *


screen = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

class Moneda(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		imagen_moneda = pygame.image.load("Recursos/files/coin.png")
		self.image=pygame.transform.scale(imagen_moneda,(item_size/2,item_size/2))
		self.rect = self.image.get_rect()
		self.rect.center = (x,y)

class Trampa(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		imagen_trampa = pygame.image.load("Recursos/Traps/Spikes/Idle.png")
		self.image=pygame.transform.scale(imagen_trampa,(item_size/1,item_size/1))
		self.rect = self.image.get_rect()
		self.rect.center = (x,y)
		
class Puerta(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		imagen_puerta = pygame.image.load("Recursos/files/exit.png")
		self.image=pygame.transform.scale(imagen_puerta,(item_size,int(item_size*1.5)))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class Balas(pygame.sprite.Sprite):
	def __init__(self, x, y, direccion):
		pygame.sprite.Sprite.__init__(self)
		self.speed = 10
		self.image = pygame.image.load("Recursos/icons/bullet.png")
		self.rect = self.image.get_rect()
		self.rect.center = (x,y)
		self.direccion = direccion
	
	def update(self):
		#move bullet
		self.rect.x += (self.direction * self.speed)
		#check if bullet has gone off screen
		if self.rect.right < 0 or self.rect.left > ANCHO_PANTALLA:
			self.kill()

def escribir(texto,fuente,color,x,y):
	imagen_score = fuente.render(texto,True,color)
	screen.blit(imagen_score,(x,y))

