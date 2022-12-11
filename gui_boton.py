import pygame
from pygame.locals import *
from gui_widget import Widget

 
class Button(Widget):
    def __init__(self,x,y,text,screen,on_click=None,on_click_param=None,font_size=60):
        super().__init__(x,y,text,screen,font_size)
        pygame.font.init()
        self.font = pygame.font.SysFont("Sans Serif",self.font_size)
        self.text_image = self.font.render(self.text,True,(255,0,0))
        self.rect = self.text_image.get_rect()
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
    def __init__(self,x,y,text,screen,on_click=None,on_click_param=None,font_size=20):
        super().__init__(x,y,text,screen,font_size)
        pygame.font.init()
        self.font = pygame.font.Font(r"Dungeon Quests Italic.otf",self.font_size)
        self.text_image = self.font.render(self.text,True,(255,0,255))
        self.rect = self.text_image.get_rect()
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