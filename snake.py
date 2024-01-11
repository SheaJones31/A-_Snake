import pygame
import settings


class Snake:
    def __init__(self):
        self.length = 1
        self.position_x = settings.WIDTH // 2 + 10
        self.position_y = settings.HEIGHT // 2 - 10
        self.positions = [(self.position_x, self.position_y)]  # Start in the middle of the screen
        self.direction = None
        self.color = settings.WHITE
        self.score = 0

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        if self.direction is None:
            return

        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * settings.SNAKE_BLOCK)) % settings.WIDTH), (cur[1] + (y * settings.SNAKE_BLOCK)) % settings.HEIGHT)
        self.positions.insert(0, new)
        if len(self.positions) > self.length:
            self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((settings.WIDTH / 2), (settings.HEIGHT / 2))]
        self.direction = None
        self.score = 0

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (settings.SNAKE_BLOCK, settings.SNAKE_BLOCK))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93, 216, 228), r, 1)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.turn((0, -1))
            elif event.key == pygame.K_DOWN:
                self.turn((0, 1))
            elif event.key == pygame.K_LEFT:
                self.turn((-1, 0))
            elif event.key == pygame.K_RIGHT:
                self.turn((1, 0))

    def grow(self):
        self.length += 1
        self.score += 1

    def check_collision(self, position):
        return self.get_head_position() == position

    def check_fail(self):
        head = self.get_head_position()
        return head in self.positions[1:]
