from cgi import test
import pygame as pg
from settings import WORLD_MAP , TILESIZE
from tile import Tile
from player import Player
from camera import CameraGroup
from debug import debug
from support import import_csv , import_folder

class Level:
    '''Essa classe basicamente é o coração do jogo. O level é uma espécie de conteiner que vai conter todos os objetos/sprites do jogo, Sejam eles visiveis ou não. O funcionamento divide os sprites em duas classes, sprites visiveis e sprites de obstáculo, cada um com suas propriedades. Um obstáculo pode ter os dois grupos ao mesmo tempo, como por exemplo uma árvore com hitbox, que vai ter colisão e vai ser desenhada na tela. '''

    def __init__(self):
        
        # Grupo de sprites:
        
        self.visible_sprites = CameraGroup() # Grupo de sprites visíveis na tela, tudo que for visivel vai ter esse subgrupo. O subgrupo vai ser usado para fazer a camera funcionar.

        
        self.obstacle_sprites = pg.sprite.Group() # Grupo de sprites que são obstáculos, ou seja, não podem ser atravessados e terão colisão com o player. Tudo que tiver essa proprieadade vai ter esse subgrupo.


        self.display_surface = pg.display.get_surface() # Getter do tamanho da tela: (é mais prático criar isto aqui para deixar a possibilidade de mudar o tamanho da tela no futuro pelo menu do game.)

        
        #Sprite Setup:
        self.create_map()
        

    def create_map(self):
        '''Este método vai criar o mapa do jogo. Basicamente ele vai criar um grid de tiles, e vai colocar os tiles no lugar certo. A ideia é que o mapa seja criado a partir de um arquivo de texto, que vai ser lido e vai criar o mapa. O mapa nada mais é que uma matriz de tiles, onde cada tile vai ter uma posição e um tipo. A posição dos tiles vai ser definida pelo arquivo de texto, e o tipo vai ser definido pelo arquivo de texto também. Cada posição vai variar de acordo com o tamanho do Tile (no nosso caso, 64). Em suma, no local 0,0 vai ter um tile, no local 64,0 vai ter outro tile, e assim por diante. '''
        #criando um dicionario dos layers do mapa? eu acho, gabriel do futuro aqui, eu acho nao, eu tenho certeza, essa funcao basicamnete importa o arquivo csv e retorna uma matriz com os valores do arquivo pra noz usar como mapa
        layouts = {
            'invis': import_csv('../map/testmapwow_terrain.csv'),
            'terrain': import_csv('../map/testmapwow_terrain.csv'),
            'objects': import_csv('../map/testmapwow_objects.csv'),
            'player': import_csv('../map/testmapwow_player.csv'),
        }
        graphics = {
            'objects': import_folder('../graphics/objects'),
        }
        for style,layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':  # -1 no csv exportado significa que nao tem nada no tile, entao ele nao vai ser nem lido e nem criado
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'invis': #leia o comentario de baixo, e meio autoexplicativo
                            Tile((x,y),[self.visible_sprites, self.obstacle_sprites], 'invis') #cria um tile invisivel, que vai ser usado como obstaculo
                        if style == 'terrain':
                            pass
                        if style == 'ground':
                            pass
                        if style == 'objects':
                            pass
                        if style == 'player':
                            pass
        self.player = Player((500, 500), [self.visible_sprites], self.obstacle_sprites) # Cria o player no mapa, 500 500 e a posicao x e y dele, basico

    def run(self):
        '''Este método vai executar o level em si, e ao mesmo tempo vai dar update nele. Basicamente vai desenhar as coisas na tela. '''
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        debug(self.player.hitbox)


        
        
        #         if col  == 'x':
        #             Tile((x,y),[self.visible_sprites, self.obstacle_sprites])
        #         if col == 'p':
        #             self.player = Player((x,y), [self.visible_sprites], self.obstacle_sprites)
