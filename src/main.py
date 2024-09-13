from classes import *

if __name__ == "__main__":
    gameInteraction.title_screen()
    Game.start()
    while True:
        gameInteraction.request_action()