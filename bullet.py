import pygame
from typing import Tuple, TYPE_CHECKING
from config import RED_ORANGE, PURPLE, DEEP_BLUE, WHITE

if TYPE_CHECKING: # To avoid circular import
    from weapon import BulletType

class Bullet:
    def __init__(self, x: float, y: float, direction: Tuple[float, float], bullet_type: "BulletType"):
        self.x: float = x
        self.y: float = y
        self.direction: Tuple[float, float] = direction  # Vector (dx, dy)
        self.speed: float = 10
        self.bullet_type: "BulletType" = bullet_type
        self.radius: int = 5

    def update(self) -> None:
        self.x += self.direction[0] * self.speed
        self.y += self.direction[1] * self.speed

    def draw(self, screen: pygame.Surface) -> None:
        color: Tuple[int, int, int] = self.get_color()
        pygame.draw.circle(screen, color, (int(self.x), int(self.y)), self.radius)

    def get_color(self) -> Tuple[int, int, int]:
        if self.bullet_type.__class__.__name__ == "NormalBullet":
            return WHITE
        elif self.bullet_type.__class__.__name__ == "FireBullet":
            return RED_ORANGE
        elif self.bullet_type.__class__.__name__ == "ElectricBullet":
            return PURPLE
        elif self.bullet_type.__class__.__name__ == "ExplosiveBullet":
            return DEEP_BLUE
        else:
            return WHITE
