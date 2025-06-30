from typing import Tuple, List, TYPE_CHECKING
from bullet import Bullet

if TYPE_CHECKING:
    from player import Player

# Bullet Types
class BulletType:
    def apply_effect(self) -> None:
        pass

class NormalBullet(BulletType):
    def apply_effect(self) -> None:
        print("Normal bullet")

class ExplosiveBullet(BulletType):
    def apply_effect(self) -> None:
        print("Explosive bullet")

class ElectricBullet(BulletType):
    def apply_effect(self) -> None:
        print("Electric bullet")

class FireBullet(BulletType):
    def apply_effect(self) -> None:
        print("Fire bullet")

# Gunfire Strategy
class ShootingStrategy:
    def shoot(self, weapon: "Weapon", direction: Tuple[float, float], bullets: List[Bullet]) -> None:
        pass

class SingleShot(ShootingStrategy):
    def shoot(self, weapon: "Weapon", direction: Tuple[float, float], bullets: List[Bullet]) -> None:
        bullets.append(Bullet(weapon.owner.x, weapon.owner.y, direction, weapon.bullet_type))
        weapon.bullet_type.apply_effect()

class MultiShot(ShootingStrategy):
    def shoot(self, weapon: "Weapon", direction: Tuple[float, float], bullets: List[Bullet]) -> None:
        import math
        angles: List[float] = [-0.2, -0.1, 0.1, 0.2]  # Spread angles
        for angle in angles:
            cos: float = math.cos(angle)
            sin: float = math.sin(angle)
            new_dir: Tuple[float, float] = (
                direction[0] * cos - direction[1] * sin,
                direction[0] * sin + direction[1] * cos
            )
            bullets.append(Bullet(weapon.owner.x, weapon.owner.y, new_dir, weapon.bullet_type))
            weapon.bullet_type.apply_effect()

class RapidFire(ShootingStrategy):
    def shoot(self, weapon: "Weapon", direction: Tuple[float, float], bullets: List[Bullet]) -> None:
        for _ in range(3):
            bullets.append(Bullet(weapon.owner.x, weapon.owner.y, direction, weapon.bullet_type))
            weapon.bullet_type.apply_effect()

# Weapons
class Weapon:
    def __init__(self, bullet_type: BulletType, shooting_strategy: ShootingStrategy):
        self.bullet_type: BulletType = bullet_type
        self.shooting_strategy: ShootingStrategy = shooting_strategy
        self.owner: "Player" | None = None
        self.name: str = "Unnamed"
        self.damage: int = 0

    def shoot(self, direction: Tuple[float, float], bullets: List[Bullet]) -> None:
        self.shooting_strategy.shoot(self, direction, bullets)

    def set_bullet_type(self, bullet_type: BulletType) -> None:
        self.bullet_type = bullet_type

    def set_shooting_strategy(self, shooting_strategy: ShootingStrategy) -> None:
        self.shooting_strategy = shooting_strategy

    def set_owner(self, owner: "Player") -> None:
        self.owner = owner

class Handgun(Weapon):
    def __init__(self, bullet_type: BulletType):
        super().__init__(bullet_type, SingleShot())
        self.name: str = "Handgun"
        self.damage: int = 10

class Shotgun(Weapon):
    def __init__(self, bullet_type: BulletType):
        super().__init__(bullet_type, MultiShot())
        self.name: str = "Shotgun"
        self.damage: int = 8

class MachineGun(Weapon):
    def __init__(self, bullet_type: BulletType):
        super().__init__(bullet_type, RapidFire())
        self.name: str = "MachineGun"
        self.damage: int = 5
