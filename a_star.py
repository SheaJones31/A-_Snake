import settings
from pathfinder import GridCell, a_star
import pygame


class AStarUse:
    def __init__(self, snake, food):
        self.snake = snake
        self.food = food
        self.grid = self.create_grid()
        self.path = []

    def update_a_star(self):
        # Update the grid representation of the game after moving the snake
        self.grid = self.create_grid()

        # Use A* to find a path from the snake's updated head to the food
        start = GridCell(int(self.snake.get_head_position()[0] // settings.SNAKE_BLOCK),
                         int(self.snake.get_head_position()[1] // settings.SNAKE_BLOCK), GridCell.SNAKE)
        goal = GridCell(int(self.food.position[0] // settings.SNAKE_BLOCK),
                        int(self.food.position[1] // settings.SNAKE_BLOCK), GridCell.FOOD)

        self.path = a_star(start, goal, self.grid)
        self.ai_move()
        if 1 == abs(start.x - goal.x) + abs(start.y - goal.y):
            if (goal.x, goal.y) not in self.snake.positions:
                self.snake.turn((goal.x - start.x, goal.y - start.y))

    def ai_move(self):
        # Move the snake based on the path
        if self.path:
            current_direction = self.snake.direction
            next_direction = self.get_direction_from_path()
            if next_direction and current_direction != next_direction:
                self.snake.move()
                self.snake.turn(next_direction)

    def create_grid(self):
        # Assuming settings.SNAKE_BLOCK is the size of each grid cell
        grid_width = settings.WIDTH // settings.SNAKE_BLOCK
        grid_height = settings.HEIGHT // settings.SNAKE_BLOCK

        # Initialize the grid
        grid = [[GridCell(x, y) for x in range(grid_width)] for y in range(grid_height)]

        # Convert the snake's positions to grid coordinates and update the grid
        for pos in self.snake.positions:
            grid_x = int(pos[0] // settings.SNAKE_BLOCK)
            grid_y = int(pos[1] // settings.SNAKE_BLOCK)
            if 0 <= grid_x < grid_width and 0 <= grid_y < grid_height:
                grid[grid_y][grid_x].cell_type = GridCell.SNAKE

        # Update the food's position in the grid
        food_x = int(self.food.position_x // settings.SNAKE_BLOCK)
        food_y = int(self.food.position_y // settings.SNAKE_BLOCK)
        if 0 <= food_x < grid_width and 0 <= food_y < grid_height:
            grid[food_y][food_x].cell_type = GridCell.FOOD

        return grid

    def get_direction_from_path(self):
        if not self.path or len(self.path) < 2:
            return None  # No direction if the path is too short

        head_x, head_y = self.snake.get_head_position()
        next_step = self.path[1]  # path[0] is the current head position, path[1] is the next step
        next_x, next_y = next_step.x * settings.SNAKE_BLOCK, next_step.y * settings.SNAKE_BLOCK

        # Determine direction based on the position of the next step relative to the head
        if next_x > head_x:
            return 1, 0  # Right
        elif next_x < head_x:
            return -1, 0  # Left
        elif next_y > head_y:
            return 0, 1  # Down
        else:
            return 0, -1  # Up

    def draw(self, game_display):
        for cell in self.path[:-1]:
            x, y = cell.x * settings.SNAKE_BLOCK, cell.y * settings.SNAKE_BLOCK
            rect = pygame.Rect(x, y, settings.SNAKE_BLOCK, settings.SNAKE_BLOCK)
            pygame.draw.rect(game_display, settings.PATH_COLOR, rect)
