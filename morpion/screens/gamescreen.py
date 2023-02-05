import pygame
from . import Window
from ..logger import logger as log
from ..tools import Button
from ..constants import WHITE
from ..board import Board


class GameScreen(Window):
    def __init__(self, game):
        super().__init__(game)

        self.nameBase = "Morpion"+ " - " + self.game.params['player1_name'] + " VS " + self.game.params['player2_name'] + " - " 
        self.board = Board(self.game.params['player1'], self.game.params['player2'])
        self.mark= [self.game.params['player1'], self.game.params['player2']]
        self.namePlayer = [self.game.params['player1_name'], self.game.params['player2_name']]

       
        self.cell00 = Button(self.game,(5,5),"",(195,195),textScale=1.8,imgPath = "morpion/assets/UI/button_gray.png",action=self.play, params=(0,0))
        self.cell01 = Button(self.game,(205,5),"",(195,195),textScale=1.8,imgPath = "morpion/assets/UI/button_gray.png",action=self.play, params=(0,1))
        self.cell02 = Button(self.game,(405,5),"",(195,195),textScale=1.8,imgPath = "morpion/assets/UI/button_gray.png",action=self.play, params=(0,2))
        self.cell10 = Button(self.game,(5,205),"",(195,195),textScale=1.8,imgPath = "morpion/assets/UI/button_gray.png",action=self.play, params=(1,0))
        self.cell11 = Button(self.game,(205,205),"",(195,195),textScale=1.8,imgPath = "morpion/assets/UI/button_gray.png",action=self.play, params=(1,1))
        self.cell12 = Button(self.game,(405,205),"",(195,195),textScale=1.8,imgPath = "morpion/assets/UI/button_gray.png",action=self.play, params=(1,2))
        self.cell20 = Button(self.game,(5,405),"",(195,195),textScale=1.8,imgPath = "morpion/assets/UI/button_gray.png",action=self.play, params=(2,0))
        self.cell21 = Button(self.game,(205,405),"",(195,195),textScale=1.8,imgPath = "morpion/assets/UI/button_gray.png",action=self.play, params=(2,1))
        self.cell22 = Button(self.game,(405,405),"",(195,195),textScale=1.8,imgPath = "morpion/assets/UI/button_gray.png",action=self.play, params=(2,2))

        self.cells = [self.cell00, self.cell01, self.cell02, self.cell10, self.cell11, self.cell12, self.cell20, self.cell21, self.cell22]

        

        self.currentscreen = 'game_screen'

    



    def update_display(self, events):
        for cell in self.cells:
            x,y = cell.params

            text = self.board.getMark(x, y)
            if text != 0:
                cell.setText(text)

            self.blit(cell.image, cell.rect)
            cell.update(events)


    def update(self, events):
    
        if not self.board.finished:
            self.current_mark = self.mark[self.board.getTurnPlayer()-1]
            self.name = self.nameBase + self.namePlayer[self.board.getTurnPlayer()-1] + " turn"
            pygame.display.set_caption(self.name)

            self.update_display(events)
            self.board.isWinner()


        if self.board.finished:
            self.update_display(events)
            self.name = self.nameBase +  " Game finished"
            pygame.display.set_caption(self.name)

            self.game.params['winner'] = self.board.getWinner()
           
            # add end screen
            


           
   
        


    def play(self, pos):
        x, y = pos
        #log.debug(f"Button {x} {y}")
        if not self.board.finished:
            self.board.setMark(self.current_mark, x, y)

        
