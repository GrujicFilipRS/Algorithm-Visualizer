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

        self.elements_completed = []
    
    def verify_start_pos(self, start_pos) -> int:
        if type(start_pos) != type([]):
            return 2 # Incorrect type/format of starting position

        if len(start_pos) != 4:
            return 2 # Incorrect length of outer string

        try:
            for i in start_pos:
                if len(i) != 5:
                    return 2 # Incorrect length of inner string
        except:
            return 2 # Must be 2 dimensional graph

        for i in range(len(start_pos)):
            for j in range(len(start_pos)):
                if start_pos[i][j] not in [0, 1]:
                    return 2 # Incorrect value of elements of inner lists
        
        return 0

    def proceed(self) -> None:
        if self.current_ind == [len(self.elements)-1, len(self.elements[0])-1]:
            return 0

        def increment_current_ind() -> bool:
            self.current_ind[1] += 1
            if self.current_ind[1] >= len(self.elements[0]):
                self.current_ind[1] = 0
                self.current_ind[0] += 1
                if self.current_ind[0] >= len(self.elements):
                    return True
            return False

        self.animation_ind += 1
        if self.animation_ind == 1:
            self.highlighted_red.append(self.current_ind)
            return
        
        if not self.clearing:
            if self.elements[self.current_ind[0]][self.current_ind[1]] == 0:
                self.highlighted_red.clear()
                increment_current_ind()
                
                self.highlighted_red.append([self.current_ind[0], self.current_ind[1]])
            else:
                self.highlighted_red.clear()
                self.highlighted_blue.append([self.current_ind[0], self.current_ind[1]])
                self.elements_completed.append([[self.current_ind[0], self.current_ind[1]]])
                self.clearing = True
        else:
            def get_next_to(i, j):
                next_to_current = [
                    [i - 1, j] if i != 0 else None,
                    [i + 1, j] if i != len(self.elements) - 1 else None,
                    [i, j - 1] if j != 0 else None,
                    [i, j + 1] if j != len(self.elements[0]) - 1 else None,
                ]
                try:
                    while True:
                        next_to_current.remove(None)
                except:
                    pass
                
                return next_to_current
            
            if len(self.highlighted_green) == 0:
                self.elements[self.current_ind[0]][self.current_ind[1]] = 0
                next_to = get_next_to(self.current_ind[0], self.current_ind[1])
                for coord in next_to:
                    if self.elements[coord[0]][coord[1]] == 1:
                        self.highlighted_green.append(coord)
                
                if self.clearing and len(self.highlighted_green) == 0:
                    self.clearing = False
            else:
                coords: list[list[int]] = self.highlighted_green[:]
                
                for coord in coords:
                    self.elements[coord[0]][coord[1]] = 0
                    self.highlighted_green.remove(coord)
                    self.highlighted_blue.append(coord)
                    self.elements_completed[-1].append(coord)

                    next_to = get_next_to(coord[0], coord[1])
                    for new_coord in next_to:
                        if self.elements[new_coord[0]][new_coord[1]] == 1:
                            self.highlighted_green.append(new_coord)

    def draw(self, win, font) -> None:
        ELEMENT_WIDTH: int = 80
        ELEMENT_HEIGHT: int = 80
        MARGIN: tuple[int] = (30, 30)
        OFFSET: tuple[int] = ((1200 - len(self.elements[0]) * (ELEMENT_WIDTH + MARGIN[0]) + MARGIN[0]) // 2, (650 - len(self.elements) * (ELEMENT_HEIGHT + MARGIN[1]) + MARGIN[1]) // 2)
        for i in range(len(self.elements)):
            for j in range(len(self.elements[0])):
                color = (255, 255, 255)
                if [i, j] in self.highlighted_red:
                    color = (255, 0, 0)
                elif [i, j] in self.highlighted_blue:
                    color = (0, 150, 255)
                elif [i, j] in self.highlighted_green:
                    color = (0, 200, 0)
                pos = (j * ELEMENT_WIDTH + OFFSET[0] + MARGIN[0] * j, i * ELEMENT_HEIGHT + OFFSET[1] + MARGIN[0] * i)
                circle_pos = (j * ELEMENT_WIDTH + OFFSET[0] + ELEMENT_WIDTH / 2 + MARGIN[0] * j, i * ELEMENT_HEIGHT + OFFSET[1] + ELEMENT_HEIGHT / 2 + MARGIN[0] * i)
                pygame.draw.circle(win, color, circle_pos, ELEMENT_WIDTH / 2, 1)
                text = font[32].render(f'{self.elements[i][j]}', True, color, None)
                win.blit(text, (pos[0] + ELEMENT_WIDTH / 2 - text.get_width() / 2, pos[1] + ELEMENT_HEIGHT / 2 - text.get_height() / 2))
        
        continue_txt: pygame.Surface = font[28].render('Press any key to step forward', True, (255, 255, 255), None)
        continue_txt_pos = [600 - continue_txt.get_width() // 2, 550]
        if self.animation_ind == 0:
            win.blit(continue_txt, continue_txt_pos)
        
        esc_txt: pygame.Surface = font[16].render('Press ESC to leave the visualization', True, (150, 0, 0), None)
        esc_txt_pos = [5, 625]
        win.blit(esc_txt, esc_txt_pos)