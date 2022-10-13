import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pg.image.load('../graphs/test/player.png')
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pg.math.Vector2() # direção do player é um vetor 2D, ou seja, se move em X e Y. Mais tarde vamos multiplicar isso pela velocidade do player.
        
        self.speed = 5 # velocidade do player
        
        self.obstacle_sprites = obstacle_sprites
        
    def input(self):
        '''Definimos o input do player aqui. Tudo o que pode ser apertado e o que acontecerá quando for apertado. '''
        
        keys = pg.key.get_pressed()
        
        if keys [pg.K_w]:
            self.direction.y = -1
        elif keys [pg.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
            
        if keys [pg.K_d]:
            self.direction.x = 1
        elif keys [pg.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0
    
    
    def move(self, speed):
        '''Este método vai ser chamado quando o player se mover. Ele vai mover o player de acordo com a direção que ele está indo, e a velocidade que ele está indo. Também são chamados os métodos de colisão aqui. '''
        
        if self.direction.magnitude() != 0:  #Normalizando vetores para que o player não se mova mais rápido quando se move em diagonal.
            self.direction = self.direction.normalize()
        
        self.rect.x += self.direction.x * speed
        self.collision('horizontal')
        self.rect.y += self.direction.y * speed
        self.collision('vertical')
    
    def collision(self, direction):
        '''Este método vai ser chamado quando o player colidir com um obstáculo. Basicamente ele vai verificar se o player está colidindo com um obstáculo, e se estiver, ele vai fazer o player voltar para a posição anterior. O pygame não consegue checkar a direção da colisão com obstáculos, então vamos fazer isso manualmente. Resumidamente, se o jogador estiver se movendo para a direita, é impossível que ele tenha uma colisão com um obstáculo à esquerda, então não vamos checar isso. '''
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right
        
                        
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom
    
    def update(self):
        self.input()
        self.move(self.speed)