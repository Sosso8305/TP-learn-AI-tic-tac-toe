import pygame
from . import Window
from ..logger import logger as log
from ..tools import Button


class GameScreen(Window):
    def __init__(self, game):
        super().__init__(game)

        self.rect = self.game.display.get_rect()
        self.background = pygame.image.load("morpion/assets/menu/background.png")
        self.background = pygame.transform.scale(self.background, self.rect.size)


        
        self.currentscreen = 'game_screen'

    
    def update(self, events):
        self.blit(self.background, (0, 0))
       
       
    

