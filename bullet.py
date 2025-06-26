import pygame
from config import RED_ORANGE, PURPLE, WHITE

class Bullet:
    def __init__(self, x, y, direction, bullet_type):
        self.x = x
        self.y = y
        self.direction = direction  # Vector (dx, dy)
        self.speed = 10
        self.bullet_type = bullet_type
        self.radius = 5

    def update(self):
        self.x += self.direction[0] * self.speed
        self.y += self.direction[1] * self.speed

    def draw(self, screen):
        color = self.get_color()
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius)
    def get_color(self):
        if self.bullet_type.__class__.__name__ == "NormalBullet":
            return WHITE
        elif self.bullet_type.__class__.__name__ == "FireBullet":
            return RED_ORANGE
        elif self.bullet_type.__class__.__name__ == "ElectricBullet":
            return PURPLE
        else:
            return WHITE 