import pygame
from config import BULLET_COLOR

class Bullet:
    def __init__(self, x, y, direction, bullet_type):
        self.x = x
        self.y = y
        self.direction = direction  # Vetor (dx, dy)
        self.speed = 10
        self.bullet_type = bullet_type
        self.radius = 5

    def update(self):
        self.x += self.direction[0] * self.speed
        self.y += self.direction[1] * self.speed

    def draw(self, screen):
        pygame.draw.circle(screen, BULLET_COLOR, (int(self.x), int(self.y)), self.radius)
