# Tetris Game Configuration

# Window settings
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 500
FPS = 60

# Game board settings
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
CELL_SIZE = 20

# Colors (RGB)
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GRAY = (128, 128, 128)
COLOR_DARK_GRAY = (64, 64, 64)
COLOR_LIGHT_GRAY = (200, 200, 200)

# Tetromino colors
COLORS = {
    'I': (0, 240, 240),      # Cyan
    'O': (240, 240, 0),      # Yellow
    'T': (160, 0, 240),      # Purple
    'S': (0, 240, 0),        # Green
    'Z': (240, 0, 0),        # Red
    'J': (0, 0, 240),        # Blue
    'L': (240, 160, 0),      # Orange
}

# Game speed settings
INITIAL_DROP_SPEED = 0.5  # seconds
MIN_DROP_SPEED = 0.1
SPEED_INCREASE_PER_LEVEL = 0.05

# Scoring
SCORE_1_LINE = 100
SCORE_2_LINES = 300
SCORE_3_LINES = 500
SCORE_4_LINES = 800

# Game board offset for rendering
BOARD_OFFSET_X = 50
BOARD_OFFSET_Y = 50

# UI positions
NEXT_PIECE_X = 280
NEXT_PIECE_Y = 100
SCORE_X = 280
SCORE_Y = 250
LEVEL_X = 280
LEVEL_Y = 320
