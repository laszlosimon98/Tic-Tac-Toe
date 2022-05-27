import random
import pygame
from enum import Enum

from settings import *
from game.game import Game
from gui.menu import Menu 
pygame.init()
pygame.font.init()


class TicTacToe():
    def __init__(self, width) -> None:
        self.w = width
        self.h = self.w
        self.win = pygame.display.set_mode((self.w, self.h))
        self.title = pygame.display.set_caption("Tic Tac Toe")
        self.program = Menu(width, self.game, self.exit)
        self.run = True
        self.clock = pygame.time.Clock()
    
    def game(self) -> None:
        self.program = Game(self.w, self.back, self.new_game)
    
    def exit(self) -> None:
        self.run = False
    
    def new_game(self) -> None:
        self.program = Game(self.w, self.back, self.new_game)

    def back(self) -> None:
        self.program = Menu(self.w, self.game, self.exit)

    def draw(self, win) -> None:
        win.fill(WHITE)
        self.program.draw(win)
        self.clock.tick(30)
        pygame.display.update()

    def update(self) -> None:
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                self.program.update(event)

            self.draw(self.win)

if __name__ == '__main__':
    game = TicTacToe(400)
    game.update()