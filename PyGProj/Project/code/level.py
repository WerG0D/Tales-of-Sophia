import pygame as pg
from settings import *
from tile import Tile
from player import Player

class Level:
    '''Essa classe basicamente é o coração do jogo. O level é uma espécie de conteiner que vai conter todos os objetos/sprites do jogo, Sejam eles visiveis ou não. O funcionamento divide os sprites em duas classes, sprites visiveis e sprites de obstáculo, cada um com suas propriedades. Um obstáculo pode ter os dois grupos ao mesmo tempo, como por exemplo uma árvore com hitbox, que vai ter colisão e vai ser desenhada na tela. '''

    def __init__(self):
        
        # Grupo de sprites:
        
        self.visible_sprites = pg.sprite.Group() # Grupo de sprites visíveis na tela, tudo que for visivel vai ter esse subgrupo

        
        self.obstacle_sprites = pg.sprite.Group() # Grupo de sprites que são obstáculos, ou seja, não podem ser atravessados e terão colisão com o player. Tudo que tiver essa proprieadade vai ter esse subgrupo.


        self.display_surface = pg.display.get_surface() # Getter do tamanho da tela: (é mais prático criar isto aqui para deixar a possibilidade de mudar o tamanho da tela no futuro pelo menu do game.)

        
        #Sprite Setup:
        self.create_map()
        

    def create_map(self):
        '''Este método vai criar o mapa do jogo. Basicamente ele vai criar um grid de tiles, e vai colocar os tiles no lugar certo. A ideia é que o mapa seja criado a partir de um arquivo de texto, que vai ser lido e vai criar o mapa. O mapa nada mais é que uma matriz de tiles, onde cada tile vai ter uma posição e um tipo. A posição dos tiles vai ser definida pelo arquivo de texto, e o tipo vai ser definido pelo arquivo de texto também. Cada posição vai variar de acordo com o tamanho do Tile (no nosso caso, 64). Em suma, no local 0,0 vai ter um tile, no local 64,0 vai ter outro tile, e assim por diante. '''
        
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col  == 'x':
                    Tile(pos=(x,y), groups=[self.visible_sprites, self.obstacle_sprites])
                if col == 'p':
                    self.player = Player((x,y), [self.visible_sprites], self.obstacle_sprites)
        

    def run(self):
        '''Este método vai executar o level em si, e ao mesmo tempo vai dar update nele. Basicamente vai desenhar as coisas na tela. '''

        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()