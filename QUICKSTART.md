# Tetris Game - Quick Start Guide

## Installation & Running

### 1. Install Pygame
```bash
pip install pygame==2.5.2
```

### 2. Run the Game
```bash
python main.py
```

The game window will open immediately!

## How to Play

### Controls
- **LEFT/RIGHT ARROWS** - Move piece left/right
- **DOWN ARROW** - Soft drop (move piece down)
- **UP ARROW** - Rotate piece
- **SPACE** - Hard drop (instant drop to bottom) or restart when game over

### Objective
1. Arrange falling Tetris pieces to complete horizontal lines
2. Complete lines to earn points and clear them
3. Survive as long as possible before pieces reach the top

### Scoring
- **1 line** = 100 points
- **2 lines** = 300 points
- **3 lines** = 500 points
- **4 lines (Tetris)** = 800 points

### Difficulty
- Game starts at Level 1
- Level increases every 10 lines cleared
- Speed increases with each level

## File Structure

```
tetris/
├── main.py           - Start the game here
├── config.py         - Game settings (colors, speeds, sizes)
├── shapes.py         - Tetromino piece definitions
├── board.py          - Game board logic
├── game.py           - Core game mechanics
├── utils.py          - Rendering and UI
├── test_game.py      - Unit tests (run: python test_game.py)
├── requirements.txt  - Dependencies
├── README.md         - Full documentation
└── QUICKSTART.md     - This file
```

## Testing

Run the test suite to verify everything works:
```bash
python test_game.py
```

All tests should pass with ✓ marks.

## Troubleshooting

### "ModuleNotFoundError: No module named 'pygame'"
Solution: Install pygame with `pip install pygame==2.5.2`

### Game window doesn't appear
- Make sure you're running `python main.py` from the tetris directory
- Check that pygame is properly installed

### Game runs slowly
- The game is optimized for 60 FPS
- If you experience lag, close other applications

## Game Features

✅ 7 Tetromino pieces (I, O, T, S, Z, J, L)
✅ Smooth rotation and movement
✅ Piece preview (next piece display)
✅ Score tracking
✅ Level system with progressive difficulty
✅ Line clearing detection
✅ Game over detection
✅ Restart functionality
✅ Clean, modern UI

Enjoy! 🎮
