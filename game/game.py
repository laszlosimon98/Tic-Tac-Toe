import pygame
import random

from settings import *
from gui.button import Button

class Game():
    def __init__(self, width, back) -> None:
        self.w = width
        self.h = self.w
        self.diff = 50
        self.game_over = False
        self.col = 3
        self.board = self.create_board(self.col)
        self.player1 = 'X'
        self.player2 = 'O'
        self.current_player = self.player1 if random.random() < 0.5 else self.player2
        self.font = pygame.font.SysFont("Arial", 16)
        self.isFinished = False

        self.button = Button(10, 10, 50, 20, back)
    
    def is_game_over(self) -> bool:
        return self.game_over
    
    def create_board(self, col) -> list[list]:
        arr = list()
        for i in range(col):
            arr.append(list())
            for _ in range(col):
                arr[i].append("")
        return arr
    
    def draw_lines(self, win, col, width, height) -> None:
        pygame.draw.rect(win, GREY, (0, 0, width, self.diff), 0)
        for i in range(col):
            pygame.draw.line(win, BLACK, ((i + 1) * width / col, self.diff), ((i + 1) * width / col, height))
            pygame.draw.line(win, BLACK, (0, i * (height - self.diff) / col + self.diff), (width, i * (height - self.diff) / col + self.diff))
    
    def get_mouse_index(self, pos, width, height, col) -> tuple[int, int]:
        return (pos[0] // (width // col), pos[1] // ((height + self.diff) // col))

    def draw_circle(self, win, pos, width, height, col) -> None:
        pygame.draw.circle(win, BLACK, (pos[0] * (width / col) + (width / col) / 2, pos[1] * ((height - self.diff) / col) + ((height - self.diff)/ col) / 2 + self.diff), ((height - self.diff) / col - 5) / 2, 2)

    def draw_x(self, win, pos, width, height, col) -> None:
        pygame.draw.line(win, BLACK, (pos[0] * width / col + 5, pos[1] * (height - self.diff) / col + self.diff + 5), (pos[0] * width / col + width / col - 5, pos[1] * (height - self.diff) / col + (height - self.diff) / col + self.diff - 5), 2)
        pygame.draw.line(win, BLACK, (pos[0] * width / col + 5, pos[1] * (height - self.diff) / col + (height - self.diff) / col + self.diff - 5), (pos[0] * width / col + width / col - 5, pos[1] * (height - self.diff) / col + self.diff + 5), 2)

    def turn(self, pos) -> None:
        x, y = pos
        if not self.isFinished:
            if self.board[x][y] == "":
                self.board[x][y] = self.current_player
                self.current_player = 'X' if self.current_player == 'O' else 'O'
                self.isFinished = self.check_winner()
        
    def check_winner(self) -> bool:
        for i, _ in enumerate(self.board):
            if self.board[0][i] != '' and self.board[0][i] == self.board[1][i] and self.board[0][i] == self.board[2][i] or \
               self.board[i][0] != '' and self.board[i][0] == self.board[i][1] and self.board[i][0] == self.board[i][2] or \
               self.board[0][0] != '' and self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2] or \
               self.board[2][0] != '' and self.board[2][0] == self.board[1][1] and self.board[2][0] == self.board[0][2]:
                return True
        return False

    def draw(self, win) -> None:
        self.draw_lines(win, self.col, self.w, self.h)

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 'O':
                    self.draw_circle(win, (i, j), self.w, self.h, self.col)
                elif self.board[i][j] == 'X':
                    self.draw_x(win, (i, j), self.w, self.h, self.col)

        if self.isFinished:
            winner = self.player1 if self.current_player == self.player2 else self.player2
            text = self.font.render(f"Winner is {winner}", 0, BLACK)
            win.blit(text, (self.w - text.get_width() - 5, self.diff / 2 - text.get_height() / 2))

        self.button.draw(win)

    def update(self, event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = self.get_mouse_index(pygame.mouse.get_pos(), self.w, self. h, self.col)
            self.turn(pos)
            self.button.update(event)
        
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.board = self.create_board(self.col)
            self.isFinished = False
