import pygame
from utilities import message
import settings


def show_retry_screen(game_display, score):
    running = True
    retry_selected = 0  # 0 for Yes, 1 for No

    while running:
        game_display.fill((0, 0, 0))  # Clear screen (or set to your game's background)

        # Display the main retry message
        message(f"Retry? You scored {score}", settings.WHITE, game_display)

        # Display 'Yes' and 'No' options
        yes_no_color = [settings.RED if retry_selected == 0 else settings.WHITE,
                        settings.RED if retry_selected == 1 else settings.WHITE]
        message("Yes", yes_no_color[0], game_display, y_offset=30)
        message("No", yes_no_color[1], game_display, y_offset=60)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    retry_selected = 1 - retry_selected
                elif event.key == pygame.K_RETURN:
                    return retry_selected == 0  # Return True if 'Yes' is selected
            elif event.type == pygame.QUIT:
                return False

    return False
