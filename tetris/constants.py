# screen dimension
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
GRID_SIZE = 30

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# shapes and colors
SHAPES = [
    [[1, 1, 1, 1]],  # I 
    [[1, 1], [1, 1]],  # O 
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 1, 0], [0, 1, 1]],  # Z 
    [[0, 1, 1], [1, 1, 0]],  # S 
    [[1, 0, 0], [1, 1, 1]],  # L 
    [[0, 0, 1], [1, 1, 1]]   # J 
]

SHAPE_COLORS = [
    (0, 255, 255),  # Cyan
    (255, 255, 0),  # Yellow
    (128, 0, 128),  # Purple
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (255, 165, 0),  # Orange
    (0, 0, 255)     # Blue
]

BOARD_WIDTH = SCREEN_WIDTH // GRID_SIZE
BOARD_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
