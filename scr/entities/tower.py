import pygame

class Tower:
    def __init__(self, position):
        self.position = position
        self.range = 100
        self.damage = 10
        self.fire_rate = 1.0
        self.last_shot_time = 0

    def update(self, delta_time, enemies):
        self.last_shot_time += delta_time
        if self.last_shot_time >= self.fire_rate:
            self.shoot(enemies)
            self.last_shot_time = 0

    def shoot(self, enemies):
        # Find the first enemy within range and shoot it
        for enemy in enemies:
            if self.is_in_range(enemy):
                enemy.take_damage(self.damage)
                break

    def is_in_range(self, enemy):
        distance = ((self.position[0] - enemy.position[0]) ** 2 +
                    (self.position[1] - enemy.position[1]) ** 2) ** 0.5
        return distance <= self.range

    def render(self, screen):
        # Draw the tower on the screen
        pygame.draw.circle(screen, (0, 255, 0), self.position, 20)
