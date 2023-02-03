import pygame
from .logger import logger as log 
from .screens import MenuScreen, GameScreen
from .tools import TextDisplayer

class Game:
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Morpion")
        self.DISPLAY_SIZE = (600, 600)
        self.display = pygame.display.set_mode(self.DISPLAY_SIZE)
        self.clock = pygame.time.Clock()
        self.running = False
        self.textDisplayer = TextDisplayer(self)

        self.current_screen = "main_screen"

        self.screens = {
            "main_screen": MenuScreen(self),
            "game_screen": GameScreen(self)
        }

        self.params = {
            "player1": "X",
            "player2": "O",
            "player1_name": "Player 1",
            "player2_name": "Player 2",
            "typePlayer1": "human",
            "typePlayer2": "human",
            "AI_method": "easy" # easy, mimax, minimax_alpha_beta, complex
        }


        
    def setScreen(self, screen_name):
        if screen_name in self.screens:
            self.current_screen = screen_name
        else:
            log.error(f"Screen {screen_name} doesn't exist")
        
    
    def run(self):
        self.running = True
        log.debug("funct Game.run() called")
        

        while self.running:
            events = pygame.event.get()

            self.screens[self.current_screen].update(events)
            self.display.blit(self.screens[self.current_screen], (0,0))
            pygame.display.update()

            for event in events:
                if event.type == pygame.QUIT:
                    log.info("Game closed")
                    self.running = False
                    pygame.quit()
