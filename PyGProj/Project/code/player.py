import pygame as pg
from settings import HITBOX_OFFSET, CONTROLKEYS


class Player(pg.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        
        self.image = pg.image.load('../graphs/test/player.png')
        
        self.rect = self.image.get_rect(topleft=pos)
        
        self.hitbox = self.rect.inflate(HITBOX_OFFSET['playerY'], HITBOX_OFFSET['playerX'])
         
        self.direction = pg.math.Vector2() 
        
        self.speed = 20 # velocidade do player
        
        self.obstacle_sprites = obstacle_sprites
        
    def input(self):
        
        keys = pg.key.get_pressed()
        
        if keys[CONTROLKEYS['up']]:
            self.direction.y = -1
            self.image = pg.image.load('../graphs/player/up/up_0.png')
            
        elif keys[CONTROLKEYS['down']]:
            self.direction.y = 1
            self.image = pg.image.load('../graphs/player/down/down_0.png')
            
        else:
            self.direction.y = 0
            
        if keys[CONTROLKEYS['right']]:
            self.direction.x = 1
            self.image = pg.image.load('../graphs/player/right/right_0.png')
            
        elif keys[CONTROLKEYS['left']]:
            self.direction.x = -1
            self.image = pg.image.load('../graphs/player/left/left_0.png')
            
        else:
            self.direction.x = 0
    
    
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
        
        self.move(self.speed)
        
        self.playertp()