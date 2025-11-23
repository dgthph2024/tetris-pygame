# Tetris Game Utilities (Rendering)

import pygame
from config import (
    WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE,
    BOARD_WIDTH, BOARD_HEIGHT,
    COLOR_BLACK, COLOR_WHITE, COLOR_GRAY, COLOR_DARK_GRAY, COLOR_LIGHT_GRAY,
    COLORS,
    BOARD_OFFSET_X, BOARD_OFFSET_Y,
    NEXT_PIECE_X, NEXT_PIECE_Y,
    SCORE_X, SCORE_Y,
    LEVEL_X, LEVEL_Y,
)


class Renderer:
    """Handles all rendering for the Tetris game."""
    
    def __init__(self, screen):
        """
        Initialize the renderer.
        
        Args:
            screen: Pygame surface to render to
        """
        self.screen = screen
        self.font_large = pygame.font.Font(None, 36)
        self.font_medium = pygame.font.Font(None, 28)
        self.font_small = pygame.font.Font(None, 24)
    
    def draw_game(self, game):
        """
        Draw the entire game state.
        
        Args:
            game: TetrisGame object
        """
        self.screen.fill(COLOR_BLACK)
        
        self.draw_board(game.board)
        self.draw_current_piece(game.current_piece, game.board)
        self.draw_border()
        self.draw_ui(game)
    
    def draw_board(self, board):
        """
        Draw the game board grid.
        
        Args:
            board: Board object
        """
        # Draw grid background
        for y in range(BOARD_HEIGHT):
            for x in range(BOARD_WIDTH):
                rect = pygame.Rect(
                    BOARD_OFFSET_X + x * CELL_SIZE,
                    BOARD_OFFSET_Y + y * CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE
                )
                pygame.draw.rect(self.screen, COLOR_DARK_GRAY, rect, 1)
        
        # Draw placed blocks
        for y in range(BOARD_HEIGHT):
            for x in range(BOARD_WIDTH):
                if board.grid[y][x] is not None:
                    self.draw_block(x, y, board.grid[y][x])
    
    def draw_current_piece(self, piece, board):
        """
        Draw the current falling piece.
        
        Args:
            piece: Tetromino object
            board: Board object (for validation)
        """
        for dx, dy in piece.get_blocks():
            x = piece.x + dx
            y = piece.y + dy
            
            if y >= 0:
                self.draw_block(x, y, piece.shape_type)
    
    def draw_block(self, x, y, shape_type):
        """
        Draw a single block.
        
        Args:
            x: Column position
            y: Row position
            shape_type: Shape type (for color)
        """
        color = COLORS.get(shape_type, COLOR_WHITE)
        rect = pygame.Rect(
            BOARD_OFFSET_X + x * CELL_SIZE + 1,
            BOARD_OFFSET_Y + y * CELL_SIZE + 1,
            CELL_SIZE - 2,
            CELL_SIZE - 2
        )
        pygame.draw.rect(self.screen, color, rect)
        pygame.draw.rect(self.screen, COLOR_LIGHT_GRAY, rect, 1)
    
    def draw_border(self):
        """Draw the border around the game board."""
        border_rect = pygame.Rect(
            BOARD_OFFSET_X - 2,
            BOARD_OFFSET_Y - 2,
            BOARD_WIDTH * CELL_SIZE + 4,
            BOARD_HEIGHT * CELL_SIZE + 4
        )
        pygame.draw.rect(self.screen, COLOR_WHITE, border_rect, 3)
    
    def draw_ui(self, game):
        """
        Draw UI elements (score, level, next piece).
        
        Args:
            game: TetrisGame object
        """
        # Draw "Next Piece" label
        next_label = self.font_medium.render("NEXT", True, COLOR_WHITE)
        self.screen.blit(next_label, (NEXT_PIECE_X, NEXT_PIECE_Y - 30))
        
        # Draw next piece preview
        self.draw_next_piece(game.next_piece)
        
        # Draw score
        score_label = self.font_medium.render("SCORE", True, COLOR_WHITE)
        self.screen.blit(score_label, (SCORE_X, SCORE_Y - 30))
        
        score_text = self.font_small.render(str(game.score), True, COLOR_LIGHT_GRAY)
        self.screen.blit(score_text, (SCORE_X, SCORE_Y))
        
        # Draw level
        level_label = self.font_medium.render("LEVEL", True, COLOR_WHITE)
        self.screen.blit(level_label, (LEVEL_X, LEVEL_Y - 30))
        
        level_text = self.font_small.render(str(game.level), True, COLOR_LIGHT_GRAY)
        self.screen.blit(level_text, (LEVEL_X, LEVEL_Y))
        
        # Draw game over message
        if game.game_over:
            self.draw_game_over()
    
    def draw_next_piece(self, piece):
        """
        Draw the next piece preview.
        
        Args:
            piece: Tetromino object
        """
        preview_x = NEXT_PIECE_X
        preview_y = NEXT_PIECE_Y
        
        for dx, dy in piece.get_blocks():
            x = preview_x + dx * CELL_SIZE
            y = preview_y + dy * CELL_SIZE
            
            color = COLORS.get(piece.shape_type, COLOR_WHITE)
            rect = pygame.Rect(x, y, CELL_SIZE - 2, CELL_SIZE - 2)
            pygame.draw.rect(self.screen, color, rect)
            pygame.draw.rect(self.screen, COLOR_LIGHT_GRAY, rect, 1)
    
    def draw_game_over(self):
        """Draw the game over screen."""
        # Semi-transparent overlay
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(COLOR_BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Game over text
        game_over_text = self.font_large.render("GAME OVER", True, COLOR_WHITE)
        text_rect = game_over_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 30)
        )
        self.screen.blit(game_over_text, text_rect)
        
        # Restart instruction
        restart_text = self.font_small.render("Press SPACE to restart", True, COLOR_LIGHT_GRAY)
        restart_rect = restart_text.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 30)
        )
        self.screen.blit(restart_text, restart_rect)
