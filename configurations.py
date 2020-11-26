"""Snake game configuration paramaters"""
COLOR_YELLOW = (255,255,102)
COLOR_GREEN = (154,205,50)
COLOR_WHITE = (255,255,255)
COLOR_BLACK = (0,0,0)
COLOR_L_BLACK = (96,96,96)
COLOR_RED = (255,0,0)
COLOR_L_BLUE = (75,139,190)
COLOR_BLUE = (48,105,152)
COLOR_L_YELLOW = (255,232,115)
COLOR_YELLOW = (255,212,59)
COLOR_GREY = (100,100,100)
COLOR_LIGHT_GREY = (169,169,169)


CELL_SIZE = 20
BANNER_ROWS = 2
BOARD_ROWS = 30
SHOW_GRID = False

class Configurations():
    """Snake game configuration paramaters"""
    def __init__(self):
        self.cell_size = CELL_SIZE
        self.banner_rows = BANNER_ROWS
        self.board_rows = BOARD_ROWS
        self.show_grid = SHOW_GRID

        self.board_width = self.board_rows * self.cell_size
        self.center = self.board_rows // 2
