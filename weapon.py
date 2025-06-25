# Bullets
class BulletType:
    def apply_effect(self):
        pass
    
class NormalBullet(BulletType):
    def apply_effect(self):
        print("Normal bullet")
        
class ExplosiveBullet(BulletType):
    def apply_effect(self):
        print("Explosive bullet")
        
class EletroBullet(BulletType):
    def apply_effect(self):
        print("Eletro Bullet")
        
class FireBullet(BulletType):
    def apply_effect(self):
        print("Fire Bullet")

# Gunfire Strategy

class ShootingStrategy:
    def shoot(self, weapon):
        pass
    
class SingleShot(ShootingStrategy):
    def shoot(self, weapon):
        print("Single Shot")
        weapon.bullet_type.apply_effect()
        
class MultiShot(ShootingStrategy):
    def shoot(self, weapon):
        print("Multiple Shot")
        weapon.bullet_type.apply_effect()

class RapidShot(ShootingStrategy):
    def shoot(self, weapon):
        print("Rapid Shot")
        weapon.bullet_type.apply_effect()

# Weapons
class Weapon:
    def __init__(self, bullet_type, shooting_strategy):
        self.bullet_type = bullet_type
        self.shooting_strategy = shooting_strategy
    
    def shoot(self):
        self.shooting_strategy.shoot(self)
        
    def set_bullet_type(self, bullet_type):
        self.bullet_type = bullet_type
    
    def set_shooting_strategy(self, shooting_strategy):
        self.shooting_strategy = shooting_strategy

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
        super().__init__(bullet_type, RapidShot())
        self.name = "MachineGun"
        self.damage = 5