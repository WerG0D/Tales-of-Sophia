import pygame as pg
import os
import sys
from settings import *
from level import Level 
from player import *
from camera import CameraGroup
class Game: 
    
    def __init__(self):
        # general setup
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGTH))
        pg.display.set_caption('Lorem Ipsum')
        self.clock = pg.time.Clock()
        pg.event.set_grab(True)

        self.level = Level()  # instancia o level
        self.camera_group = CameraGroup() # instancia o grupo de camera
        
        # sound
        
        '''main_sound = pg.mixer.Sound('../audio/main.ogg') # carrega o som principal e o coloca em loop
        main_sound.set_volume(0.5)
        main_sound.play(loops=-1)
        '''
    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()
                    
                if event.type == pg.MOUSEWHEEL: #ISSO DEVERIA FUNCIONAR, MAS NÃO FUNCIONA
                    self.camera_group.zoom_scale += event.y * 0.03

            self.screen.fill(WATER_COLOR)
            self.level.run()
            pg.display.update()
            self.clock.tick(FPS)
            keys = pg.key.get_pressed()
            if keys[pg.K_o]:
                print(self.level.player.rect.x, self.level.player.rect.y) #printa a posição do player
                print() #debug flag do vscode


if __name__ == '__main__':
    game = Game()
    game.run()
