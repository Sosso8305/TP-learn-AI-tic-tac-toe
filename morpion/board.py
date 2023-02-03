from logger import logger as log
from random import randint

class Board:
    
    def __init__(self,player1,player2):
        self.player1 = player1 # "X" or "O"
        self.player2 = player2
        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        #self.board = [['X','X','O'],['O','O','X'],['X',0,0]]
        self.turn = 1
        self.winner = 0 # 0 = no winner, 1 = player1, 2 = player2
        self.finished = False
        self.turnPlayer = randint(1,2)


    def isWinner(self):
        winnerMark = 0

        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != 0:
                winnerMark  = self.board[i][0]
                self.finished = True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != 0:
                winnerMark  = self.board[0][i]
                self.finished = True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != 0:
            winnerMark  = self.board[0][0]
            self.finished = True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != 0:
            winnerMark  = self.board[0][2]
            self.finished = True

        if self.turn == 9 and not self.finished:
            self.finished = True
            self.winner = 0
            return True


        if self.finished:
            if winnerMark == "X" and self.player1 == "X":
                self.winner = 1
            elif winnerMark == "O" and self.player1 == "O":
                self.winner = 1
            else:
                self.winner = 2   

            return True
        
        return False


    def setMark(self, mark, x, y):
        if self.turnPlayer == 1:
            if mark != self.player1:
                log.error("Player 1 tried to play with the wrong mark")
                return False
        elif self.turnPlayer == 2:
            if mark != self.player2:
                log.error("Player 2 tried to play with the wrong mark")
                return False


        if self.board[x][y] == 0:
            self.board[x][y] = mark
            self.turn += 1
            if self.turnPlayer == 1:
                self.turnPlayer = 2
            else:
                self.turnPlayer = 1
            return True
        else:
            log.error("Player tried to play on a non empty case")
            return False

    def getTurnPlayer(self):
        return self.turnPlayer

    def display(self):
        for i in range(3):
            print(self.board[i])

    def getWinner(self):
        return self.winner

    def getMark(self,x,y):
        if x < 0 or x > 2 or y < 0 or y > 2:
            log.error("Player tried to get a mark out of the board")
        return self.board[x][y]
    