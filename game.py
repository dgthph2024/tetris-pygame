# Tetris Game Logic

import random
from shapes import SHAPES
from config import (
    BOARD_WIDTH, BOARD_HEIGHT,
    SCORE_1_LINE, SCORE_2_LINES, SCORE_3_LINES, SCORE_4_LINES,
    INITIAL_DROP_SPEED, MIN_DROP_SPEED, SPEED_INCREASE_PER_LEVEL
)
from board import Board


class Tetromino:
    """Represents a Tetris piece (Tetromino)."""
    
    def __init__(self, shape_type):
        """
        Initialize a Tetromino piece.
        
        Args:
            shape_type: String representing the shape ('I', 'O', 'T', 'S', 'Z', 'J', 'L')
        """
        self.shape_type = shape_type
        self.rotation = 0
        self.x = BOARD_WIDTH // 2 - 1
        self.y = 0
    
    def get_blocks(self):
        """
        Get the block coordinates of the current rotation state.
        
        Returns:
            List of (x, y) tuples relative to the piece's position
        """
        return SHAPES[self.shape_type][self.rotation]
    
    def rotate(self):
        """Rotate the piece 90 degrees clockwise."""
        self.rotation = (self.rotation + 1) % len(SHAPES[self.shape_type])
    
    def rotate_back(self):
        """Rotate the piece back (undo rotation)."""
        self.rotation = (self.rotation - 1) % len(SHAPES[self.shape_type])
    
    def move_left(self):
        """Move the piece left."""
        self.x -= 1
    
    def move_right(self):
        """Move the piece right."""
        self.x += 1
    
    def move_down(self):
        """Move the piece down."""
        self.y += 1
    
    def reset_position(self):
        """Reset the piece to starting position."""
        self.x = BOARD_WIDTH // 2 - 1
        self.y = 0
        self.rotation = 0


class TetrisGame:
    """Main Tetris game logic."""
    
    def __init__(self):
        """Initialize the Tetris game."""
        self.board = Board()
        self.current_piece = self.create_new_piece()
        self.next_piece = self.create_new_piece()
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.drop_time = 0
        self.game_over = False
        self.drop_speed = INITIAL_DROP_SPEED
    
    def create_new_piece(self):
        """
        Create a new random Tetromino piece.
        
        Returns:
            A new Tetromino object
        """
        shape_types = list(SHAPES.keys())
        return Tetromino(random.choice(shape_types))
    
    def get_drop_speed(self):
        """
        Get the current drop speed based on level.
        
        Returns:
            Drop speed in seconds
        """
        speed = INITIAL_DROP_SPEED - (self.level - 1) * SPEED_INCREASE_PER_LEVEL
        return max(speed, MIN_DROP_SPEED)
    
    def update(self, delta_time):
        """
        Update game state.
        
        Args:
            delta_time: Time elapsed since last update in seconds
        """
        if self.game_over:
            return
        
        self.drop_time += delta_time
        drop_speed = self.get_drop_speed()
        
        if self.drop_time >= drop_speed:
            self.drop_time = 0
            self.soft_drop()
    
    def soft_drop(self):
        """Move the current piece down by one cell."""
        if self.game_over:
            return
        
        self.current_piece.move_down()
        
        if not self.board.is_valid_position(self.current_piece, 
                                           self.current_piece.x, 
                                           self.current_piece.y):
            # Piece can't move down, place it
            self.current_piece.move_down()
            self.current_piece.y -= 1
            self.place_current_piece()
    
    def hard_drop(self):
        """Drop the current piece to the bottom instantly."""
        if self.game_over:
            return
        
        while self.board.is_valid_position(self.current_piece, 
                                          self.current_piece.x, 
                                          self.current_piece.y + 1):
            self.current_piece.move_down()
        
        self.place_current_piece()
    
    def move_left(self):
        """Move the current piece left."""
        if self.game_over:
            return
        
        self.current_piece.move_left()
        
        if not self.board.is_valid_position(self.current_piece, 
                                           self.current_piece.x, 
                                           self.current_piece.y):
            self.current_piece.move_right()
    
    def move_right(self):
        """Move the current piece right."""
        if self.game_over:
            return
        
        self.current_piece.move_right()
        
        if not self.board.is_valid_position(self.current_piece, 
                                           self.current_piece.x, 
                                           self.current_piece.y):
            self.current_piece.move_left()
    
    def rotate(self):
        """Rotate the current piece."""
        if self.game_over:
            return
        
        self.current_piece.rotate()
        
        if not self.board.is_valid_position(self.current_piece, 
                                           self.current_piece.x, 
                                           self.current_piece.y):
            self.current_piece.rotate_back()
    
    def place_current_piece(self):
        """Place the current piece on the board and spawn a new one."""
        self.board.place_piece(self.current_piece, 
                              self.current_piece.x, 
                              self.current_piece.y)
        
        # Check for game over
        if self.board.is_game_over():
            self.game_over = True
            return
        
        # Clear lines and update score
        lines_cleared = self.board.clear_lines()
        self.update_score(lines_cleared)
        
        # Spawn next piece
        self.current_piece = self.next_piece
        self.current_piece.reset_position()
        self.next_piece = self.create_new_piece()
        
        # Check if new piece can be placed
        if not self.board.is_valid_position(self.current_piece, 
                                           self.current_piece.x, 
                                           self.current_piece.y):
            self.game_over = True
    
    def update_score(self, lines_cleared):
        """
        Update the score based on lines cleared.
        
        Args:
            lines_cleared: Number of lines cleared in this action
        """
        if lines_cleared == 0:
            return
        
        score_map = {
            1: SCORE_1_LINE,
            2: SCORE_2_LINES,
            3: SCORE_3_LINES,
            4: SCORE_4_LINES,
        }
        
        self.score += score_map.get(lines_cleared, 0)
        self.lines_cleared += lines_cleared
        
        # Increase level every 10 lines
        self.level = 1 + (self.lines_cleared // 10)
    
    def reset(self):
        """Reset the game to initial state."""
        self.board.reset()
        self.current_piece = self.create_new_piece()
        self.next_piece = self.create_new_piece()
        self.score = 0
        self.level = 1
        self.lines_cleared = 0
        self.drop_time = 0
        self.game_over = False
