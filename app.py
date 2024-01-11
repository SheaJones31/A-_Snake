import time
import pygame
import settings
from game_state import GameState


def game_loop():
    pygame.init()
    game_state = GameState()

    game_state.initial_pause()

    while not game_state.game_over:
        game_state.handle_events()
        game_state.update()
        game_state.draw()
        pygame.display.update()
        #time.sleep(settings.SNAKE_SPEED)


if __name__ == "__main__":
    game_loop()
