import pygame as pg
import os
import sys
from settings import *
from level import Level
from player import *


class Game:
    '''Classe que vai ser responsável por rodar o jogo, e por gerenciar o menu, o level, e tudo mais. A classe principal do game. '''   
    
    def __init__(self):
        '''Construtor do game, aqui vai ser inicializado tudo que for necessário para o game rodar. '''
        # general setup
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGTH))
        pg.display.set_caption('Lorem Ipsum')
        self.clock = pg.time.Clock()

        self.level = Level()  # instancia o level
                              # instancia o player

        # sound
        
        main_sound = pg.mixer.Sound('../audio/main.ogg') # carrega o som principal e o coloca em loop
        main_sound.set_volume(0.5)
        main_sound.play(loops=-1)

    def run(self):
        '''Este método vai executar o game em si, e ao mesmo tempo vai dar update nele. Um loop infinito que vai carregar constantemente o level, o player e outras entidades. '''
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_m:
                        pass  # Aqui vai ser adicionado uma tecla pra navegar no menu ou começar o game
                        # self.level.toggle_menu()

            self.screen.fill(WATER_COLOR)
            self.level.run()
            pg.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
