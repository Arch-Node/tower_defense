import pygame


class Enemy:
    def __init__(self, path, speed, health):
        self.path = path
        self.speed = speed
        self.health = health
        self.position = self.path[0]
        self.path_index = 0
        self.alive = True

    def update(self, delta_time):
        if not self.alive:
            return

        # Move the enemy along the path
        self.move(delta_time)

        # Check if the enemy has reached the end of the path
        if self.path_index >= len(self.path):
            self.alive = False  # Enemy has reached the end

    def move(self, delta_time):
        if self.path_index >= len(self.path) - 1:
            return

        current_position = pygame.Vector2(self.position)
        target_position = pygame.Vector2(self.path[self.path_index + 1])
        direction = (target_position - current_position).normalize()
        movement = direction * self.speed * delta_time

        if (current_position + movement).distance_to(target_position) < self.speed * delta_time:
            self.position = self.path[self.path_index + 1]
            self.path_index += 1
        else:
            self.position = current_position + movement

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.alive = False

    def render(self, screen):
        if not self.alive:
            return

        # Draw the enemy on the screen
        pygame.draw.circle(screen, (255, 0, 0), (int(self.position[0]), int(self.position[1])), 15)

    def is_alive(self):
        return self.alive
