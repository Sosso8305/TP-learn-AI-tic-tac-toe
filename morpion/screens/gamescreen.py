import pygame
from . import Window
from ..logger import logger as log
from ..tools import Button
from ..constants import WHITE
from ..board import Board


class GameScreen(Window):
    def __init__(self, game):
        super().__init__(game)

        #self.board = Board(self.game.params[player1], self.game.params[player2])
        
        
        
        


        
        self.currentscreen = 'game_screen'

    
    def update(self, events):
        
        pass
       
       
    

