"""Game grid method object"""
import random
from cell import Cell

class Grid():
    """Game grid method object"""
    def __init__(self, snake, apples, configurations):
        self.snake = snake
        self.apples = apples
        self.config = configurations

    def check_snake_state(self):
        """Check state of snake"""
        head = self.snake.head
        if self.is_snake_outside() or self.snake.is_snake(head):
            return -1
        if self.is_apple_inside(head):
            return 1
        return 0

    def is_apple_inside(self, cell):
        """Check if apple is eaten"""
        res = False
        for apple in self.apples:
            if apple.pos_x == cell.pos_x and apple.pos_y == cell.pos_y:
                res = True
                break
        return res

    def is_snake_outside(self):
        """Check if snake outside of grid"""
        head = self.snake.head
        return head.pos_x < 0 or head.pos_x >= self.config.board_rows \
            or head.pos_y < self.config.banner_rows \
                or head.pos_y >= self.config.board_rows + self.config.banner_rows

    def remove_apple(self, cell):
        """Remove eaten apple from grid"""
        if self.is_apple_inside(cell):
            apple_to_remove = next(apple for apple in self.apples \
                if apple.pos_x == cell.pos_x and apple.pos_y == cell.pos_y)
            self.apples.remove(apple_to_remove)

    def seed_apples(self, level):
        """Randomly place apples on grid"""
        while len(self.apples) < level + 3:
            randx = random.randrange(self.config.board_rows)
            randy = random.randrange(self.config.banner_rows, self.config.board_rows + 1)
            if not self.is_apple_inside(Cell(randx, randy)) \
                and self.snake.head.pos_x != randx \
                and self.snake.head.pos_y != randy \
                and not self.snake.is_snake(Cell(randx, randy)):
                self.apples.append(Cell(randx, randy))
