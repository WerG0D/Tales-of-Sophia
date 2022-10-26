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

        
        self.obstacle_sprites = pg.sprite.Group() # Grupo de sprites que são obstáculos, ou seja, não podem ser atravessados e terão colisão com o player. Tudo que tiver essa proprieadade vai ter esse subgrupo.


        self.display_surface = pg.display.get_surface() 

        
        #Sprite Setup:
        self.create_map()
        

    def create_map(self):
        
        #inicio dos dicionários csv
        layouts = {
            'invis': import_csv('../map/testmapwow_terrain.csv'),
            'terrain': import_csv('../map/testmapwow_terrain.csv'),
            'objects': import_csv('../map/testmapwow_objects.csv'),
            'player': import_csv('../map/testmapwow_player.csv'),
        }
        graphics = {
            'objects': import_folder('../graphs/objects'),
        }
        
        
        for style,layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':  # -1 no csv exportado significa que nao tem nada no tile, entao ele nao vai ser nem lido e nem criado
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        
                        if style == 'invis': #leia o comentario de baixo, e meio autoexplicativo
                            Tile((x,y),[self.obstacle_sprites], 'invis') #cria um tile invisivel, que vai ser usado como obstaculo
                        
                        if style == 'terrain':
                            pass
                        
                        if style == 'ground':
                            pass
                        
                        if style == 'objects':
                            
                            surf = graphics['objects'][0] # surf = graphics['objects'][int(col)]
                            
                            '''ATENCAO GABRIEL DO FUTURO, AQUI VAI SER CRIADO O SPRITE DO OBJETO, AGORA VOCE TA USANDO SO UM 0 ALI EM CIMA ENTrE CAIXAS PQ SO TE 1 UNICO SPRITE, SE ADICIONAR OUTROs vai ferrar o codigo, FAVOR MEXER AQUI NO FUTURO'''
                            
                            Tile((x, y), [self.visible_sprites,self.obstacle_sprites], 'object', surf)

                        if style == 'player':
                            self.player = Player((x,y), [self.visible_sprites], self.obstacle_sprites)

    def run(self):
        
        self.visible_sprites.custom_draw(self.player)
        
        self.visible_sprites.update()
        
        debug(self.player.hitbox)
