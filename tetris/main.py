import pygame
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE, BLACK, GRAY, SHAPES, SHAPE_COLORS, BOARD_WIDTH, BOARD_HEIGHT
from tetrimino import Tetrimino

# forming game window
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()

# Initialize an empty board
board = [[BLACK for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

# creating the grid
def draw_grid():
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
            rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, GRAY, rect, 1)

# Function to fix the Tetrimino on the board
def fix_piece_to_board(piece, board):
    for i, row in enumerate(piece.shape):
        for j, value in enumerate(row):
            if value:
                board[piece.y + i][piece.x + j] = piece.color


def clear_lines():
    global board  
    new_board = [row for row in board if any(color == BLACK for color in row)]

    while len(new_board) < BOARD_HEIGHT:
        new_board.insert(0, [BLACK for _ in range(BOARD_WIDTH)])
    board = new_board


def main():
    running = True
    current_piece = Tetrimino(random.choice(SHAPES), random.choice(SHAPE_COLORS))
    fall_time = 0
    fall_speed = 0.5

    while running:
        screen.fill(BLACK)
        draw_grid()

     
        for y in range(BOARD_HEIGHT):
            for x in range(BOARD_WIDTH):
                if board[y][x] != BLACK:
                    pygame.draw.rect(
                        screen,
                        board[y][x],
                        pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                    )

       
        current_piece.draw(screen)

    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if current_piece.collision(board):
                        current_piece.x += 1  
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if current_piece.collision(board):
                        current_piece.x -= 1  
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if current_piece.collision(board):
                        current_piece.y -= 1  
                if event.key == pygame.K_UP:
                    current_piece.rotate(board)

        # fall time
        fall_time += clock.get_rawtime()
        if fall_time / 1000 >= fall_speed:
            current_piece.y += 1
            if current_piece.collision(board):
                current_piece.y -= 1  
                fix_piece_to_board(current_piece, board) 
                clear_lines()  
                current_piece = Tetrimino(random.choice(SHAPES), random.choice(SHAPE_COLORS))
              
                if current_piece.collision(board):
                    running = False  
            fall_time = 0

        # screen refresh
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()