import pygame
from settings import *
pygame.init()

class Game():
    def __init__(self, width, height) -> None:
        self.w = width
        self.h = height
        self.title = pygame.display.set_caption("Tic Tac Toe")
        self.win = pygame.display.set_mode((self.w, self.h))
        self.game_over = False
    
    def draw(self, win):
        win.fill(WHITE)
        pygame.display.update()

    def update(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
            
            self.draw(self.win)

if __name__ == '__main__':
    game = Game(400, 400)
    game.update()