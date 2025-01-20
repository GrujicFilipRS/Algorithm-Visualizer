import pygame

win = pygame.display.set_mode((1200, 650), pygame.RESIZABLE)
pygame.display.set_caption('Algorithm visualizer')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    win.fill((25, 25, 25))

    pygame.display.update()