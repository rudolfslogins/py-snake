"""Snake object"""
from direction import Direction
from cell import Cell

class Snake():
    """Snake object"""
    def __init__(self):
        self.direction = Direction.RIGHT
        self.head = Cell(2, 2)
        self.tail = [Cell(0,2), Cell(1,2)]
        self.tail_size = 2

    def set_direction(self, direction):
        """Set snake moving direction"""
        if direction == Direction.RIGHT \
            and self.is_snake(Cell(self.head.pos_x + 1, self.head.pos_y)):
            self.direction = self.direction
        elif direction == Direction.LEFT \
            and self.is_snake(Cell(self.head.pos_x - 1, self.head.pos_y)):
            self.direction = self.direction
        elif direction == Direction.UP and self.is_snake(Cell(self.head.pos_x, self.head.pos_y -1)):
            self.direction = self.direction
        elif direction == Direction.DOWN \
            and self.is_snake(Cell(self.head.pos_x, self.head.pos_y + 1)):
            self.direction = self.direction
        else:
            self.direction = direction

    def move(self):
        """Move snake"""
        self.tail.append(self.head)
        if self.tail_size < len(self.tail):
            self.tail.remove(self.tail[0])
        if self.direction == Direction.RIGHT:
            self.head = Cell(self.head.pos_x + 1, self.head.pos_y)
        elif self.direction == Direction.LEFT:
            self.head = Cell(self.head.pos_x - 1, self.head.pos_y)
        elif self.direction == Direction.UP:
            self.head = Cell(self.head.pos_x, self.head.pos_y - 1)
        elif self.direction == Direction.DOWN:
            self.head = Cell(self.head.pos_x, self.head.pos_y + 1)

    def grow(self):
        """Grow snake"""
        self.tail_size += 2

    def is_snake(self, cell):
        """Check if cell is in snake position"""
        res = False
        for t_cell in self.tail:
            if t_cell.pos_x == cell.pos_x and t_cell.pos_y == cell.pos_y:
                res = True
                break
        return res
