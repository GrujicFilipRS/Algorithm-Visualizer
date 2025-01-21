import pygame

class BFS:
    def __init__(self) -> None:
        self.elements = [
            [0, 0, 1, 1, 0],
            [0, 0, 1, 1, 0],
            [1, 1, 0, 1, 1],
            [1, 1, 1, 0, 0],
        ]
        self.animation_ind = 0

        self.clearing: bool = False
        self.current_ind: list[int] = [0, 0]
        self.highlighted_red: list[list[int]] = []
        self.highlighted_green: list[list[int]] = []
        self.highlighted_blue: list[list[int]] = []

    def proceed(self) -> None:
        self.animation_ind += 1
        if self.animation_ind == 1:
            self.highlighted_red.append(self.current_ind)
            return
        
        if not self.clearing:
            if self.elements[self.current_ind[0]][self.current_ind[1]] == 0:
                self.highlighted_red.clear()
                self.current_ind[1] += 1
                if self.current_ind[1] >= len(self.elements[0]):
                    self.current_ind[1] = 0
                    self.current_ind[0] += 1
                
                self.highlighted_red.append(self.current_ind)
            else:
                self.highlighted_red.clear()
                self.highlighted_blue.append(self.current_ind)
                self.clearing = True
        else:
            pass

    def draw(self, win, font) -> None:
        ELEMENT_WIDTH = 80
        ELEMENT_HEIGHT = 80
        MARGIN = (30, 30)
        OFFSET = ((1200 - len(self.elements[0]) * (ELEMENT_WIDTH + MARGIN[0]) + MARGIN[0]) / 2, (650 - len(self.elements) * (ELEMENT_HEIGHT + MARGIN[1]) + MARGIN[1]) / 2)
        for i in range(len(self.elements)):
            for j in range(len(self.elements[0])):
                color = (255, 255, 255)
                if [i, j] in self.highlighted_red:
                    color = (255, 0, 0)
                elif [i, j] in self.highlighted_blue:
                    color = (0, 0, 255)
                elif [i, j] in self.highlighted_green:
                    color = (0, 255, 0)
                pos = (j * ELEMENT_WIDTH + OFFSET[0] + MARGIN[0] * j, i * ELEMENT_HEIGHT + OFFSET[1] + MARGIN[0] * i)
                circle_pos = (j * ELEMENT_WIDTH + OFFSET[0] + ELEMENT_WIDTH / 2 + MARGIN[0] * j, i * ELEMENT_HEIGHT + OFFSET[1] + ELEMENT_HEIGHT / 2 + MARGIN[0] * i)
                pygame.draw.circle(win, color, circle_pos, ELEMENT_WIDTH / 2, 1)
                text = font[32].render(f'{self.elements[i][j]}', True, color, None)
                win.blit(text, (pos[0] + ELEMENT_WIDTH / 2 - text.get_width() / 2, pos[1] + ELEMENT_HEIGHT / 2 - text.get_height() / 2))