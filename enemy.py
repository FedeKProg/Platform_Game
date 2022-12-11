import pygame
from constantes import *

screen = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

class Enemy(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("Recursos/files/blob.png")
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.direccion = 1
		self.contador_movimiento = 0
		self.head_collition_rect = pygame.Rect(self.rect.x + self.rect.w / 4.5, self.rect.y-5,self.rect.w/1.8,self.rect.h/5)
		

	def update(self):
		
		#setear movimiento enemigo
		self.rect.x += self.direccion
		self.contador_movimiento += 1
		if abs(self.contador_movimiento) > 50:
			self.direccion *= -1
			self.contador_movimiento *= -1
	def draw(self):
		pygame.draw.rect(screen,(255,255,255),self.rect,2)
	




