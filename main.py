#!/usr/bin/env python3
# Tetris Game - Main Entry Point

import pygame
import sys
from config import WINDOW_WIDTH, WINDOW_HEIGHT, FPS
from game import TetrisGame
from utils import Renderer


class TetrisApp:
    """Main application class for Tetris game."""
    
    def __init__(self):
        """Initialize the Tetris application."""
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("TETRIS")
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.game = TetrisGame()
        self.renderer = Renderer(self.screen)
    
    def handle_events(self):
        """Handle user input and window events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.game.move_left()
                
                elif event.key == pygame.K_RIGHT:
                    self.game.move_right()
                
                elif event.key == pygame.K_DOWN:
                    self.game.soft_drop()
                
                elif event.key == pygame.K_SPACE:
                    if self.game.game_over:
                        self.game.reset()
                    else:
                        self.game.hard_drop()
                
                elif event.key == pygame.K_UP:
                    self.game.rotate()
    
    def update(self):
        """Update game state."""
        delta_time = self.clock.tick(FPS) / 1000.0
        self.game.update(delta_time)
    
    def render(self):
        """Render the game."""
        self.renderer.draw_game(self.game)
        pygame.display.flip()
    
    def run(self):
        """Main game loop."""
        while self.running:
            self.handle_events()
            self.update()
            self.render()
        
        pygame.quit()
        sys.exit()


def main():
    """Entry point for the Tetris game."""
    app = TetrisApp()
    app.run()


if __name__ == "__main__":
    main()
