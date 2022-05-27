import pygame
from settings import *
from gui.button import Button

pygame.font.init()

class Menu:
    def __init__(self, width, start, exit) -> None:
        self.w = width
        self.start_btn= Button(width / 2 - BUTTONWIDTH / 2, 100, BUTTONWIDTH, BUTTONHEIGHT, "Start", start)
        self.exit_btn = Button(width / 2 - BUTTONWIDTH / 2, 125 + BUTTONHEIGHT, BUTTONWIDTH, BUTTONHEIGHT, "Exit", exit)
        self.font = pygame.font.SysFont("Times New Roman", 36)

    def draw(self, win) -> None:
        text = self.font.render("Tic Tac Toe", 0, BLACK)
        self.start_btn.draw(win)
        self.exit_btn.draw(win)
        win.blit(text, (self.w / 2 - text.get_width() / 2, 30))

    def update(self, event) -> None:
        self.start_btn.update(event)
        self.exit_btn.update(event)
