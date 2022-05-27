import pygame
from settings import *

pygame.font.init()

class Button:
    def __init__(self, x_pos, y_pos, width, height, title, function) -> None:
        self.x = x_pos
        self.y = y_pos
        self.w = width
        self.h = height
        self.t = title
        self.f = function
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.font = pygame.font.SysFont("Times New Roman", 18)

    
    def draw(self, win) -> None:
        text = self.font.render(self.t, 0, BLACK)
        pygame.draw.rect(win, BLACK, self.rect, 1)
        win.blit(text, (self.x + self.w / 2 - text.get_width() / 2, self.y + self.h / 2 - text.get_height() / 2))

    
    def update(self, event) -> None:
        mouse_pos = pygame.mouse.get_pos()
        r_in = pygame.Rect.collidepoint(self.rect, mouse_pos)

        if r_in and event.type == pygame.MOUSEBUTTONDOWN:
            self.f()