import pygame
import json
from map_data import *


class MapCreator():
    def __init__(self,nivel):
        '''
        So proceder a cargar los niveles guardados en archivos json. 
        Dependiendo del numero del nivel, se abre y utiliza el archivo correspondiente al mismo.
        '''
        self.nivel = nivel
        self.timer_nivel = 0
        if nivel == 1:
            self.map_data = self.CargarJson("nivel_1.json")
            # self.lista_map.append(self.map_data)
            self.nivel_mapa = "level_1_data"
            self.timer_nivel = 30
        if nivel == 2:
            self.map_data = self.CargarJson("nivel_2.json")
            # self.lista_map.append(self.map_data)
            self.nivel_mapa = "level_2_data"
            self.timer_nivel = 60
        if nivel == 3:
            self.map_data = self.CargarJson("nivel_3.json")
            # self.lista_map.append(self.map_data)
            self.nivel_mapa = "level_3_data"
            self.timer_nivel = 90
        

    def CargarJson(self,file):
        '''
        Funcion para cargar y leer los archivos json.
        '''
        with open(file, 'r') as archivo:
            self.map_data = json.load(archivo)
        return self.map_data

    def get_items(self):
        '''
        Funcion para obtener y listar los items del juego, para luego ser procesados y ejecutados en el juego.
        '''
        map_list_dic = self.map_data[self.nivel_mapa]
        self.map_list = []
        for items in map_list_dic:
            item = items
            self.map_list.append(item)

        return self.map_list

    def get_timer_sec(self):
        '''
        Funcion para obtener el tiempo del juego.
        '''
        return self.timer_nivel
        
    # def vaciar_lista(self):
    #     self.map_list.clear()
    #     return self.map_list
        

# level_1_data = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
#     [1, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 3, 0, 0, 4, 1], 
#     [1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 1], 
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
#     [1, 0, 0, 0, 0, 0, 0, 4, 0, 0, 3, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
#     [1, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
#     [1, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 3, 0, 0, 4, 1], 
#     [1, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 1], 
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
#     [1, 0, 0, 0, 0, 0, 0, 4, 0, 0, 3, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
#     [1, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
#     [1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
#     [1, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 1], 
#     [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 4, 0, 3, 0, 0, 1], 
#     [1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 1]
#     ]