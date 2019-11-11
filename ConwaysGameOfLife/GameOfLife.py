from time import sleep
import random
import pygame
import sys, os


BOARD =HEIGHT, WIDTH = 420, 420
# BOARD =HEIGHT, WIDTH = 1280, 680
CELL_SIZE = 5
DEAD_COLOR = (23, 32, 42)
ALIVE_COLOR = (93, 173, 226)
STAT_COLOR = (213, 93, 226)
SPEED = 0

class GameOfLife:

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode(BOARD)
        pygame.display.set_caption('ConwaysGameOfLife')
        i_icon = os.getcwd() + '\\ConwaysGameOfLife\\icon.PNG'
        icon = pygame.image.load(i_icon)
        pygame.display.set_icon(icon)
        self.init_grid()
        self.active_cells = 0
        self.static_cells = 0

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
                    
        
        font = pygame.font.Font(None, 18)
        text_active = font.render("active: " + str(self.active_cells), True, (173, 238, 235))
        text_static = font.render("static: " + str(self.static_cells), True, (173, 238, 235))
        place_active = text_active.get_rect(center=(HEIGHT - 50, WIDTH - 5))
        place_static = text_active.get_rect(center=(HEIGHT - 47, WIDTH - 15))

        self.screen.blit(text_active, place_active)
        self.screen.blit(text_static, place_static)
        self.active_cells = 0
        self.static_cells = 0
        pygame.display.flip()

    def initial_grid(self):
        self.draw_grid()
        OUT = True
        while OUT:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    exit()
                if events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_ESCAPE:
                        exit()
                    if events.key == pygame.K_KP_ENTER:
                        OUT = False
                    if events.key == pygame.K_r:
                        for i in range(self.row):
                            for j in range(self.col):
                                self.active_field[i][j] = random.choice([0, 1])
                        self.draw_grid()
                    if events.key == pygame.K_s:
                        self.active_field[19][20] = 1
                        self.active_field[20][21] = 1
                        self.active_field[20][22] = 1
                        self.active_field[19][22] = 1
                        self.active_field[18][22] = 1
                        self.draw_grid()
                    if events.key == pygame.K_g:
                        self.active_field[1][5] = 1
                        self.active_field[1][6] = 1
                        self.active_field[2][5] = 1
                        self.active_field[2][6] = 1

                        self.active_field[36][3] = 1
                        self.active_field[35][3] = 1
                        self.active_field[36][4] = 1
                        self.active_field[35][4] = 1
                        
                        self.active_field[11][5] = 1
                        self.active_field[11][6] = 1
                        self.active_field[11][7] = 1
                        self.active_field[12][4] = 1
                        self.active_field[12][8] = 1
                        self.active_field[13][3] = 1
                        self.active_field[13][9] = 1
                        self.active_field[14][3] = 1
                        self.active_field[14][9] = 1
                        self.active_field[15][6] = 1
                        self.active_field[16][4] = 1
                        self.active_field[16][8] = 1
                        self.active_field[17][5] = 1
                        self.active_field[17][6] = 1
                        self.active_field[17][7] = 1
                        self.active_field[18][6] = 1

                        self.active_field[21][3] = 1
                        self.active_field[21][4] = 1
                        self.active_field[21][5] = 1
                        self.active_field[22][3] = 1
                        self.active_field[22][4] = 1
                        self.active_field[22][5] = 1
                        self.active_field[23][2] = 1
                        self.active_field[23][6] = 1
                        self.active_field[25][1] = 1
                        self.active_field[25][2] = 1
                        self.active_field[25][6] = 1
                        self.active_field[25][7] = 1

                        self.draw_grid()
                if events.type == pygame.MOUSEBUTTONDOWN:
                    if events.button == 1:
                        cor_y = int(events.pos[0] / CELL_SIZE)
                        cor_x = int(events.pos[1] / CELL_SIZE)
                        self.active_field[cor_y][cor_x] = 1
                        self.draw_grid()
                    if events.button == 3:
                        cor_y = int(events.pos[0] / CELL_SIZE)
                        cor_x = int(events.pos[1] / CELL_SIZE)
                        self.active_field[cor_y][cor_x] = 0
                        self.draw_grid()
        

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
                    self.active_cells+=1
                elif (self.unactive_field[i][j] == 1):
                    if (neighbors < 2 or neighbors > 3):
                        self.active_field[i][j] = 0
                    elif (neighbors == 2 or neighbors ==3):
                        self.active_field[i][j] = 1
                        self.static_cells+=1
        

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
        self.initial_grid()
        while True:
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    exit()
                elif events.type == pygame.KEYDOWN:
                    if events.key == pygame.K_ESCAPE:
                        exit()
            
            self.update_grid()
            self.draw_grid()
            sleep(SPEED)

if __name__ == "__main__":
    game = GameOfLife()
    game.run_game()    