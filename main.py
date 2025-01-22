import pygame
from bfs import *
from load_fonts import load_fonts
from start import StartPage

def handle_pygame() -> None:
    pygame.init()
    font = load_fonts()
    win = pygame.display.set_mode((1200, 650), pygame.RESIZABLE)
    pygame.display.set_caption('Algorithm visualizer')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        win.fill((25, 25, 25))
        pygame.display.update()

if __name__ == '__main__':
    startPage = StartPage()
    startPage.show()