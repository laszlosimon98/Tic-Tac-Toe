import pygame
from settings import *
from gui.button import Button

class Menu:
    def __init__(self, width, point) -> None:
        self.w = width
        self.button = Button(100, 100, 100, 20, point)

    def draw(self, win) -> None:
        self.button.draw(win)

    def update(self, event) -> None:
        self.button.update(event)
