import pygame as pg
from settings import *
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
        
    def center_target_camera(self, target):
        '''Essa é a camera que centraliza o player. Usamos a posição dele como offset, fazendo com que a camera sempre deixe o player no centro da tela. Essa opção por hora não tá sendo interessante pro que eu to pensando, mas não é um caso de YAGNI.'''
        
        self.offset.x = target.rect.centerx - self.half_width 
        self.offset.y = target.rect.centery - self.half_height

        print(self.offset)

    def box_target_camera(self, target):
        '''Aqui as coisas ficam um pouco complexas, mas basicamente o que acontece é que a camera vai seguir o player, mas só vai seguir ele se ele estiver fora da camera, ou seja, se ele estiver dentro da camera, a camera não vai se mover. Mentira, não é nem um pouco complexo é só eu fznd drama'''
        
        if target.rect.left < self.camera_rect.left:
            self.camera_rect.left = target.rect.left
        if target.rect.right > self.camera_rect.right:
            self.camera_rect.right = target.rect.right
        if target.rect.top < self.camera_rect.top:
            self.camera_rect.top = target.rect.top
        if target.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = target.rect.bottom
        
        self.offset.x = self.camera_rect.left - self.camera_borders['left']
        self.offset.y = self.camera_rect.top - self.camera_borders['top']
        
    def zoom_keyboard(self):
        '''Aqui a gente faz a camera dar zoom usando o teclado. A gente vai usar o teclado para testar a camera, mas a ideia é que a gente use o mouse para dar zoom. Por algum motivo o pygame só deixa usar a roda do mouse lá no main loop... Então não dá pra implementar aqui nesse arquivo. Da uma olhada no arquivo main pra ver o input da camera com zoom'''
            
        keys = pg.key.get_pressed()
        if keys[pg.K_KP_PLUS]:
            self.zoom_scale += 0.1
        if keys[pg.K_KP_MINUS]:
            self.zoom_scale -= 0.1
    
    
    def mouse_control_v2(self, target):
        
        mouse = pg.mouse.get_pos()

        middle = pg.math.Vector2((target.rect.centerx - mouse[0]) / 2, (target.rect.centery - mouse[1]) / 2)

        # debugging stuff
        # print(f'middle {middle} target {target.rect.center} mouse {mouse} half {self.half_width} {self.half_height} calculate {(target.rect.centerx - middle.x) - self.half_width}')

        self.offset.x = (target.rect.centerx - middle.x) - self.half_width
        self.offset.y = (target.rect.centery - middle.y) - self.half_height

    def mouse_control(self):
        '''Esse é o método que vamos usar para a camera movida ao mouse. O funcionamento dela é simpples mas chato de implementar. Basicamente, o offset vai ser definido por onde o mouse está na tela. O nosso retangulo camera vai se mover para acompanhar o mouse, não o player.'''
        mouse = pg.math.Vector2(pg.mouse.get_pos())
        mouse_offset_vector = pg.math.Vector2()
        
        left_border = self.camera_borders['left']
        top_border = self.camera_borders['top']
        right_border = self.display_surface.get_size()[0] - self.camera_borders['right']
        bottom_border = self.display_surface.get_size()[1] - self.camera_borders['bottom']
        
        if top_border < mouse.y < bottom_border:
            if mouse.x < left_border:
                mouse_offset_vector.x = mouse.x - left_border
                pg.mouse.set_pos((left_border, mouse.y))
            if mouse.x > right_border:
                mouse_offset_vector.x = mouse.x - right_border
                pg.mouse.set_pos((right_border, mouse.y))
        elif mouse.y < top_border:
            if mouse.x < left_border:
                mouse_offset_vector = mouse - pg.math.Vector2(left_border, top_border)
                pg.mouse.set_pos((left_border, top_border))
            if mouse.x > right_border:
                mouse_offset_vector = mouse - pg.math.Vector2(right_border, top_border)
                pg.mouse.set_pos((right_border, top_border))
        elif mouse.y > bottom_border:
            if mouse.x < left_border:
                mouse_offset_vector = mouse - pg.math.Vector2(left_border, bottom_border)
                pg.mouse.set_pos((left_border, bottom_border))
            if mouse.x > right_border:
                mouse_offset_vector = mouse - pg.math.Vector2(right_border, bottom_border)
                pg.mouse.set_pos((right_border, bottom_border))
       
        if left_border < mouse.x < right_border:
            if mouse.y < top_border:
                mouse_offset_vector.y = mouse.y - top_border
                pg.mouse.set_pos((mouse.x, top_border))
            if mouse.y > bottom_border:
                mouse_offset_vector.y = mouse.y - bottom_border
                pg.mouse.set_pos((mouse.x, bottom_border))
        self.offset += mouse_offset_vector * self.mouse_speed
        
    def custom_draw(self, player):
        
        # self.center_target_camera(player) #Chama a função que vai centralizar a camera no player
        
        # self.box_target_camera(player) #Chama a função que vai usar a camera de caixa
        
        # self.mouse_control() #Chama a função que vai criar a camera de mouse.
        self.mouse_control_v2(player)
        self.zoom_keyboard()
        
        pg.draw.rect(self.display_surface, (255,0,0), self.camera_rect, 5) #debug camera rect. Cria um retangulo que mostra as dimensoes da camera
        
        self.internal_surface.fill(WATER_COLOR) #Por algum motivo maluco se a gente não fizer isso, a camera fica com umas linhas pretas. Não sei o motivo, mas isso resolve.
        
        for sprite in sorted (self.sprites(), key=lambda sprite: sprite.rect.centery): 
            offset_rect = sprite.rect.topleft - self.offset + self.internal_offset
            self.internal_surface.blit(sprite.image, offset_rect)
        
        scaled_surface = pg.transform.scale(self.internal_surface, self.internal_surface_size_vector * self.zoom_scale)
        scaled_rect = scaled_surface.get_rect(center = (self.half_width, self.half_height))
            
        self.display_surface.blit(scaled_surface, scaled_rect)
        
