from cgi import print_directory
import pygame as pg
from settings import HITBOX_OFFSET, CONTROLKEYS
from support import import_folder
class Player(pg.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        #hitbox
        self.image = pg.image.load('../graphs/playerdefault/0.png')
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(HITBOX_OFFSET['playerY'], HITBOX_OFFSET['playerX'])
        
        #atributos do player
        self.speed = 10 
        self.attackspeed = 1
        
        #logica
        self.direction = pg.math.Vector2()
        self.attacktime= 0
        self.magictime = 0
        self. interacttime = 0
        self.attacking = False #na real isso e usado ate pras interações, mas o nome vai ficar ataque ate eu pensar em algo melhor
        
        #setup dos graficos
        self.obstacle_sprites = obstacle_sprites
        self.import_player_assets()
        self.status = 'down'
        self.frame_index =0
        self.animation_speed = 0.15
        
        
        
    def import_player_assets(self):
        assets_path = '../graphs/player/'
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [], 'left_idle': [], 'right_idle': [
        ], 'up_idle': [], 'down_idle': [], 'left_attack': [], 'right_attack': [], 'up_attack': [], 'down_attack': []}
        for animation in self.animations.keys():
            full_path = assets_path + animation
            self.animations[animation] = import_folder(full_path)
            
        
    def input(self):
        
        keys = pg.key.get_pressed()
        
        if keys[CONTROLKEYS['up']]:
            self.direction.y = -1
            self.status = 'up'
            
        elif keys[CONTROLKEYS['down']]:
            self.direction.y = 1
            self.status = 'down'
            
        else:
            self.direction.y = 0
            
        if keys[CONTROLKEYS['right']]:
            self.direction.x = 1
            self.status = 'right'
            
        elif keys[CONTROLKEYS['left']]:
            self.direction.x = -1
            self.status = 'left'
            
        else:
            self.direction.x = 0
        
        #tempo pra animação de ataque
                
        if int(pg.time.get_ticks()) - self.attacktime >= (80/self.attackspeed): #muita logica envolvida pra levar em conta o attk speed, que deve ser um atributo do jogo final, mas vai valer a pena
            self.attacking = False
        
        if keys[CONTROLKEYS['attack']]:
            if int(pg.time.get_ticks()) - self.attacktime >= (1000/self.attackspeed):
                self.attacking = True
                self.attacktime = pg.time.get_ticks()
                print('receba')
                
        if keys[CONTROLKEYS['magic']]:
            #imagino q vamos usar mais de um spell entao tem q chegar na conclusao de como q vai funcionar para calcular o cd
            if int(pg.time.get_ticks()) - self.magictime >= (100): #adicionar o cooldown do spell aqui, isso provavelmente vai virar uma funcao separada no futuro e receber o id do spell e o cd dele :brain:
                self.attacking = True
                self.magictime = pg.time.get_ticks()
                print('olha a magica')
        
        if keys[CONTROLKEYS['interact']]:
            if int(pg.time.get_ticks()) - self.interacttime >= (100):
                self.attacking = True
                self.interacttime = pg.time.get_ticks()
                print('momento interacao')
        
        if keys[CONTROLKEYS['inventory']]:
            print('inventario')
    
    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.rect.center)
    
    
    def get_status(self):
        #idle
        if self.direction.x == 0 and self.direction.y == 0 and 'idle' not in self.status and 'attack' not in self.status:
            self.status = self.status + '_idle'
        #attack
        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if 'attack' not in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle', '_attack')
                else:
                    self.status = self.status + '_attack'
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack', '')
    
    
    def move(self,speed): 
        
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            
        self.hitbox.x += self.direction.x * speed
        
        self.collision('horizontal')
        
        self.hitbox.y += self.direction.y * speed
        
        self.collision('vertical')
        
        self.rect.center = self.hitbox.center
        
    def collision(self,direction):
        
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: 
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: 
                        self.hitbox.left = sprite.hitbox.right
                        
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: 
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: 
                        self.hitbox.top = sprite.hitbox.bottom        
        
    def playertp(self):
        
        keys = pg.key.get_pressed()
        
        if keys[pg.K_F2]: #Não vamos definir no settings porque é só debug
            print('tp')
            X = int(input('X:'))
            Y = int(input('Y:'))
            self.hitbox.x = X
            self.hitbox.y = Y
            
            
    def update(self):
        self.input()
        self.get_status()
        self.animate()
        self.move(self.speed)
        #self.playertp()