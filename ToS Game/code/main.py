import pygame as pg
import sys
from settings import WIDTH, HEIGHT, FPS, WATER_COLOR, CONTROLKEYS
from level import Level 
import pygame_menu as pg_menu

class Game:   
    
    def __init__(self):
        
        # general setup
        pg.init()
        
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        
        pg.display.set_caption('Tales of sophia')
        
        self.clock = pg.time.Clock()
        
        pg.event.set_grab(True)
        
        self.level = Level()  # instancia o level
        
    def run(self):
        
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                
                if event.type == pg.KEYDOWN and event.key == CONTROLKEYS['exit']:
                        pg.quit()
                        sys.exit()
                game.level.visible_sprites.zoom_scroll(event) ## cara, essa parte do codigo busca a instasncia da camera e executa a funcao de zoom no scroll do mouse
            
            self.screen.fill(WATER_COLOR)
            
            self.level.run()
            
            pg.display.update()
            
            self.clock.tick(FPS)
            
            keys = pg.key.get_pressed()
            if keys[pg.K_o]:
                print(self.level.player.rect.x, self.level.player.rect.y) #printa a posição do player
                print() #debug flag do vscode


if __name__ == '__main__':
    game = Game()
    
#Menu:
class Menu():

    surface = pg.display.set_mode((WIDTH, HEIGHT))

    def start_game():
        game.run()
    
    menugame = pg_menu.Menu('Tales of Sophia', WIDTH, HEIGHT, theme=pg_menu.themes.THEME_DARK)
    
    menugame.add.button('Start Game', start_game)
    
    menugame.add.button('Quit', pg_menu.events.EXIT)
    
    menugame.mainloop(surface)
#