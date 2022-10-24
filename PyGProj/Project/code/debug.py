
import pygame as pg
pg.init()
font = pg.font.Font(None,30)

def debug(info,y = 10, x = 10):
	display_surface = pg.display.get_surface()
	debug_surf = font.render(str(info),True,'White')
	debug_rect = debug_surf.get_rect(topleft = (x,y))
	pg.draw.rect(display_surface,'Black',debug_rect)
	display_surface.blit(debug_surf,debug_rect)



def keydebug(tag, info):    #olha q legal adicionei essa funcao que pode ser usada pra debugar uma informacao usando a tecla f1 :P
    #tag e so um nome pra variavel q ta sendo debugada
    keys = pg.key.get_pressed()
    if keys[pg.K_F1]:
        print(tag,info)
