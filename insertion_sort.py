import pygame

class InsertionSort:
    def __init__(self) -> None:
        self.elements: list[int] = [6, 4, 3, 7, 2, 8, 1, 5]
        self.animation_ind: int = 0

        self.current_inds: list[int] = [0, 1]
        self.highlighted_red: list[int] = []
        self.highlighted_green: list[int] = []
        self.highlighted_blue: list[int] = []
    
    def verify_start_pos(self, start_pos) -> int:
        if type(start_pos) != type([]):
            return 2

        if len(start_pos) > 8:
            return 2

        try:
            for i in start_pos:
                if i > 8 or i < 1:
                    return 2
        except:
            return 2

        return 0

    def draw(self, win, font):
        ELEMENT_WIDTH: int = 60
        ELEMENT_HEIGHT_SEGMENT: int = 60
        ELEMENT_GAP: int = 5
        OFFSET = (600 - ((ELEMENT_WIDTH + ELEMENT_GAP) * len(self.elements) - ELEMENT_GAP) // 2, 50)

        continue_txt: pygame.Surface = font[28].render('Press any key to step forward', True, (255, 255, 255), None)
        continue_txt_pos = [600 - continue_txt.get_width() // 2, 550]
        if self.animation_ind == 0:
            win.blit(continue_txt, continue_txt_pos)
        
        esc_txt: pygame.Surface = font[16].render('Press ESC to leave the visualization', True, (150, 0, 0), None)
        esc_txt_pos = [5, 625]
        win.blit(esc_txt, esc_txt_pos)

        for i, value in enumerate(self.elements):
            color = (255, 255, 255)
            if i in self.highlighted_green:
                color = (0, 200, 0)
            if i in self.highlighted_blue:
                color = (0, 150, 255)
            if i in self.highlighted_red:
                color = (255, 0, 0)
            pygame.draw.rect(win, color, pygame.Rect(OFFSET[0]+i*(ELEMENT_WIDTH+ELEMENT_GAP), OFFSET[1] + (8 - value) * ELEMENT_HEIGHT_SEGMENT, ELEMENT_WIDTH, ELEMENT_HEIGHT_SEGMENT * value))
            value_txt = font[24].render(f'{value}', True, color, None)
            pos_value_txt = (OFFSET[0]+i*(ELEMENT_WIDTH+ELEMENT_GAP) + ELEMENT_WIDTH // 2 - value_txt.get_width() // 2, OFFSET[1] + (8 - value) * ELEMENT_HEIGHT_SEGMENT - 35)
            win.blit(value_txt, pos_value_txt)
    
    def proceed(self):
        if self.animation_ind == 0:
            self.highlighted_blue += self.current_inds
            self.animation_ind += 1
            return
        
        if len(self.highlighted_blue) != 0: # There is something to be checked (and flipped)
            self.highlighted_blue.clear()

            i = self.current_inds[0]
            j = self.current_inds[1]
            a = self.elements[i]
            b = self.elements[j]
            if a > b:
                self.elements[i] = b
                self.elements[j] = a
            
            #self.highlighted_blue += self.current_inds
            self.current_inds = [j, j + 1]
            if j + 1 >= len(self.elements):
                self.current_inds = [0, 1]
                if self.elements == sorted(self.elements):
                    return 0
            self.highlighted_blue.clear()
            self.highlighted_blue += self.current_inds
            self.animation_ind += 1
            return
        
        # There is something to be highlighted
        self.highlighted_blue.clear()
        self.highlighted_blue += self.current_inds
        
        self.animation_ind += 1
    