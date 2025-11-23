# Tetris Game Board

from config import BOARD_WIDTH, BOARD_HEIGHT

class Board:
    """Represents the Tetris game board."""
    
    def __init__(self):
        """Initialize an empty board."""
        self.grid = [[None for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
    
    def is_valid_position(self, piece, x, y):
        """
        Check if a piece can be placed at the given position.
        
        Args:
            piece: The Tetromino piece object
            x: X coordinate (column)
            y: Y coordinate (row)
        
        Returns:
            True if the position is valid, False otherwise
        """
        for dx, dy in piece.get_blocks():
            new_x = x + dx
            new_y = y + dy
            
            # Check boundaries
            if new_x < 0 or new_x >= BOARD_WIDTH or new_y >= BOARD_HEIGHT:
                return False
            
            # Check collision with existing blocks
            if new_y >= 0 and self.grid[new_y][new_x] is not None:
                return False
        
        return True
    
    def place_piece(self, piece, x, y):
        """
        Place a piece on the board.
        
        Args:
            piece: The Tetromino piece object
            x: X coordinate (column)
            y: Y coordinate (row)
        """
        for dx, dy in piece.get_blocks():
            new_x = x + dx
            new_y = y + dy
            
            if new_y >= 0:
                self.grid[new_y][new_x] = piece.shape_type
    
    def clear_lines(self):
        """
        Check for and clear complete lines.
        
        Returns:
            Number of lines cleared
        """
        lines_to_clear = []
        
        # Find complete lines
        for y in range(BOARD_HEIGHT):
            if all(self.grid[y][x] is not None for x in range(BOARD_WIDTH)):
                lines_to_clear.append(y)
        
        # Remove complete lines
        for y in sorted(lines_to_clear, reverse=True):
            del self.grid[y]
            self.grid.insert(0, [None for _ in range(BOARD_WIDTH)])
        
        return len(lines_to_clear)
    
    def is_game_over(self):
        """
        Check if the game is over (blocks reached the top).
        
        Returns:
            True if game is over, False otherwise
        """
        for x in range(BOARD_WIDTH):
            if self.grid[0][x] is not None:
                return True
        return False
    
    def reset(self):
        """Reset the board to empty state."""
        self.grid = [[None for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
