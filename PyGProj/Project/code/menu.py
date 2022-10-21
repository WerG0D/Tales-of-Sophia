import pygame as pg
import pygame_menu as pg_menu
from settings import HEIGHT, WIDTH


class Menu:

    pg.init()
    surface = pg.display.set_mode((WIDTH, HEIGHT))

    def load_game():
        # Do the job here !
        pass

    def start_game():
            game.level.run()
        pass

    def options():
        pass

    def about():
        pass

    menu = pg_menu.Menu('Tales of Sophia', 1280, 720, theme=pg_menu.themes.THEME_DARK)
    menu.add.button('Start Game', start_game)
    menu.add.button('Load Game', load_game)
    menu.add.button('Options', options)
    menu.add.button('About', about)
    menu.add.button('Quit', pg_menu.events.EXIT)

    menu.mainloop(surface)
