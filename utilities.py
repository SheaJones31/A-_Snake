import pygame
import settings


def message(msg, color, game_display, y_offset=0):
    font_style = pygame.font.SysFont(None, 30)
    mesg = font_style.render(msg, True, color)

    # Get the size of the rendered message
    mesg_size = mesg.get_size()

    # Calculate the x and y position to center the text
    x = (settings.WIDTH - mesg_size[0]) / 2
    y = (settings.HEIGHT - mesg_size[1]) / 2 + y_offset

    # Blit the message on the screen at the calculated position
    game_display.blit(mesg, (x, y))
