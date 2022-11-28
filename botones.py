import pygame
from constantes import *

screen = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

class Boton():
	def __init__(self,x,y,image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.click = False



	def draw(self):
		reinicio = False
		pos = pygame.mouse.get_pos()
		#chequear posicion mouse
		if self.rect.collidepoint(pos):
			#chequear el clickeo del mouse
			if pygame.mouse.get_pressed()[0] == 1 and self.click == False:
				reinicio = True
				self.click=True
		#chequear que se solto el click [0 = click izquierdo]
		if pygame.mouse.get_pressed()[0] == 0:
			self.click = False

		screen.blit(self.image, self.rect)
		return reinicio