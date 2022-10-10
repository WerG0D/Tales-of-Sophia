import pygame, sys
from settings import *
from level import Level
#import level
class Game:
	def __init__(self):

		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Zelda')
		self.clock = pygame.time.Clock()

		self.level = Level() #instancia o level

		# sound 
		main_sound = pygame.mixer.Sound('./audio/main.ogg')
		main_sound.set_volume(0.5)
		main_sound.play(loops = -1)
	
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_m:
						pass #Aqui vai ser adicionado uma tecla pra navegar no menu ou começar o game
						#self.level.toggle_menu()

			self.screen.fill(WATER_COLOR)
			self.level.run() #Aqui vai ser adicionado o level, menu, sla
			pygame.display.update()
			self.clock.tick(FPS)

if __name__ == '__main__':
	game = Game()
	game.run()