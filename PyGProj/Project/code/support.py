from csv import reader
from os import walk
import pygame as pg

def import_csv(path):
    terrain_map=[]
    with open(path) as level_map:
        layout = reader(level_map,delimiter=",")
        for row in layout:
            terrain_map.append(list(row))
    return terrain_map

pg.init()
def import_folder(path): #importador de arquivos de sprite pogg
    surface_list= []
    for _,__,img_files in walk(path):
        for image in img_files:
            fullpath = path +'/'+ image
            image_surf = pg.image.load(fullpath).convert_alpha()
            surface_list.append(image_surf)
    return surface_list

