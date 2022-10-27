import pygame as pg

from settings import TILESIZE

class Tile(pg.sprite.Sprite):

    
    def __init__(self, pos, groups,sprite_type,surface= pg.Surface((TILESIZE,TILESIZE))): #surface defaulta pra um bloco com os valores settados no settings.py
        
        super().__init__(groups)
        self.sprite_type = sprite_type
        
        self.image = surface
        
        if sprite_type == 'object':
            self.rect = self.image.get_rect(topleft=(pos[0],pos[1] - TILESIZE))
        
        else:
            self.rect = self.image.get_rect(topleft=pos) 
        
        self.hitbox = self.rect.inflate(0, -10) 
    
