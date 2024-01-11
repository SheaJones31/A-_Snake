import pygame
from snake import Snake
from food import Food
from a_star import AStarUse
import utilities
import settings
import post_game


class GameState:
    def __init__(self):
        self.game_over = False
        self.snake = Snake()
        self.food = Food(self.snake)
        self.a_star = AStarUse(self.snake, self.food)
        self.game_display = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        pygame.display.set_caption('Snake Game')
        self.clock = pygame.time.Clock()
        self.clock.tick(settings.TICK_RATE)

    def initial_pause(self):
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    paused = False

            self.game_display.fill(settings.BLACK)
            utilities.message("Press any key to start, press 'q' to quit", settings.WHITE, self.game_display)
            pygame.display.update()
            self.clock.tick(settings.PAUSE_TICK)  # Lower FPS since it's just a pause screen
        self.clock.tick(settings.TICK_RATE)  # After breaking loop, FPS restored

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                else:
                    self.snake.handle_event(event)

    def update(self):
        # Move the snake first
        self.snake.move()

        # Check for collisions and grow snake if it eats food
        if self.snake.check_collision(self.food.position):
            self.food.randomize_position(self.snake.positions)
            self.snake.grow()

        # Check if the snake has collided with itself
        if self.snake.check_fail():
            print("GAME OVER")
            #self.game_over = True
            if self.game_over and post_game.show_retry_screen(self.game_display, self.snake.score):
                self.game_over = False
                self.snake.reset()
                return
            else:
                self.snake.reset()
                return
        self.a_star.update_a_star()

    def grid_lines(self):
        for i in range(settings.WIDTH // settings.SNAKE_BLOCK):  # Loop for the number of cells horizontally
            # Draw vertical lines
            pygame.draw.line(self.game_display, settings.WHITE, (i * settings.SNAKE_BLOCK, 0), (i * settings.SNAKE_BLOCK, settings.HEIGHT))
        for j in range(settings.HEIGHT // settings.SNAKE_BLOCK):  # Loop for the number of cells vertically
            # Draw horizontal lines
            pygame.draw.line(self.game_display, settings.WHITE, (0, j * settings.SNAKE_BLOCK), (settings.WIDTH, j * settings.SNAKE_BLOCK))

    def draw(self):
        self.game_display.fill(settings.BLACK)
        self.a_star.draw(self.game_display)
        self.grid_lines()
        self.snake.draw(self.game_display)
        self.food.draw(self.game_display)
        pygame.display.set_caption(f'Snake Game - Score: {self.snake.score}')

