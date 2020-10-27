import pygame

pygame.init()

display_width = 550
display_height = 550

pink = (255,182,193)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Game Of Life")
clock = pygame.time.Clock()

def game_loop():

    while True:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        for row in range(550):
            for col in range(550):
                pygame.draw.rect(gameDisplay, pink, [row, col, 50, 50])
                col = col + 50
            row = row + 50
            

        pygame.display.update()
        clock.tick(40)

game_loop()