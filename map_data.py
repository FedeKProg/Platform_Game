import pygame
from constantes import *
from enemy import *
from interacciones import *


screen = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

class Level():
	def __init__(self, data):

		self.lista_items = []
		#cargar imagenes
		imagen_tierra_limites = pygame.image.load("Recursos/tile/4.png")
		imagen_fondo_limite = pygame.image.load("Recursos/tile/0.png")

		#ubicar imagenes en pantalla, guiandose con columnas y filas
		contador_filas = 0
		for fila in data:
			contador_columnas = 0
			for item in fila:
				if item == 1:
					limites = pygame.transform.scale(imagen_tierra_limites,(item_size,item_size))
					limites_rect = limites.get_rect()
					limites_rect.x = contador_columnas * item_size
					limites_rect.y = contador_filas * item_size
					item = (limites,limites_rect)
					self.lista_items.append(item)
				if item == 2:
					img = pygame.transform.scale(imagen_fondo_limite, (item_size, item_size))
					img_rect = img.get_rect()
					img_rect.x = contador_columnas * item_size
					img_rect.y = contador_filas * item_size
					tile = (img, img_rect)
					self.lista_items.append(tile)
				if item == 3:
					#agregar enemigo en el mapa
					enemigo = Enemy(contador_columnas*item_size,contador_filas*item_size+10)
					grupo_enemigo.add(enemigo)
				if item == 4:
					#agregar moneda en el mapa
					moneda = Moneda(contador_columnas*item_size +(item_size/2),contador_filas*item_size+(item_size/2))
					grupo_monedas.add(moneda)
				if item == 5:
					#agregar puertaa en el mapa
					puerta = Puerta(contador_columnas*item_size,contador_filas*item_size - (item_size/2))
					grupo_puertas.add(puerta)
				if item == 6:
					#agregar puertaa en el mapa
					trampa = Trampa(contador_columnas*item_size + (item_size/2),contador_filas*item_size + (item_size/1.7))
					grupo_trampas.add(trampa)
				contador_columnas += 1
			contador_filas += 1

		

	def draw_items(self,screen):
		for item in self.lista_items:
			screen.blit(item[0], item[1])
			#pygame.draw.rect(screen, (255,255,255), item[1], 2)


# def draw_grid():
# 	for line in range(0,25):
# 		pygame.draw.line(screen, (255,255,255), (2, line * item_size), (ANCHO_PANTALLA, line * item_size))
# 		pygame.draw.line(screen, (255,255,255), (line * item_size,2), (line * item_size, ANCHO_PANTALLA))

# level_data=[
# [0,0,0,0],
# [0,2,2,1],
# [1,2,2,1],
# [1,1,1,1],
# ]

