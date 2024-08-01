import pygame
import logging

class GameLoop:
    def __init__(self):
        self.running = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((800, 600))

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
