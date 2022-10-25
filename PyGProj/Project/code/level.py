import pygame as pg
from settings import WORLD_MAP , TILESIZE
from tile import Tile
from player import Player
from camera import CameraGroup
from support import *
from debug import *
from game_data import *

class Level:
    '''Essa classe basicamente é o coração do jogo. O level é uma espécie de conteiner que vai conter todos os objetos/sprites do jogo, Sejam eles visiveis ou não. O funcionamento divide os sprites em duas classes, sprites visiveis e sprites de obstáculo, cada um com suas propriedades. Um obstáculo pode ter os dois grupos ao mesmo tempo, como por exemplo uma árvore com hitbox, que vai ter colisão e vai ser desenhada na tela. '''

    def __init__(self, level_data, surface):
        
        # Grupo de sprites:
        
        self.visible_sprites = CameraGroup() # Grupo de sprites visíveis na tela, tudo que for visivel vai ter esse subgrupo. O subgrupo vai ser usado para fazer a camera funcionar.

        
        self.obstacle_sprites = pg.sprite.Group() # Grupo de sprites que são obstáculos, ou seja, não podem ser atravessados e terão colisão com o player. Tudo que tiver essa proprieadade vai ter esse subgrupo.


        self.display_surface = pg.display.get_surface() # Getter do tamanho da tela: (é mais prático criar isto aqui para deixar a possibilidade de mudar o tamanho da tela no futuro pelo menu do game.)

        
        # Criando o mapa:
        terrain_layout = import_csv_layout(level_data['terrain']) # Importando o layout do terreno
        
        self.terrain_sprites = self.create_map(terrain_layout, 'terrain')
        
    
        

    def create_map(self, layout, tile_type):
        '''Este método vai criar o mapa do jogo. Basicamente ele vai criar um grid de tiles, e vai colocar os tiles no lugar certo. A ideia é que o mapa seja criado a partir de um arquivo de texto, que vai ser lido e vai criar o mapa. O mapa nada mais é que uma matriz de tiles, onde cada tile vai ter uma posição e um tipo. A posição dos tiles vai ser definida pelo arquivo de texto, e o tipo vai ser definido pelo arquivo de texto também. Cada posição vai variar de acordo com o tamanho do Tile (no nosso caso, 64). Em suma, no local 0,0 vai ter um tile, no local 64,0 vai ter outro tile, e assim por diante. '''
        
        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                if col == '-1':
                    x = col_index * TILESIZE
                    y = row_index * TILESIZE
                    if type == 'terrain':
                        Tile((x,y),[self.visible_sprites, self.obstacle_sprites], (TILESIZE,TILESIZE))
                if col == '0':
                    self.player = Player((x,y), [self.visible_sprites], self.obstacle_sprites)
        

    def run(self):
        '''Este método vai executar o level em si, e ao mesmo tempo vai dar update nele. Basicamente vai desenhar as coisas na tela. '''
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.obstacle_sprites.draw(self.display_surface)
        debug(self.player.hitbox)
