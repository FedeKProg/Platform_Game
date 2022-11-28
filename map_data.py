import pygame
from constantes import *
from enemy import *
from interacciones import *


screen = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
grupo_enemigo = pygame.sprite.Group()
grupo_monedas = pygame.sprite.Group()
grupo_puertas = pygame.sprite.Group()

class Level():
	def __init__(self, data):

		self.lista_items = []
		#cargar imagenes
		imagen_tierra_limites = pygame.image.load("Clase_22/images/tileset/forest/Tiles/10.png")
		imagen_fondo_limite = pygame.image.load("Clase_22/images/tileset/forest/Tiles/2.png")

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
					# self.collition_rect = pygame.Rect(limites_rect)
					# self.ground_collition_rect = pygame.Rect(limites_rect)
					# self.ground_collition_rect.height = GROUND_COLLIDE_H
					item = (limites,limites_rect)
					self.lista_items.append(item)
				if item == 2:
					img = pygame.transform.scale(imagen_fondo_limite, (item_size, item_size))
					img_rect = img.get_rect()
					img_rect.x = contador_columnas * item_size
					img_rect.y = contador_filas * item_size
					# self.collition_rect = pygame.Rect(img_rect)
					# self.ground_collition_rect = pygame.Rect(img_rect)
					# self.ground_collition_rect.height = GROUND_COLLIDE_H
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
				contador_columnas += 1
			contador_filas += 1

		

	def draw_items(self):
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

