import pygame
from load_fonts import load_fonts

from bfs import BFS

algorithm = None

def handle_pygame(id, start_pos) -> int:
    global algorithm

    true_start = ''
    try:
        true_start = eval(start_pos)
    except:
        return 1 # Bad evaluation of starting position

    algorithm = None
    if id == 0:
        algorithm = BFS()

    startpos_status = algorithm.verify_start_pos(true_start)
    if startpos_status != 0: return startpos_status
    else: algorithm.elements = true_start

    pygame.init()
    font = load_fonts()
    win = pygame.display.set_mode((1200, 650), pygame.RESIZABLE)
    pygame.display.set_caption('Algorithm visualizer')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0
            if event.type == pygame.KEYDOWN:
                algorithm.proceed()

        win.fill((25, 25, 25))
        
        algorithm.draw(win, font)

        pygame.display.update()