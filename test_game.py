#!/usr/bin/env python3
# Test script for Tetris game mechanics

from game import TetrisGame, Tetromino
from board import Board
from config import BOARD_WIDTH, BOARD_HEIGHT


def test_piece_creation():
    """Test Tetromino piece creation."""
    print("Testing piece creation...")
    piece = Tetromino('I')
    assert piece.shape_type == 'I'
    assert piece.rotation == 0
    assert piece.x == BOARD_WIDTH // 2 - 1
    assert piece.y == 0
    print("✓ Piece creation works")


def test_piece_rotation():
    """Test piece rotation."""
    print("Testing piece rotation...")
    piece = Tetromino('T')
    initial_blocks = piece.get_blocks()
    piece.rotate()
    rotated_blocks = piece.get_blocks()
    assert initial_blocks != rotated_blocks
    print("✓ Piece rotation works")


def test_piece_movement():
    """Test piece movement."""
    print("Testing piece movement...")
    piece = Tetromino('O')
    initial_x = piece.x
    piece.move_left()
    assert piece.x == initial_x - 1
    piece.move_right()
    piece.move_right()
    assert piece.x == initial_x + 1
    piece.move_down()
    assert piece.y == 1
    print("✓ Piece movement works")


def test_board_placement():
    """Test piece placement on board."""
    print("Testing board placement...")
    board = Board()
    piece = Tetromino('I')
    
    # Check valid position
    assert board.is_valid_position(piece, piece.x, piece.y)
    
    # Place piece
    board.place_piece(piece, piece.x, piece.y)
    
    # Check that blocks are placed
    placed_count = sum(1 for row in board.grid for cell in row if cell is not None)
    assert placed_count == 4  # I piece has 4 blocks
    print("✓ Board placement works")


def test_line_clearing():
    """Test line clearing."""
    print("Testing line clearing...")
    board = Board()
    
    # Fill a line
    for x in range(BOARD_WIDTH):
        board.grid[BOARD_HEIGHT - 1][x] = 'I'
    
    # Clear lines
    lines_cleared = board.clear_lines()
    assert lines_cleared == 1
    
    # Check that line was cleared
    assert all(cell is None for cell in board.grid[BOARD_HEIGHT - 1])
    print("✓ Line clearing works")


def test_game_initialization():
    """Test game initialization."""
    print("Testing game initialization...")
    game = TetrisGame()
    assert game.score == 0
    assert game.level == 1
    assert game.lines_cleared == 0
    assert game.game_over == False
    assert game.current_piece is not None
    assert game.next_piece is not None
    print("✓ Game initialization works")


def test_game_scoring():
    """Test game scoring."""
    print("Testing game scoring...")
    game = TetrisGame()
    
    # Test 1 line
    game.update_score(1)
    assert game.score == 100
    
    # Test 2 lines
    game.update_score(2)
    assert game.score == 100 + 300
    
    # Test 3 lines
    game.update_score(3)
    assert game.score == 100 + 300 + 500
    
    # Test 4 lines (Tetris)
    game.update_score(4)
    assert game.score == 100 + 300 + 500 + 800
    
    print("✓ Game scoring works")


def test_level_progression():
    """Test level progression."""
    print("Testing level progression...")
    game = TetrisGame()
    
    # Clear 10 lines to reach level 2
    for _ in range(10):
        game.update_score(1)
    
    assert game.level == 2
    
    # Clear 10 more lines to reach level 3
    for _ in range(10):
        game.update_score(1)
    
    assert game.level == 3
    print("✓ Level progression works")


def test_game_reset():
    """Test game reset."""
    print("Testing game reset...")
    game = TetrisGame()
    
    # Modify game state
    game.score = 1000
    game.level = 5
    game.game_over = True
    
    # Reset
    game.reset()
    
    assert game.score == 0
    assert game.level == 1
    assert game.game_over == False
    print("✓ Game reset works")


def run_all_tests():
    """Run all tests."""
    print("=" * 50)
    print("Running Tetris Game Tests")
    print("=" * 50)
    
    test_piece_creation()
    test_piece_rotation()
    test_piece_movement()
    test_board_placement()
    test_line_clearing()
    test_game_initialization()
    test_game_scoring()
    test_level_progression()
    test_game_reset()
    
    print("=" * 50)
    print("✓ All tests passed!")
    print("=" * 50)


if __name__ == "__main__":
    run_all_tests()
