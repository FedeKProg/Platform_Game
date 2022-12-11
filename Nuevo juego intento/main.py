import pygame
from pygame import mixer
import sys
from player import *

screen = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("El juego de Fede")
clock = pygame.time.Clock()


jugador = Player(200,200,3)

while True:     

	jugador.draw()

	lista_eventos = pygame.event.get()
	for event in lista_eventos:
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.flip()
pygame.quit()