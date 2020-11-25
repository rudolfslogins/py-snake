"""Class for game object drawing and staus tracking"""
import sys
import tkinter as tk
from tkinter import messagebox
from direction import Direction
from cell import Cell
from snake import Snake
from grid import Grid
from configurations import COLOR_RED, COLOR_BLACK, COLOR_L_BLACK, COLOR_GREEN, COLOR_WHITE
import pygame

class Game():
    """Game object"""
    def __init__(self, cf):
        self.snake = Snake()
        self.apples = [Cell(cf.center - 2, cf.center), Cell(cf.center + 2, cf.center),\
    Cell(cf.center, cf.center - 2), Cell(cf.center, cf.center + 2)]
        self.config = cf
        self.level = 1
        self.points = 0
        self.grid = Grid(self.snake, self.apples, cf)

    def draw_cell(self, surface, cell, color=(0,0,0), is_apple = False):
        """Draw cell"""
        distance = self.config.board_width // self.config.board_rows
        pos_x = cell.pos_x * self.config.cell_size
        pos_y = cell.pos_y * self.config.cell_size
        if is_apple:
            apple_radius = self.config.cell_size // 2
            pygame.draw.circle(surface, COLOR_RED, \
                (pos_x + apple_radius, pos_y + apple_radius), apple_radius)
            pygame.draw.circle(surface, COLOR_BLACK, \
                (pos_x + apple_radius + apple_radius / 1.25, pos_y + apple_radius / 4), \
                    self.config.cell_size // 4)
        else:
            pygame.draw.rect(surface, color, \
                (cell.pos_x*distance+1,cell.pos_y*distance+1, distance-1, distance-1))
            if self.snake.head == cell:
                radius = self.config.cell_size // 10
                offset = self.config.cell_size / 3
                if self.snake.direction == Direction.UP:
                    circle_middle = (pos_x + offset, pos_y + offset)
                    circle_middle2 = (pos_x + offset * 2, pos_y + offset)
                elif self.snake.direction == Direction.DOWN:
                    circle_middle = (pos_x + offset, pos_y + offset * 2)
                    circle_middle2 = (pos_x + offset * 2, pos_y + offset * 2)
                elif self.snake.direction == Direction.RIGHT:
                    circle_middle = (pos_x + 2 * offset, pos_y + offset)
                    circle_middle2 = (pos_x + 2 * offset, pos_y + 2 * offset)
                else:
                    circle_middle = (pos_x + offset, pos_y + offset)
                    circle_middle2 = (pos_x + offset, pos_y + 2 * offset)
                pygame.draw.circle(surface, COLOR_WHITE, circle_middle, radius)
                pygame.draw.circle(surface, COLOR_WHITE, circle_middle2, radius)


    def draw_grid(self, surface):
        """Draw game grid"""
        pos_x = 0
        pos_y = self.config.cell_size * self.config.banner_rows

        if self.config.show_grid:
            for _ in range(self.config.board_rows + 1):
                pygame.draw.line(surface, COLOR_WHITE, (pos_x, self.config.cell_size * 2),\
                    (pos_x, self.config.board_width + self.config.cell_size * 2))
                pygame.draw.line(surface, COLOR_WHITE, (0,pos_y),(self.config.board_width,pos_y))
                pos_x = pos_x + self.config.cell_size
                pos_y = pos_y + self.config.cell_size
        else:
            pygame.draw.line(surface, COLOR_BLACK, (pos_x, self.config.cell_size * \
                self.config.banner_rows), (pos_x, self.config.board_width + pos_y))
            pygame.draw.line(surface, COLOR_BLACK, (pos_x, self.config.cell_size * \
                self.config.banner_rows),(self.config.board_width + pos_x, pos_y))
            pygame.draw.line(surface, COLOR_BLACK, (self.config.board_width + pos_x, \
                self.config.cell_size * self.config.banner_rows),(self.config.board_width + pos_x, \
                self.config.board_width + pos_y))
            pygame.draw.line(surface, COLOR_BLACK, (self.config.board_width + pos_x, \
                self.config.board_width + pos_y),(pos_x, self.config.board_width + pos_y))

    def redraw_window(self, surface):
        """Redraw game window"""
        surface.fill(COLOR_GREEN)
        self.draw_grid(surface)
        for apple in self.apples:
            self.draw_cell(surface, apple, color=COLOR_RED, is_apple=True)

        self.draw_cell(surface, self.snake.head, color=COLOR_BLACK)
        for t_cell in self.snake.tail:
            self.draw_cell(surface, t_cell, color=COLOR_L_BLACK)
        font = pygame.font.SysFont('Arial', self.config.cell_size, True)
        img = font.render(f"Level: {self.level}  Score: {self.points}", True, COLOR_BLACK)
        surface.blit(img, (self.config.cell_size // 2, self.config.cell_size // 2))
        pygame.display.update()

    def message_box(self, subject, content):
        """Show message to player"""
        tk.Tk().withdraw()
        tk.Tk().destroy()
        messagebox.showinfo(subject, content)

    def quit_game(self):
        """Quit game"""
        pygame.quit()
        sys.exit()
