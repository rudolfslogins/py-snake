"""Snake game in python"""
from pathlib import Path

import pygame
from direction import Direction
from game import Game
from configurations import Configurations

pygame.init()
pygame.display.set_caption("PySnake")
abs_path = str(Path("images\png-snake-icon.png").absolute()).replace('\\','\\\\')
icon = pygame.image.load(abs_path)
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

cf = Configurations()
game = Game(cf)
win = pygame.display.set_mode((cf.board_width + 1, cf.board_width + 1 + cf.cell_size * 2))

# Main game loop
while True:
    pygame.time.delay(260 - game.level * 20)
    clock.tick(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.quit_game()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                game.snake.set_direction(Direction.RIGHT)
            elif event.key == pygame.K_LEFT:
                game.snake.set_direction(Direction.LEFT)
            elif event.key == pygame.K_UP:
                game.snake.set_direction(Direction.UP)
            elif event.key == pygame.K_DOWN:
                game.snake.set_direction(Direction.DOWN)

    game.snake.move()
    STATE = game.grid.check_snake_state()
    if STATE == -1:
        game.message_box("GAME OVER", f"You lost\nLevel: {game.level} Score: {game.points}")
        break
    if STATE == 1:
        game.snake.grow() 
        game.grid.remove_apple(game.snake.head)
        game.points += 100
        if len(game.apples) < 1:
            game.level += 1
            game.grid.seed_apples(game.level)
    game.redraw_window(win)
