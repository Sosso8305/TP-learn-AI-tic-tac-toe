from morpion import Game
from morpion import logger as log

if __name__ == "__main__":
    game = Game()
    log.info("Game running")
    game.run()
    