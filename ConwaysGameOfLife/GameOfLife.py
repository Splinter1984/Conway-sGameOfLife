from time import sleep
import random
import pygame
import sys


BOARD =HEIGHT, WIDTH = 640, 420
# BOARD =HEIGHT, WIDTH = 1280, 680
CELL_SIZE = 5
DEAD_COLOR = (23, 32, 42)
ALIVE_COLOR = (93, 173, 226)
SPEED = 1

class GameOfLife:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(BOARD)
        pygame.display.set_caption('ConwaysGameOfLife')
        self.init_field()

    def init_field(self):
        self.row = int(HEIGHT / CELL_SIZE)
        self.col = int(WIDTH / CELL_SIZE)
    
        self.field = []
        for i in range(self.row):
            self.field.append([])
            for j in range(self.col):
                self.field[i].append(0)

    def draw_grid(self):
        self.screen.fill((DEAD_COLOR))
        for i in range(self.row):
            for j in range(self.col):
                if self.field[i][j] == 1:
                    pygame.draw.circle(self.screen, ALIVE_COLOR, (i * CELL_SIZE + int(CELL_SIZE / 2), j * CELL_SIZE + int(CELL_SIZE / 2)), int(CELL_SIZE / 2))
        pygame.display.flip()

    def initial_grid(self):
        for i in range(self.row):
            for j in range(self.col):
                self.field[i][j] = random.choice([0, 1])

    # def in_bounds(y, x):
	#     if (x > 0 and y > 0 and y < HEIGHT - 1 and x < WIDTH - 1):
	# 	    return True
	#     return False

    # def neighbors_value(y, x):
    #     neighbors_count = 0
	#     for i in range(-1, 1):
	# 	    for j in range(-1, 1):     
    #             if (!(i == x and j == y) and in_Bounds(i, j) and self.field[i][j] == 1):
    #                 neighbors_count+=1
    #     return neighbors_count


    # def update_gen(self):
    #     for i in range(self.row):
    #         for j in range(self.col):
    #             neighbors = neighbors_value(i, j)
    #             if (self.field[i][j] == 0 and neighbors == 3):
    #                 self.field[i][j] = 1
    #             if (self.field[i][j] == 1 and neighbors < 2 or neighbors > 3):
    #                 self.field[i][j] = 0

    def run_game(self):
        QUIT = False
        while True:
            for event in pygame.event.get():
                if event.type == QUIT: sys.exit()
            self.initial_grid()
            self.draw_grid()
            # self.update_gen()
            sleep(SPEED)


if __name__ == "__main__":
    game = GameOfLife()
    game.run_game()    