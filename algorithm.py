import pygame

class Algorithm:
    def __init__(self) -> None:
        self.elements = []
        self.animation_ind = 0

class BFS(Algorithm):
    def __init__(self) -> None:
        self.elements = [
            [0, 0, 1, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 1, 1, 1],
            [0, 0, 1, 1, 0],
        ]

    def draw(self, win, font) -> None:
        ELEMENT_WIDTH = 80
        ELEMENT_HEIGHT = 80
        MARGIN = (30, 30)
        OFFSET = ((1200 - len(self.elements[0]) * (ELEMENT_WIDTH + MARGIN[0]) + MARGIN[0]) / 2, (650 - len(self.elements) * (ELEMENT_HEIGHT + MARGIN[1]) + MARGIN[1]) / 2)
        for i in range(len(self.elements)):
            for j in range(len(self.elements[0])):
                pos = (j * ELEMENT_WIDTH + OFFSET[0] + MARGIN[0] * j, i * ELEMENT_HEIGHT + OFFSET[1] + MARGIN[0] * i)
                circle_pos = (j * ELEMENT_WIDTH + OFFSET[0] + ELEMENT_WIDTH / 2 + MARGIN[0] * j, i * ELEMENT_HEIGHT + OFFSET[1] + ELEMENT_HEIGHT / 2 + MARGIN[0] * i)
                pygame.draw.circle(win, (255, 255, 255), circle_pos, ELEMENT_WIDTH / 2, 1)
                text = font[32].render(f'{self.elements[i][j]}', True, (255, 255, 255), None)
                win.blit(text, (pos[0] + ELEMENT_WIDTH / 2 - text.get_width() / 2, pos[1] + ELEMENT_HEIGHT / 2 - text.get_height() / 2))