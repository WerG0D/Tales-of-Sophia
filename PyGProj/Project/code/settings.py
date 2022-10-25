import pygame as pg
# game setup
WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 64
HITBOX_OFFSET = {
    'playerX': -30,
    'playerY': -10,
    'object': -40,
    'grass': -10,
    'invisible': 0}

# ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = '../graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# upgrade menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'


# world map

WORLD_MAP = [
    ['x', 'x', 'x', 'x', ' ', 'x', 'x', 'x', 'x', 'x',
        'x', 'x', 'x', ' ', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', 'p', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x',
        'x', 'x', 'x', 'x', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', 'x', 'x', 'x', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', 'x',
        ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', 'x', 'x', 'x', 'x',
        'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', 'x',
        ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ',
        ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
        ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', 'x', 'x', 'x', ' ', 'x', 'x', 'x', 'x', 'x',
        'x', 'x', 'x', ' ', 'x', 'x', 'x', 'x', 'x', 'x'],
]

#controls
CONTROLKEYS = {
    'exit': pg.K_ESCAPE,
    'enter': pg.K_RETURN,
    ## move
    'up': pg.K_w,
    'down': pg.K_s,
    'left': pg.K_a,
    'right': pg.K_d,
    ##cam
    'camera_up': pg.K_UP,
    'camera_down': pg.K_DOWN,
    'camera_left': pg.K_LEFT,
    'camera_right': pg.K_RIGHT,
    'camera_zoom_in': pg.K_KP_PLUS,
    'camera_zoom_out': pg.K_MINUS,
    'camera_zoom_reset': pg.K_0,
    'camera_unlock': pg.K_u,
    'camera_lock': pg.K_l,
    'camera_speed_up': pg.K_i,
    'camera_speed_down': pg.K_k,
}