import pygame
import time
import random

class Game_Of_Life:
    def __init__(self):
        self.rows, self.cols = (101, 101)
        self.__half_rows, self.__half_cols = (int(self.rows / 2), int(self.cols / 2))
        self.matrix = [[0 for i in range(self.cols)] for j in range(self.rows)]
        # Getting alive cells of Quadrant 2, 3, 4
        for i in range(self.__half_rows):
            for j in range(self.__half_cols):
                self.matrix[i][j] = random.randrange(0, 2)
                if self.matrix[i][j] == 1:
                    self.matrix[i][self.cols - 1 - j] = 1
                    self.matrix[self.rows - 1 - i][j] = 1
                    self.matrix[self.rows - 1 - i][self.cols - 1 - j] = 1    

    def display_matrix(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print("  " + str(self.matrix[i][j]) + " ", end = " ")
            print("\n")

    def game_rules(self):
        modifying_cells = []
        for i in range(self.rows):
            for j in range(self.cols):
                neighbours = []
                neighbours.append((i - 1, j - 1))
                neighbours.append((i - 1, j + 1))
                neighbours.append((i + 1, j - 1))
                neighbours.append((i + 1, j + 1))
                neighbours.append((i    , j - 1))
                neighbours.append((i    , j + 1))
                neighbours.append((i - 1, j    ))
                neighbours.append((i + 1, j    ))
                alive_neighbours = 0
                for neighbour in neighbours:
                    if (neighbour[0] >= 0 and neighbour[0] < self.rows and neighbour[1] >= 0 and neighbour[1] < self.cols):
                        if self.matrix[neighbour[0]][neighbour[1]] == 1:
                            alive_neighbours = alive_neighbours + 1
                if self.matrix[i][j] == 1:
                    # Death by underpopulation
                    if alive_neighbours < 2:
                        modifying_cells.append((i, j))
                    # sustainable life
                    if alive_neighbours == 2 or alive_neighbours == 3:
                        continue
                    # Death by overpopulation
                    if alive_neighbours > 3:
                        modifying_cells.append((i, j))
                else:
                    # birth
                    if alive_neighbours == 3:
                        modifying_cells.append((i, j))
        for cells in modifying_cells:
            if self.matrix[cells[0]][cells[1]] == 1:
                self.matrix[cells[0]][cells[1]] = 0
            else:
                self.matrix[cells[0]][cells[1]] = 1

def main():
    obj = Game_Of_Life()
    pygame.init()

    r = 5
    display_width = obj.rows * r
    display_height = obj.cols * r

    pink = (255,182,193)
    hotpink = (255,105,180)

    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Game Of Life")
    clock = pygame.time.Clock()

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        for row in range(display_width):
            for col in range(display_height):
                x, y = (int(row / r), int(col / r))
                if obj.matrix[x][y] == 1:
                    pygame.draw.rect(gameDisplay, hotpink, [row, col, r, r])
                else:
                    pygame.draw.rect(gameDisplay, pink, [row, col, r, r])
                col = col + r
            row = row + r
            
        obj.game_rules()

        pygame.display.update()
        clock.tick(1000000000)
        
        # obj.display_matrix()
        # print("\n------------------------------------------------------\n")
        # time.sleep(2)

main()