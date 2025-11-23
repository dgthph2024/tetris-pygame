# Tetris Game - Code Walkthrough

## Quick Overview

This document provides a detailed walkthrough of the Tetris game codebase, explaining how each component works and how they interact.

## 1. config.py - Game Configuration

**Purpose**: Centralize all game constants and settings.

**Key Constants**:
- `WINDOW_WIDTH = 400, WINDOW_HEIGHT = 500` - Game window size
- `BOARD_WIDTH = 10, BOARD_HEIGHT = 20` - Game board dimensions
- `CELL_SIZE = 20` - Size of each grid cell in pixels
- `COLORS` - Dictionary mapping piece types to RGB colors
- `SCORE_*_LINES` - Points for clearing 1, 2, 3, or 4 lines
- `INITIAL_DROP_SPEED = 0.5` - Initial piece drop speed in seconds

**Why**: Centralizing constants makes the game easy to configure without touching code logic.

## 2. shapes.py - Tetromino Definitions

**Purpose**: Define all 7 Tetris piece shapes and their rotations.

**Structure**:
```python
SHAPES = {
    'I': [rotation_0, rotation_1, rotation_2, rotation_3],
    'O': [...],
    'T': [...],
    # ... etc
}
```

**How Rotations Work**:
- Each piece has 4 rotation states
- Each rotation is a list of (x, y) coordinates relative to the piece's origin
- Example: I piece horizontal = [(0,1), (1,1), (2,1), (3,1)]

**Why**: Storing rotations as coordinate lists makes collision detection simple - just check if each block is valid.

## 3. board.py - Game Board Logic

**Purpose**: Manage the 10×20 game board and block placement.

**Key Methods**:

### `is_valid_position(piece, x, y)`
- Checks if a piece can be placed at position (x, y)
- Validates boundaries (0 ≤ x < 10, 0 ≤ y < 20)
- Checks for collisions with existing blocks
- Returns True if position is valid

### `place_piece(piece, x, y)`
- Marks grid cells as occupied by the piece
- Stores the piece type (shape_type) in each cell
- Called when a piece lands

### `clear_lines()`
- Finds all complete rows (all 10 cells filled)
- Removes complete rows
- Shifts remaining rows down
- Returns count of cleared lines

### `is_game_over()`
- Checks if any blocks exist in the top row
- Game ends when new pieces can't spawn

**Data Structure**:
```python
self.grid = [[None, 'I', 'T', ...],  # Row 0 (top)
             [None, None, 'I', ...],  # Row 1
             ...
             ['O', 'O', 'O', ...]]    # Row 19 (bottom)
```

## 4. game.py - Core Game Logic

**Purpose**: Implement game mechanics and piece management.

### Tetromino Class

**Attributes**:
- `shape_type` - The piece type ('I', 'O', 'T', etc.)
- `rotation` - Current rotation state (0-3)
- `x, y` - Current position on the board

**Methods**:
- `get_blocks()` - Returns block coordinates for current rotation
- `rotate()` - Increment rotation (with wraparound)
- `move_left/right/down()` - Update position
- `reset_position()` - Return to spawn position

### TetrisGame Class

**Attributes**:
- `board` - Board instance
- `current_piece` - Currently falling piece
- `next_piece` - Preview of next piece
- `score` - Current score
- `level` - Current level (1-based)
- `lines_cleared` - Total lines cleared
- `game_over` - Game state flag
- `drop_time` - Accumulator for auto-drop timing

**Key Methods**:

### `update(delta_time)`
- Called every frame with elapsed time
- Accumulates drop_time
- When drop_time ≥ drop_speed, calls soft_drop()
- Implements automatic piece falling

### `soft_drop()`
- Moves piece down by 1 cell
- If collision detected, places piece and spawns new one
- Checks for game over

### `hard_drop()`
- Moves piece down repeatedly until collision
- Instantly places piece at bottom
- Useful for fast gameplay

### `move_left/right/rotate()`
- Attempt to move/rotate piece
- Validate new position
- Undo move if invalid (wall kick prevention)

### `place_current_piece()`
- Marks piece blocks on board
- Checks for game over
- Clears complete lines
- Updates score and level
- Spawns next piece

### `update_score(lines_cleared)`
- Adds points based on lines cleared
- Updates level (every 10 lines)
- Scoring: 1=100, 2=300, 3=500, 4=800

### `get_drop_speed()`
- Calculates speed based on level
- Formula: 0.5 - (level-1) × 0.05
- Minimum speed: 0.1 seconds
- Faster levels = harder difficulty

## 5. utils.py - Rendering

**Purpose**: Handle all graphics and UI rendering.

### Renderer Class

**Initialization**:
- Creates pygame fonts (large, medium, small)
- Stores reference to game screen

**Key Methods**:

### `draw_game(game)`
- Main rendering function called each frame
- Clears screen
- Draws board, current piece, UI
- Handles game over screen

### `draw_board(board)`
- Draws grid lines (dark gray)
- Draws all placed blocks with colors

### `draw_current_piece(piece, board)`
- Draws the falling piece
- Only draws blocks that are visible (y ≥ 0)

### `draw_block(x, y, shape_type)`
- Draws a single block at grid position (x, y)
- Uses color from COLORS dictionary
- Adds border for visual definition

