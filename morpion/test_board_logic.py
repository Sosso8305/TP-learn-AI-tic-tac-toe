from board import Board

board = Board("X","O")

mark = ["X","O"]

print("Welcome to Tic Tac Toe !")
print("Player 1 is ", board.player1)
print("Player 2 is ", board.player2)
print("Let's start !\n")

while not board.finished:
    current_mark = mark[board.getTurnPlayer()-1]
    print("\n Player", board.getTurnPlayer(), "turn (",board.turn,")")
    board.display()
    x = int(input("x: "))
    y = int(input("y: "))
    board.setMark(current_mark,x,y)
    board.isWinner()

board.display()
print("Winner is player", board.getWinner())


