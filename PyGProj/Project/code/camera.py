###################### ATENCAO, A CAMERA E INSTANCIADA APENAS NO ARQUIVO level.py usando o grupo visible_sprites, favor manipular ela apenas por esse grupo e nao instanciar ela masi nenhuma vez
import pygame as pg
from settings import WATER_COLOR, CONTROLKEYS
from debug import keydebug

PlayerX_Offset = -27 #tomar cuidado com essa maluquice aqui pq tenho quase ctz q vai quebrar assim q o jogo mudar de resolucao
PlayerY_Offset = -17 #Deus tenha piedade de mim


class CameraGroup(pg.sprite.Group):
    '''Esta classe é uma extensão da classe Group do pygame. Ela vai ser usada para fazer a camera funcionar. Basicamente ela vai ser um grupo de sprites, herdando todas as caracteristicas da classe Group, mas com algumas funções extras. A função custom_draw vai ser usada para desenhar os sprites na tela de uma maneira diferenciada, mudando a posição deles usando um vetor como base, e a função update vai ser usada para dar update nos sprites. '''

    def __init__(self):
        super().__init__()
        #Offset:
        self.display_surface = pg.display.get_surface() #Pega o tamanho da tela, chamado lá no arquivo main e definido nas configurações
        
        self.offset = pg.math.Vector2() #Cria um vetor para ser usado como offset
        
        #Pegamos o centro da camera fazendo a divisão inteira da altura e a largura por 2
        self.half_width = self.display_surface.get_size()[0] // 2 
        self.half_height = self.display_surface.get_size()[1] // 2

        
        #Camera de box:
        self.camera_borders = {'left': 200, 'right': 200, 'top': 100, 'bottom': 100} #bordas da camera
        left = self.camera_borders['left']
        top = self.camera_borders['top']
        
        #largura da camera é a largura da tela menos as bordas
        width = self.display_surface.get_size()[0] - left - self.camera_borders['right'] 
        height = self.display_surface.get_size()[1] - top - self.camera_borders['bottom']
        
        #Cria um retangulo para ser usado como camera
        self.camera_rect = pg.Rect(left, top, width, height)
        
        #Configs do Zoom:
        self.zoom_scale = 1
        self.internal_surface_size = (2500, 2500)
        self.internal_surface = pg.Surface(self.internal_surface_size, pg.SRCALPHA) #Disclaimer rapido, SRCALPHA faz as coisas que são transparentes não serem desenhadas. Tmj
        self.internal_rect = self.internal_surface.get_rect(center = (self.half_width, self.half_height))
        self.internal_surface_size_vector = pg.math.Vector2(self.internal_surface_size)
        self.internal_offset = pg.math.Vector2()
        self.internal_offset.x = self.internal_surface_size[0] // 2 - self.half_width
        self.internal_offset.y = self.internal_surface_size[1] // 2 - self.half_height
        self.mouse_speed = 0.2

        #Configs do chão:
        self.ground_surf = pg.image.load('../graphs/tilemap/map.png').convert_alpha()
        self.ground_rect = self.ground_surf.get_rect(topleft = (0,0))

        #define se a camera esta lockada no player
        self.islocked = True
        
        # velocidade da camera né
        self.camspeed = 1  



    def center_target_camera(self, target): #Aqui a gente vai fazer a camera seguir o player ou qqr target
        if self.islocked == True:
            self.offset.x = target.rect.centerx - self.half_width 
            self.offset.y = target.rect.centery - self.half_height
    def zoom_keyboard(self):
        '''Aqui a gente faz a camera dar zoom usando o teclado. A gente vai usar o teclado para testar a camera, mas a ideia é que a gente use o mouse para dar zoom. Por algum motivo o pygame só deixa usar a roda do mouse lá no main loop... Então não dá pra implementar aqui nesse arquivo. Da uma olhada no arquivo main pra ver o input da camera com zoom'''
        keys = pg.key.get_pressed()
        if keys [CONTROLKEYS['camera_zoom_reset']]:
            self.zoom_scale = 1
        if keys[CONTROLKEYS['camera_zoom_in']] and (self.zoom_scale < 2): #mano tem q passar esses numeros pro settings.py
                self.zoom_scale += 0.01
        if keys[CONTROLKEYS['camera_zoom_out']] and (self.zoom_scale > 0.52):
                self.zoom_scale -= 0.01
    
    def zoom_scroll(self, event):
                if event.type == pg.MOUSEWHEEL: 
                    if (event.y > 0) and (self.zoom_scale < 2):
                        self.zoom_scale += 0.05
                    if (event.y < 0) and (self.zoom_scale > 0.52):
                        self.zoom_scale -= 0.05
        
        
        
        
    # #aqui comeca meu sofrimento tentando criar uma camera independente do player, vou documentar cuidadosamente pra ver se eu consigo entender o que eu fiz

    def freecam(self):
        keydebug('X:', self.offset.x + PlayerX_Offset + self.half_width)
        keydebug('Y:', self.offset.y + PlayerY_Offset + self.half_height)
        keys = pg.key.get_pressed()

        if self.islocked == False:
            if keys[CONTROLKEYS['camera_speed_up']] and self.camspeed < 10:
                self.camspeed += 0.5
            if keys[CONTROLKEYS['camera_speed_down']] and self.camspeed > 0.5:
                self.camspeed -= 0.5
            if keys[CONTROLKEYS['camera_right']]: ##detectando a tecla pressionada pra mover a camera lesgo
                # ok,nota para quem for mexer na camera no futuro, para achar a psoicao da camera real, em relacao ao player, tem q dividir pela metade de altura e largura, pq sim, como foi feito aqui
                self.offset.x = self.offset.x + self.camspeed
                print('X:', self.offset.x)
            if keys[CONTROLKEYS['camera_left']]:
                self.offset.x = self.offset.x - self.camspeed
                print('X:', self.offset.x)
            if keys[CONTROLKEYS['camera_up']]:
                self.offset.y = self.offset.y - self.camspeed
                print('Y:', self.offset.y)
            if keys[CONTROLKEYS['camera_down']]:
                self.offset.y = self.offset.y + self.camspeed
                print('Y:', self.offset.y)

    def lockunlock(self):
        keys = pg.key.get_pressed()
        if self.islocked == True and keys[CONTROLKEYS['camera_unlock']]:
            self.islocked = False
        if self.islocked == False and keys[CONTROLKEYS['camera_lock']]:
                self.islocked = True



    
    
    def custom_draw(self, player):
        self.lockunlock() ##para debug apenas
        self.freecam()
        self.center_target_camera(player) #Chama a função que vai centralizar a camera no player
        self.zoom_keyboard()
        pg.draw.rect(self.display_surface, (255,0,0), self.camera_rect, 5) #debug camera rect. Cria um retangulo que mostra as dimensoes da camera
        
        self.internal_surface.fill(WATER_COLOR) #Por algum motivo maluco se a gente não fizer isso, a camera fica com umas linhas pretas. Não sei o motivo, mas isso resolve.
        
        ground_offset = self.ground_rect.topleft - self.offset + self.internal_offset
        self.internal_surface.blit(self.ground_surf, ground_offset)
        
        for sprite in sorted (self.sprites(), key=lambda sprite: sprite.rect.centery): 
            offset_rect = sprite.rect.topleft - self.offset + self.internal_offset
            self.internal_surface.blit(sprite.image, offset_rect)
        
        scaled_surface = pg.transform.scale(self.internal_surface, self.internal_surface_size_vector * self.zoom_scale)
        scaled_rect = scaled_surface.get_rect(center = (self.half_width, self.half_height))
            
        self.display_surface.blit(scaled_surface, scaled_rect)
        
        
        
        