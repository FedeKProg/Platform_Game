import pygame
from constantes import *


screen = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

class Moneda(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		imagen_moneda = pygame.image.load("practica_tp/Recursos/files/coin.png")
		self.image=pygame.transform.scale(imagen_moneda,(item_size/2,item_size/2))
		self.rect = self.image.get_rect()
		self.rect.center = (x,y)
		
class Puerta(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		imagen_puerta = pygame.image.load("practica_tp/Recursos/files/exit.png")
		self.image=pygame.transform.scale(imagen_puerta,(item_size,int(item_size*1.5)))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

def escribir(texto,fuente,color,x,y):
	imagen_score = fuente.render(texto,True,color)
	screen.blit(imagen_score,(x,y))

