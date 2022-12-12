import pygame
from pygame.locals import *

class Widget:
    '''
    Clase madre, en la cual se hereda el formato de texto para ser usado en la clase de Boton y en la de Textos
    '''
    def __init__(self,x,y,text,screen,font_size=60):
        self.font_size = font_size
        self.screen = screen
        self.text = text

        self.x = x
        self.y = y

    def draw(self):
        self.screen.blit(self.text_image,self.rect)