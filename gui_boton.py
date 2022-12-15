import pygame
from pygame.locals import *
from gui_widget import Widget
from constantes import *

 
class Button(Widget):
    '''
    En esta clase se setean los funcionamientos y el display de todos los botones dentro del juego
    Recibe los distintos formatos y ubicacion del mismo
    Devuelve el boton listo para ser usado en pantalla 
    '''
    def __init__(self,x,y,text,screen,on_click=None,on_click_param=None,font_size=60):
        super().__init__(x,y,text,screen,font_size)
        pygame.font.init()
        self.font = pygame.font.SysFont("Sans Serif",self.font_size)
        self.image = self.font.render(self.text,True,(255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        #self.on_click_sound = pygame.mixer.Sound()
        self.on_click = on_click
        self.on_click_param = on_click_param
        self._text = text    
    
    def button_pressed(self):
        mouse_pos = pygame.mouse.get_pos()

        #coll
        if(self.rect.collidepoint(mouse_pos)):
            if(pygame.mouse.get_pressed()[0] == 1):
                self.on_click(self.on_click_param)
    
    def draw(self):
        super().draw()
        
    def update(self,lista_eventos):
        self.draw()
        self.button_pressed()

class Textos(Widget):
    '''
    En esta clase se setean el formato y la fuente de los textos a ser usados y mostrados en el juego.
    Recibe como parametro la ubicacion del mismo.
    Devuelve el texto formateado correspondientemente.
    '''
    def __init__(self,x,y,text,screen,on_click=None,on_click_param=None,font_size=20):
        super().__init__(x,y,text,screen,font_size)
        pygame.font.init()
        self.font = pygame.font.SysFont("Times New Roman",self.font_size)
        self.image = self.font.render(self.text,True,(255,0,0))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.on_click = on_click
        self.on_click_param = on_click_param
        self._text = text

    
    
    def button_pressed(self):
        if(self.on_click_param == None):
            pass
            #poner el play del sonido en el momento que clickea

    
    def draw(self):
        super().draw()
        
    def update(self,lista_eventos):
        self.draw()
        self.button_pressed()

class TextBox(Widget):
    def __init__(self,x,y,text,screen,on_click=None,on_click_param=None,font_size=20):
        super().__init__(x,y,text,screen,font_size)
        self.font = pygame.font.SysFont("San Serif",font_size)
        self.image = self.font.render(text,True,(255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.on_click = on_click
        self.on_click_param = on_click_param
        self.write_on =True
        self._writing=""
        self.img_writing = self.font.render(self._writing,True,(255,255,0))
        self.rect_writing = self.img_writing.get_rect()
        self.rect_writing.center = (x,y)

    def write(self, event_list):
        for event in event_list:
                        
            if (event.type == pygame.KEYDOWN and self.write_on):
                
                if event.key == pygame.K_BACKSPACE:
                    self._writing = self._writing[:-1]
                else:
                    self._writing += event.unicode


    def draw(self):
        super().draw()
        self.image.blit(self.screen,(self.rect_writing.x,self.rect_writing.y))

    def update(self,event_list):
        self.draw()
        self.write(event_list) 