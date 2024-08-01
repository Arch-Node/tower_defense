import pygame
import logging
from .game_state import GameState

class MainMenuState(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.font_large = pygame.font.Font(None, 74)
        self.font_small = pygame.font.Font(None, 36)
        self.title_text = self.font_large.render('Tower Defense', True, (255, 255, 255))
        self.title_rect = self.title_text.get_rect(center=(game.screen.get_width() // 2, game.screen.get_height() // 4))

        self.instructions = [
            "Press ENTER to Start",
            "Press Q to Quit",
            "Press P to Pause/Unpause",
            "Click to Place Towers"
        ]

    def handle_event(self, event):
        logging.debug(f"Event detected: {event}")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.game.set_state(self.game.playing_state)
            elif event.key == pygame.K_q:
                self.game.running = False

    def render(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.title_text, self.title_rect)

        for i, instruction in enumerate(self.instructions):
            instruction_text = self.font_small.render(instruction, True, (255, 255, 255))
            instruction_rect = instruction_text.get_rect(center=(self.game.screen.get_width() // 2, self.game.screen.get_height() // 2 + i * 40))
            screen.blit(instruction_text, instruction_rect)
