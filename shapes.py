# Tetris Shapes (Tetrominoes)

# Each shape is represented as a list of rotation states
# Each rotation state is a list of (x, y) coordinates relative to the piece's origin

SHAPES = {
    'I': [
        [(0, 1), (1, 1), (2, 1), (3, 1)],  # Horizontal
        [(1, 0), (1, 1), (1, 2), (1, 3)],  # Vertical
        [(0, 1), (1, 1), (2, 1), (3, 1)],  # Horizontal
        [(1, 0), (1, 1), (1, 2), (1, 3)],  # Vertical
    ],
    'O': [
        [(0, 0), (1, 0), (0, 1), (1, 1)],  # Square
        [(0, 0), (1, 0), (0, 1), (1, 1)],  # Square
        [(0, 0), (1, 0), (0, 1), (1, 1)],  # Square
        [(0, 0), (1, 0), (0, 1), (1, 1)],  # Square
    ],
    'T': [
        [(1, 0), (0, 1), (1, 1), (2, 1)],  # T pointing up
        [(1, 0), (1, 1), (2, 1), (1, 2)],  # T pointing right
        [(0, 1), (1, 1), (2, 1), (1, 2)],  # T pointing down
        [(1, 0), (0, 1), (1, 1), (1, 2)],  # T pointing left
    ],
    'S': [
        [(1, 0), (2, 0), (0, 1), (1, 1)],  # S horizontal
        [(1, 0), (1, 1), (2, 1), (2, 2)],  # S vertical
        [(1, 0), (2, 0), (0, 1), (1, 1)],  # S horizontal
        [(1, 0), (1, 1), (2, 1), (2, 2)],  # S vertical
    ],
    'Z': [
        [(0, 0), (1, 0), (1, 1), (2, 1)],  # Z horizontal
        [(2, 0), (1, 1), (2, 1), (1, 2)],  # Z vertical
        [(0, 0), (1, 0), (1, 1), (2, 1)],  # Z horizontal
        [(2, 0), (1, 1), (2, 1), (1, 2)],  # Z vertical
    ],
    'J': [
        [(0, 0), (0, 1), (1, 1), (2, 1)],  # J
        [(1, 0), (2, 0), (1, 1), (1, 2)],  # J rotated
        [(0, 1), (1, 1), (2, 1), (2, 0)],  # J rotated
        [(1, 0), (1, 1), (0, 2), (1, 2)],  # J rotated
    ],
    'L': [
        [(2, 0), (0, 1), (1, 1), (2, 1)],  # L
        [(1, 0), (1, 1), (1, 2), (2, 2)],  # L rotated
        [(0, 1), (1, 1), (2, 1), (0, 0)],  # L rotated
        [(0, 0), (1, 0), (1, 1), (1, 2)],  # L rotated
    ],
}

SHAPE_COLORS = {
    'I': 'I',
    'O': 'O',
    'T': 'T',
    'S': 'S',
    'Z': 'Z',
    'J': 'J',
    'L': 'L',
}
