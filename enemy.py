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

	def update(self):
		
		#setear movimiento enemigo
		self.rect.x += self.direccion
		self.contador_movimiento += 1
		if abs(self.contador_movimiento) > 40:
			self.direccion *= -1
			self.contador_movimiento *= -1




