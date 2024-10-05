# tetrimino.py

import pygame
from constants import GRID_SIZE, BOARD_WIDTH, BOARD_HEIGHT, BLACK

# tetrimino.py

class Tetrimino:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.x = BOARD_WIDTH // 2 - len(shape[0]) // 2
        self.y = 0

    def draw(self, screen):
        for i, row in enumerate(self.shape):
            for j, value in enumerate(row):
                if value:
                    pygame.draw.rect(
                        screen,
                        self.color,
                        pygame.Rect(
                            (self.x + j) * GRID_SIZE,
                            (self.y + i) * GRID_SIZE,
                            GRID_SIZE,
                            GRID_SIZE
                        )
                    )

    def collision(self, board):
        # checking if theres board collision
        for i, row in enumerate(self.shape):
            for j, value in enumerate(row):
                if value:
                    # boundary check
                    if (
                        self.x + j < 0 or
                        self.x + j >= BOARD_WIDTH or
                        self.y + i >= BOARD_HEIGHT
                    ):
                        return True
                    # Check collision with fixed blocks on the board
                    if self.y + i >= 0 and board[self.y + i][self.x + j] != BLACK:
                        return True
        return False

    def rotate(self, board):
        # rotate and change 
        new_shape = [list(row) for row in zip(*self.shape[::-1])]
        original_x = self.x
        original_y = self.y

        self.shape = new_shape

        if self.collision(board):
            self.shape = [list(row) for row in zip(*new_shape[::-1])]
