import pygame
from settings import *
pygame.init()

class Game():
    def __init__(self, width) -> None:
        self.w = width
        self.h = self.w
        self.title = pygame.display.set_caption("Tic Tac Toe")
        self.win = pygame.display.set_mode((self.w, self.h))
        self.game_over = False
        self.col = 3
        self.board = self.create_board(self.col)
        self.board[1][1] = 'X'
        self.board[1][0] = 'O'
    
    def create_board(self, col) -> list[list]:
        arr = list()
        for i in range(col):
            arr.append(list())
            for j in range(col):
                arr[i].append("")
        return arr
    
    def draw_lines(self, win, col, width, height) -> None:
        for i in range(col - 1):
            pygame.draw.line(win, BLACK, ((i + 1) * width / col, 0), ((i + 1) * width / col, height))
            pygame.draw.line(win, BLACK, (0, (i + 1) * height / col), (width, (i + 1) * height / col))
    
    def get_mouse_index(self, pos, width, height, col) -> tuple[int, int]:
        return (pos[0] // (width // col), pos[1] // (height // col))

    def draw_circle(self, win, pos, width, height, col) -> None:
        pygame.draw.circle(win, BLACK, (pos[0] * (width // col) + (width // col) / 2, pos[1] * (height // col) + (height // col) / 2), (width // col - 2) / 2, 2)

    def draw_x(self, win, pos, width, height, col) -> None:
        startX = pos[0] * (width / col)
        startY = pos[1] * (height / col)
        pygame.draw.line(win, BLACK, (startX + 5, startY + 5), (startX + (width / col) - 5, startY + (height / col) - 5), 2)
        pygame.draw.line(win, BLACK, (startX + (width / col) - 5, startY + 5), (startX + 5, startY + (height / col) - 5), 2)
        pass

    def draw(self, win) -> None:
        win.fill(WHITE)
        self.draw_lines(win, self.col, self.w, self.h)

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 'O':
                    self.draw_circle(win, (i, j), self.w, self.h, self.col)
                elif self.board[i][j] == 'X':
                    self.draw_x(win, (i, j), self.w, self.h, self.col)
        pygame.display.update()

    def update(self) -> None:
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = self.get_mouse_index(pygame.mouse.get_pos(), self.w, self. h, self.col)
                    self.board[pos[0]][pos[1]] = 'X'
            
            self.draw(self.win)

if __name__ == '__main__':
    game = Game(400)
    game.update()