### `draw_border()`
- Draws white border around game area
- Visual boundary for the 10×20 board

### `draw_ui(game)`
- Draws "NEXT" label and next piece preview
- Draws current score
- Draws current level
- Calls draw_game_over() if game is over

### `draw_next_piece(piece)`
- Shows preview of next piece
- Positioned at right side of screen
- Uses same block rendering as main board

### `draw_game_over()`
- Semi-transparent black overlay
- "GAME OVER" text in center
- "Press SPACE to restart" instruction

## 6. main.py - Application Entry Point

**Purpose**: Main game loop and input handling.

### TetrisApp Class

**Initialization**:
- Initializes pygame
- Creates game window (400×500)
- Creates TetrisGame instance
- Creates Renderer instance

**Key Methods**:

### `handle_events()`
- Processes pygame events
- Keyboard input:
  - LEFT/RIGHT - Move piece
  - DOWN - Soft drop
  - UP - Rotate
  - SPACE - Hard drop or restart
- Window close event

### `update()`
- Gets delta_time from clock
- Calls game.update(delta_time)
- Maintains 60 FPS

### `render()`
- Calls renderer.draw_game()
- Updates display with pygame.display.flip()

### `run()`
- Main game loop:
  ```
  while running:
    handle_events()
    update()
    render()
  ```
- Runs until window closed

## 7. test_game.py - Unit Tests

**Purpose**: Verify all game mechanics work correctly.

**Test Functions**:
1. `test_piece_creation()` - Verify pieces spawn correctly
2. `test_piece_rotation()` - Verify rotation changes blocks
3. `test_piece_movement()` - Verify left/right/down movement
4. `test_board_placement()` - Verify pieces place on board
5. `test_line_clearing()` - Verify complete lines are removed
6. `test_game_initialization()` - Verify game starts correctly
7. `test_game_scoring()` - Verify score calculation
8. `test_level_progression()` - Verify level increases
9. `test_game_reset()` - Verify game can be reset

**Run Tests**:
```bash
python test_game.py
```

## Game Flow Diagram

```
START
  ↓
Initialize Game (TetrisGame)
  ├── Create empty board
  ├── Spawn current piece
  └── Spawn next piece
  ↓
MAIN LOOP (60 FPS)
  ├── Handle Input
  │   ├── Move left/right
  │   ├── Rotate
  │   └── Drop (soft/hard)
  ├── Update Game State
  │   ├── Auto-drop piece (based on speed)
  │   ├── Check collision
  │   └── Place piece if landed
  ├── Check Line Clear
  │   ├── Find complete rows
  │   ├── Remove rows
  │   └── Update score/level
  ├── Spawn New Piece
  │   ├── current_piece = next_piece
  │   └── next_piece = random piece
  ├── Check Game Over
  │   └── If blocks at top → GAME OVER
  └── Render
      ├── Draw board
      ├── Draw pieces
      └── Draw UI
  ↓
GAME OVER?
  ├── YES → Show game over screen
  │         Wait for SPACE to restart
  └── NO → Continue loop
```

## Key Design Patterns

### 1. Separation of Concerns
- **config.py**: Configuration
- **shapes.py**: Data definitions
- **board.py**: Board logic
- **game.py**: Game mechanics
- **utils.py**: Rendering
- **main.py**: Application flow

### 2. Model-View-Controller
- **Model**: TetrisGame, Board, Tetromino
- **View**: Renderer
- **Controller**: TetrisApp

### 3. Collision Detection
- Validate position before moving
- Undo move if invalid (no clipping)

### 4. State Management
- Game state centralized in TetrisGame
- Board state in Board.grid
- Piece state in Tetromino

## Performance Optimizations

1. **Fixed-size grid**: No dynamic allocation
2. **Simple collision detection**: Only check 4 blocks
3. **Efficient rendering**: Only redraw changed areas
4. **Clock-based timing**: Stable 60 FPS
5. **No unnecessary object creation**: Reuse pieces

## Common Modifications

### Change Game Speed
Edit `config.py`:
```python
INITIAL_DROP_SPEED = 0.3  # Faster (was 0.5)
```

### Change Board Size
Edit `config.py`:
```python
BOARD_WIDTH = 12  # Wider board
BOARD_HEIGHT = 24  # Taller board
```

### Change Colors
Edit `config.py`:
```python
COLORS = {
    'I': (255, 0, 0),  # Red instead of cyan
    # ...
}
```

### Change Scoring
Edit `config.py`:
```python
SCORE_1_LINE = 200  # More points
```

## Debugging Tips

1. **Print piece position**: Add to game loop
   ```python
   print(f"Piece at ({piece.x}, {piece.y})")
   ```

2. **Print board state**: Add to game loop
   ```python
   for row in game.board.grid:
       print(row)
   ```

3. **Check collision detection**: Add to move_left/right
   ```python
   print(f"Valid position: {board.is_valid_position(...)}")
   ```

4. **Monitor score/level**: Add to update_score
   ```python
   print(f"Score: {self.score}, Level: {self.level}")
   ```

## Conclusion

The Tetris game is built with clean, modular code that separates concerns and makes the codebase easy to understand and modify. Each component has a single responsibility, and the game loop is simple and efficient.

Enjoy playing! 🎮
