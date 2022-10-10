import pygame

class Level:
    def __init__(self):
        
        #Visible Sprites
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        
    def run(self):
        #Drawn
        pass