import pygame
from . import Window
from ..logger import logger as log
from ..tools import Button


class MenuScreen(Window):
    def __init__(self, game):
        super().__init__(game)

        self.rect = self.game.display.get_rect()
        self.background = pygame.image.load("morpion/assets/menu/background.png")
        self.background = pygame.transform.scale(self.background, self.rect.size)

        self.game.textDisplayer.write("Morpion", (self.rect.centerx, self.rect.centery - 150),screen=self.background,center=True)

        self.GameAIButton = Button(self.game, (self.rect.centerx - 100, self.rect.centery - 70), "VS AI", (200, 60),textScale=0.3, action=self.gameAI)
        self.Game2PButton = Button(self.game, (self.rect.centerx - 100, self.rect.centery +30), "2 Player", (200, 60), textScale=0.3, action=self.game2P)
        self.QuitButton = Button(self.game, (self.rect.centerx - 100, self.rect.centery + 150), "Quit", (200, 50), action=self.quit, imgPath = "morpion/assets/UI/button_red.png")

        self.currentscreen = 'menu_screen'

    
    def update(self, events):
        self.blit(self.background, (0, 0))
        self.blit(self.GameAIButton.image, self.GameAIButton.rect)
        self.blit(self.Game2PButton.image, self.Game2PButton.rect)
        self.blit(self.QuitButton.image, self.QuitButton.rect)

        self.GameAIButton.update(events)
        self.Game2PButton.update(events)
        self.QuitButton.update(events)

    
    def gameAI(self):
        log.info("Game vs AI")
        self.game.setScreen('game_screen')

    def game2P(self):
        log.info("Game vs Player")
        self.game.setScreen('game_screen')

    def quit(self):
        log.info("Button Quit")
        self.game.running = False        

