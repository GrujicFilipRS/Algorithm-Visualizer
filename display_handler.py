import pygame
from load_fonts import load_fonts

from bfs import BFS

algorithm = None

def handle_pygame(id, start_pos) -> None:
    global algorithm
    pygame.init()
    font = load_fonts()
    win = pygame.display.set_mode((1200, 650), pygame.RESIZABLE)
    pygame.display.set_caption('Algorithm visualizer')

    algorithm = None
    if id == 0:
        algorithm = BFS()

    to_break = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                to_break = True
                break
            if event.type == pygame.KEYDOWN:
                algorithm.proceed()
        
        if to_break: break

        win.fill((25, 25, 25))
        
        algorithm.draw(win, font)

        pygame.display.update()