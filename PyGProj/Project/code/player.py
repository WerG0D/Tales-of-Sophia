import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pg.image.load('../graphs/test/player.png')
        self.rect = self.image.get_rect(topleft=pos)