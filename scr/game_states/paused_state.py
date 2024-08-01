import logging
import pygame
from .game_state import GameState

class PausedState(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.font = pygame.font.Font(None, 74)
        self.text = self.font.render('Paused', True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(game.screen.get_width() // 2, game.screen.get_height() // 2))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                self.game.set_state(self.game.playing_state)
            elif event.key == pygame.K_q:
                self.game.running = False

    def render(self, screen):
        self.game.playing_state.render(screen)
        screen.blit(self.text, self.text_rect)
