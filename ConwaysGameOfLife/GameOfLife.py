from time import sleep
import random
import pygame
import sys


BOARD =HEIGHT, WIDTH = 420, 420
# BOARD =HEIGHT, WIDTH = 1280, 680
CELL_SIZE = 5
DEAD_COLOR = (23, 32, 42)
ALIVE_COLOR = (93, 173, 226)
STAT_COLOR = (213, 93, 226)
SPEED = 0.03

class GameOfLife:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(BOARD)
        pygame.display.set_caption('ConwaysGameOfLife')
        self.init_grid()

    def init_grid(self):
        self.row = int(HEIGHT / CELL_SIZE)
        self.col = int(WIDTH / CELL_SIZE)
    
        self.active_field = []
        self.unactive_field = []
        for i in range(self.row):
            self.active_field.append([])
            self.unactive_field.append([])
            for j in range(self.col):
                self.active_field[i].append(0)
                self.unactive_field[i].append(0)

    def draw_grid(self):
        self.screen.fill((DEAD_COLOR))
        
        for i in range(self.row):
            for j in range(self.col):
                if self.active_field[i][j] == 1:
                    pygame.draw.circle(self.screen, ALIVE_COLOR, (i * CELL_SIZE + int(CELL_SIZE / 2), j * CELL_SIZE + int(CELL_SIZE / 2)), int(CELL_SIZE / 2))
                if self.active_field[i][j] == 0:
                    pygame.draw.circle(self.screen, DEAD_COLOR, (i * CELL_SIZE + int(CELL_SIZE / 2), j * CELL_SIZE + int(CELL_SIZE / 2)), int(CELL_SIZE / 2))
                if ((self.active_field[i][j] == self.unactive_field[i][j]) and self.active_field[i][j] == 1):
                    pygame.draw.circle(self.screen, STAT_COLOR, (i * CELL_SIZE + int(CELL_SIZE / 2), j * CELL_SIZE + int(CELL_SIZE / 2)), int(CELL_SIZE / 2))
        pygame.display.flip()

    def initial_grid(self):
        for i in range(self.row):
            for j in range(self.col):
                self.active_field[i][j] = random.choice([0, 1])
        # self.active_field[20][20] = 1
        # self.active_field[20][21] = 1
        # self.active_field[20][22] = 1
        # self.active_field[19][21] = 1
        # self.active_field[18][22] = 1


    def update_grid(self):
        for i in range(self.row):
            for j in range(self.col):
                self.unactive_field[i][j] = self.active_field[i][j]
                self.active_field[i][j] = 0
        for i in range(self.row):
            for j in range(self.col):
                neighbors = self.neighbors_value(i, j)
                if (self.unactive_field[i][j] == 0 and neighbors == 3):
                    self.active_field[i][j] = 1
                elif (self.unactive_field[i][j] == 1):
                    if (neighbors < 2 or neighbors > 3):
                        self.active_field[i][j] = 0
                    elif (neighbors == 2 or neighbors ==3):
                        self.active_field[i][j] = 1
        

    def in_bounds(self, y, x):
        if ((x > 0 and x < int(WIDTH / CELL_SIZE)) and (y > 0 and y < int(HEIGHT / CELL_SIZE))):
            return True
        return False

    def neighbors_value(self, y, x):
        neighbors_count = 0
        for i in [-1, 0, 1]:    
            for j in  [-1, 0, 1]:
                if (not(i == 0 and j == 0) and self.in_bounds(y + i, x + j)):
                    if (self.unactive_field[y + i][x + j] == 1):
                        neighbors_count+=1
        return neighbors_count


    def run_game(self):
        QUIT = False
        self.initial_grid()
        self.draw_grid()
        while True:
            for event in pygame.event.get():
                if event.type == QUIT: sys.exit()
            
            self.update_grid()
            self.draw_grid()
            sleep(SPEED)


if __name__ == "__main__":
    game = GameOfLife()
    game.run_game()    