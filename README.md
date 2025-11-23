# TETRIS Game - Python + Pygame

A complete, fully functional Tetris game implementation in Python using Pygame.

## Features

### Gameplay
- ✅ Standard Tetris blocks (I, J, L, O, S, T, Z)
- ✅ 90° rotation (Up key)
- ✅ Left/Right movement (Arrow keys)
- ✅ Soft drop (Down key)
- ✅ Hard drop (Space key)
- ✅ Line clearing with score calculation
- ✅ Progressive difficulty (speed increases with level)
- ✅ Game over detection

### Scoring System
- 1 line = 100 points
- 2 lines = 300 points
- 3 lines = 500 points
- 4 lines (Tetris) = 800 points
- Level increases every 10 lines cleared

### UI
- 10×20 game board with grid
- Next piece preview
- Current score display
- Current level display
- Game over screen with restart option
- Colored blocks for each piece type

### Technical
- 60 FPS stable frame rate
- Clean, modular code architecture
- PEP8 compliant
- Well-commented code

## Installation

### Requirements
- Python 3.7+
- Pygame 2.5.2

### Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the game:
```bash
python main.py
```

## Controls

| Key | Action |
|-----|--------|
| **LEFT ARROW** | Move piece left |
| **RIGHT ARROW** | Move piece right |
| **DOWN ARROW** | Soft drop (move down) |
| **UP ARROW** | Rotate piece |
| **SPACE** | Hard drop (instant drop) / Restart (when game over) |

## File Structure

```
tetris/
├── main.py          # Main application entry point
├── config.py        # Game configuration (colors, sizes, speeds)
├── shapes.py        # Tetromino shape definitions
├── board.py         # Game board logic
├── game.py          # Core game logic and Tetromino class
├── utils.py         # Rendering and UI
├── requirements.txt # Python dependencies
└── README.md        # This file
```

## Game Rules

1. Pieces fall from the top of the board
2. Rotate pieces to fit them into gaps
3. Complete horizontal lines to clear them
4. Game ends when pieces stack to the top
5. Level increases every 10 lines cleared
6. Game speed increases with each level

## Code Quality

- Clean separation of concerns (config, shapes, board, game logic, rendering)
- No hardcoded values (all in config.py)
- Proper object-oriented design
- Comprehensive comments and docstrings
- PEP8 compliant code style

## Performance

- Stable 60 FPS
- Efficient grid-based collision detection
- Optimized rendering

Enjoy the game! 🎮
