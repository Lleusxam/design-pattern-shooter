# Bullets
from bullet import Bullet

class BulletType:
    def apply_effect(self):
        pass

class NormalBullet(BulletType):
    def apply_effect(self):
        print("Normal bullet")

class ExplosiveBullet(BulletType):
    def apply_effect(self):
        print("Explosive bullet")

class ElectricBullet(BulletType):
    def apply_effect(self):
        print("Electric bullet")

class FireBullet(BulletType):
    def apply_effect(self):
        print("Fire bullet")

# Gunfire Strategy
class ShootingStrategy:
    def shoot(self, weapon, direction, bullets):
        pass

class SingleShot(ShootingStrategy):
    def shoot(self, weapon, direction, bullets):
        bullets.append(Bullet(weapon.owner.x, weapon.owner.y, direction, weapon.bullet_type))
        weapon.bullet_type.apply_effect()

class MultiShot(ShootingStrategy):
    def shoot(self, weapon, direction, bullets):
        import math
        angles = [-0.2, -0.1, 0.1, 0.2]  # Spread angles
        for angle in angles:
            cos = math.cos(angle)
            sin = math.sin(angle)
            new_dir = (direction[0]*cos - direction[1]*sin, direction[0]*sin + direction[1]*cos)
            bullets.append(Bullet(weapon.owner.x, weapon.owner.y, new_dir, weapon.bullet_type))
            weapon.bullet_type.apply_effect()

class RapidFire(ShootingStrategy):
    def shoot(self, weapon, direction, bullets):
        for _ in range(3):
            bullets.append(Bullet(weapon.owner.x, weapon.owner.y, direction, weapon.bullet_type))
            weapon.bullet_type.apply_effect()

# Weapons
class Weapon:
    def __init__(self, bullet_type, shooting_strategy):
        self.bullet_type = bullet_type
        self.shooting_strategy = shooting_strategy
        self.owner = None

    def shoot(self, direction, bullets):
        self.shooting_strategy.shoot(self, direction, bullets)

    def set_bullet_type(self, bullet_type):
        self.bullet_type = bullet_type

    def set_shooting_strategy(self, shooting_strategy):
        self.shooting_strategy = shooting_strategy

    def set_owner(self, owner):
        self.owner = owner

class Handgun(Weapon):
    def __init__(self, bullet_type):
        super().__init__(bullet_type, SingleShot())
        self.name = "Handgun"
        self.damage = 10

class Shotgun(Weapon):
    def __init__(self, bullet_type):
        super().__init__(bullet_type, MultiShot())
        self.name = "Shotgun"
        self.damage = 8

class MachineGun(Weapon):
    def __init__(self, bullet_type):
        super().__init__(bullet_type, RapidFire())
        self.name = "MachineGun"
        self.damage = 5
