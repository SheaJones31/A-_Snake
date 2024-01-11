import pygame
import random
import settings


class Food:
    def __init__(self, snake):
        self.position_x = 0
        self.position_y = 0
        self.position = (self.position_x, self.position_y)
        self.color = settings.RED
        self.randomize_position(snake.positions)

    def randomize_position(self, snake_positions):
        while True:
            self.position_x = random.randint(0, (
                        settings.WIDTH - settings.SNAKE_BLOCK) // settings.SNAKE_BLOCK) * settings.SNAKE_BLOCK
            self.position_y = random.randint(0, (
                        settings.HEIGHT - settings.SNAKE_BLOCK) // settings.SNAKE_BLOCK) * settings.SNAKE_BLOCK
            self.position = (self.position_x, self.position_y)
            if self.position not in snake_positions:
                break

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (settings.SNAKE_BLOCK, settings.SNAKE_BLOCK))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (255, 255, 255), r, 1)
