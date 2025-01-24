import pygame
import customtkinter

def load_fonts():
    fonts = {}
    for i in range(0, 65, 2):
        fonts[i] = pygame.font.Font('./resources/Jaldi-Regular.ttf', i)
    return fonts

def tkinter_fonts():
    customtkinter.FontManager.load_font('./resources/Jaldi-Regular.ttf')