'''Um pouco sobre cameras:

Bom, basicamente, uma camera é nada mais nada menos que um retangulo invisivel na tela que vai definir o que é mostrado e o que não é mostrado. Por exemplo, se você tem um mapa de 1000x1000 pixels, e a camera é de 500x500 pixels, então só será mostrado 500x500 pixels do mapa. Se a camera estiver no canto superior esquerdo do mapa, então só será mostrado o canto superior esquerdo do mapa. Se a camera estiver no canto inferior direito do mapa, então só será mostrado o canto inferior direito do mapa. Se a camera estiver no meio do mapa, então só será mostrado o meio do mapa. E assim por diante. 

Entretanto, a camera aqui no Pygame não é um retangulo invisivel, mas sim um retangulo que é mostrado na tela. Isso é feito para facilitar o debug, mas também pode ser usado para fazer um efeito de camera de box, que é o que eu fiz aqui.

As cameras precisam de dois parametros para funcionar: o tamanho da camera e o offset da camera. O tamanho da camera é o tamanho do retangulo que vai ser mostrado na tela. O offset da camera é a posição do retangulo na tela. Normalmente, o tamanho da camera é defindo como valores fixos, e o offset da camera é definido de acordo com a posição do jogador ou de outra coisa. A posição de uma camera é definida em nosso código no canto superior esquerdo (topleft) da tela, no qual as coordenadas são (0,0). Poém, adicionamos um offset que é baseado na posição do player, fazendo a camera centralizar nele e caminhar junto com ele. Se o player chega na borda da camera, o offset sofre um update e acompanha o player.

Temos também o Ysort, que é basicamente um meio de organizar os sprites na tela. O Ysort é usado para organizar os sprites na tela de acordo com a posição deles no eixo Y. Isso é feito para que os sprites mais próximos do jogador sejam mostrados na frente dos sprites mais distantes do jogador. Isso é feito usando a função sorted, que ordena os sprites de acordo com a posição deles no eixo Y. O sprite mais próximo do jogador vai ser o primeiro da lista, e o sprite mais distante do jogador vai ser o último da lista. Então, ao desenhar os sprites na tela, eles são desenhados na ordem da lista, ou seja, do sprite mais próximo do jogador até o sprite mais distante do jogador. Isso faz com que os sprites mais próximos do jogador sejam mostrados na frente dos sprites mais distantes do jogador'''