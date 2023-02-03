import pygame

## Mother for screens

class Window(pygame.Surface):

	def __init__(self, game, size=None, flags=0):
		super().__init__(size or game.DISPLAY_SIZE, flags=flags)
		self.game = game

	def update(self, events):
		pass
