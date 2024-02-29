from Visualization import *

pygame.init()


class Menu:
    def __init__(self):
        self.option_surface = []
        self.call_back = []
        self.current_option_index = 0

    def append_option(self, option, callback):
        self.option_surface.append(font_large.render(option, True, (255, 255, 255)))
        self.call_back.append(callback)

    def switch(self, direction):
        self.current_option_index = max(0, min(self.current_option_index + direction, len(self.option_surface) - 1))

    def select(self):
        self.call_back[self.current_option_index]()

    def draw_menu(self, surf, x, y, option_y_padding):
        for i, option in enumerate(self.option_surface):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self.current_option_index:
                pygame.draw.rect(surf, (0, 100, 0), option_rect)
            surf.blit(option, option_rect)
