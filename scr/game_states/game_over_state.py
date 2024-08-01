import pygame
from .game_state import GameState

class GameOverState(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.font = pygame.font.Font(None, 74)
        self.text = self.font.render('Game Over', True, (255, 0, 0))
        self.text_rect = self.text.get_rect(center=(game.screen.get_width() // 2, game.screen.get_height() // 2))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.game.set_state(self.game.main_menu_state)

    def render(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.text, self.text_rect)
