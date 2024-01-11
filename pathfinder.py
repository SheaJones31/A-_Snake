import heapq


class GridCell:
    EMPTY = 0
    FOOD = 1
    SNAKE = 2

    def __init__(self, x, y, cell_type=0):
        self.x = x
        self.y = y
        self.cell_type = cell_type

    def __eq__(self, other):
        if not isinstance(other, GridCell):
            input("Failure")
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def is_empty(self):
        return self.cell_type == GridCell.EMPTY

    def __lt__(self, other):
        # Define a comparison based on whatever makes sense for your grid cells.
        # For example, you might compare based on a heuristic value, or simply the coordinates.
        return (self.x, self.y) < (other.x, other.y)


def manhattan_distance(start, end):
    return abs(start.x - end.x) + abs(start.y - end.y)


def get_neighbors(node, grid):
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Up, Down, Left, Right
    neighbors = []
    for dx, dy in directions:
        x, y = int(node.x + dx), int(node.y + dy)  # Convert to integers
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            if grid[y][x].is_empty() or grid[y][x].cell_type == GridCell.FOOD:
                neighbors.append(grid[y][x])
    return neighbors


def a_star(start, goal, grid):
    count = 0
    open_set = []
    heapq.heappush(open_set, (0, count, start))

    came_from = {}
    g_score = {node: float('inf') for row in grid for node in row}
    g_score[start] = 0

    f_score = {node: float('inf') for row in grid for node in row}
    f_score[start] = manhattan_distance(start, goal)

    while open_set:
        current = heapq.heappop(open_set)[2]

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for neighbor in get_neighbors(current, grid):
            tentative_g_score = g_score[current] + 1
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + manhattan_distance(neighbor, goal)
                if neighbor not in [item[2] for item in open_set]:
                    count += 1
                    heapq.heappush(open_set, (f_score[neighbor], count, neighbor))

    return []  # Return an empty path if no path is found
