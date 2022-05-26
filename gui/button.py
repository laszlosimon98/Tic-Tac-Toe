import pygame
from settings import *

class Button:
    def __init__(self, x_pos, y_pos, width, height, function) -> None:
        self.x = x_pos
        self.y = y_pos
        self.w = width
        self.h = height
        self.f = function
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
    
    def draw(self, win) -> None:
        pygame.draw.rect(win, BLACK, self.rect, 1)
    
    def update(self, event) -> None:
        mouse_pos = pygame.mouse.get_pos()
        r_in = pygame.Rect.collidepoint(self.rect, mouse_pos)

        if r_in and event.type == pygame.MOUSEBUTTONDOWN:
            self.f()