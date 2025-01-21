import pygame
from algorithm import *
from load_fonts import load_fonts

if __name__ == '__main__':
    pygame.init()
    font = load_fonts()

    win = pygame.display.set_mode((1200, 650), pygame.RESIZABLE)
    pygame.display.set_caption('Algorithm visualizer')

    bfs = BFS()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        win.fill((25, 25, 25))

        bfs.draw(win, font)

        pygame.display.update()