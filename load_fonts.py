import pygame

def load_fonts():
    fonts = {}
    for i in range(0, 33, 2):
        fonts[i] = pygame.font.Font('./resources/Jaldi-Regular.ttf', i)
    return fonts