import pygame as pg
from settings import *

class Tile(pg.sprite.Sprite):
    '''Basicamente um tile é um sprite que vai ser usado para criar o mapa do jogo. Ele vai ser usado para criar os objetos do mapa, e para criar os obstáculos do jogo. Podem existir diversos tipos (grupos) de Tile, seja de obstáculos ou apenas o cenário. '''
    
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pg.image.load('../graphs/grass/grass_1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos) # get_rect() é usado para criar um retangulo que é herdado da classe Surface. Pegamos o arquivo de imagem do Tile e transformamos ele em no retangulo. O topleft é para definir a posição do tile, que vai ser o canto superior esquerdo do tile.
    
    
    