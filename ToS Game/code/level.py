import pygame as pg
from settings import TILESIZE
from tile import Tile
from player import Player
from camera import CameraGroup
from debug import debug
from support import import_csv , import_folder
class Level:

    def __init__(self):
        
        # Grupo de sprites:
        
        self.visible_sprites = CameraGroup() # Grupo de sprites visíveis na tela, tudo que for visivel vai ter esse subgrupo. O subgrupo vai ser usado para fazer a camera funcionar.
        self.obstacle_sprites = pg.sprite.Group() # Grupo de sprites que são obstáculos, ou seja, não podem ser atravessados e terão colisão com o player. Tudo que tiver essa propriedade vai ter esse subgrupo.
        self.display_surface = pg.display.get_surface() 
        
        #logica do mapa
        self.levelstarted = False
        self.levelnow = 0

        #Sprite Setup:
        self.create_map()
        

    def create_map(self):
        
        #inicio dos dicionários csv
        layouts = {
            'invisible': import_csv('../map/csvs/_invis.csv'),
            'objects': import_csv('../map/csvs/_objects.csv'),
            'player': import_csv('../map/csvs/_player.csv'),
        }
        graphics = {
            'objects': import_folder('../graphs/objects'),
            'invis': import_folder('../graphs/invis'),
            'player': import_folder('../graphs/playerdefault'),
        }
        
        
        for style,layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':  # -1 no csv exportado significa que nao tem nada no tile, entao ele nao vai ser nem lido e nem criado
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        
                        if style == 'invis': #leia o comentario de baixo, e meio autoexplicativo
                            Tile((x,y),[self.obstacle_sprites], 'invis') #cria um tile invisivel, que vai ser usado como obstaculo
                        
                        if style == 'objects':
                            
                            surf = graphics['objects'][int(col)]
                            
                            Tile((x, y), [self.visible_sprites,self.obstacle_sprites], 'object', surf)

                        if style == 'player':
                            self.player = Player((x,y), [self.visible_sprites], self.obstacle_sprites)

    def run(self):
        if self.levelstarted == False:
            self.visible_sprites.mapset('../map/map.png') # carrega o mapa real, essa funcao pode ser usada pra mudar ele, eu espero
            self.levelstarted = True
        
        self.visible_sprites.custom_draw(self.player)
        
        self.visible_sprites.update()
        
        
        keys = pg.key.get_pressed() ## DEBUG PARA MJUDAR DE LEVEL, AINDA VOU TRABALHAR EM COMO MUDAR OS SPRITES @GabriWar
        if keys[pg.K_F3]:
            self.visible_sprites.mapset('../map/placeholder.png')
        if keys[pg.K_F4]:
            self.visible_sprites.mapset('../map/map.png')
