import pygame
from .game_state import GameState
from entities.tower import Tower
from entities.enemies import Enemy

class PlayingState(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.towers = []
        self.enemies = []
        self.path = [(100, 100), (200, 100), (200, 200), (300, 200), (300, 300)]
        self.enemies.append(Enemy(self.path, speed=50, health=100))
        self.towers.append(Tower(position=(150, 150)))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            self.towers.append(Tower(position=mouse_pos))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                self.game.set_state(self.game.paused_state)
            elif event.key == pygame.K_q:
                self.game.running = False

    def update(self, delta_time):
        for enemy in self.enemies:
            enemy.update(delta_time)
        for tower in self.towers:
            tower.update(delta_time, self.enemies)
        self.enemies = [enemy for enemy in self.enemies if enemy.is_alive()]

    def render(self, screen):
        screen.fill((0, 0, 0))
        for enemy in self.enemies:
            enemy.render(screen)
        for tower in self.towers:
            tower.render(screen)
