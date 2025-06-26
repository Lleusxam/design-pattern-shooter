import pygame
import math
from config import PLAYER_COLOR, PLAYER_SIZE, PLAYER_SPEED
from weapon import Handgun, Shotgun, MachineGun, NormalBullet
from bullet import Bullet

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        # Weapons setup
        self.weapons = [
            Handgun(NormalBullet()),
            Shotgun(NormalBullet()),
            MachineGun(NormalBullet())
        ]
        self.current_weapon_index = 0
        self.current_weapon = self.weapons[self.current_weapon_index]

        # Set player as owner of weapons
        for weapon in self.weapons:
            weapon.set_owner(self)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= PLAYER_SPEED
        if keys[pygame.K_s]:
            self.y += PLAYER_SPEED
        if keys[pygame.K_a]:
            self.x -= PLAYER_SPEED
        if keys[pygame.K_d]:
            self.x += PLAYER_SPEED

    def handle_event(self, event, bullets):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                self.switch_weapon(0)
            if event.key == pygame.K_2:
                self.switch_weapon(1)
            if event.key == pygame.K_3:
                self.switch_weapon(2)
            if event.key == pygame.K_q:
                self.change_bullet_type("normal")
            if event.key == pygame.K_e:
                self.change_bullet_type("fire")
            if event.key == pygame.K_r:
                self.change_bullet_type("electric")
            if event.key == pygame.K_t:
                self.change_bullet_type("explosive")
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                self.shoot(bullets)

    def switch_weapon(self, index):
        self.current_weapon_index = index
        self.current_weapon = self.weapons[self.current_weapon_index]
        print(f"Current weapon: {self.current_weapon.name}")

    def shoot(self, bullets):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx = mouse_x - self.x
        dy = mouse_y - self.y
        dist = math.hypot(dx, dy)
        if dist == 0:
            dist = 1  # Prevent division by zero
        direction = (dx / dist, dy / dist)
        self.current_weapon.shoot(direction, bullets)
    
    def change_bullet_type(self, bullet_type_name):
        from weapon import NormalBullet, FireBullet, ElectricBullet, ExplosiveBullet

        if bullet_type_name == "normal":
            new_bullet = NormalBullet()
        elif bullet_type_name == "fire":
            new_bullet = FireBullet()
        elif bullet_type_name == "electric":
            new_bullet = ElectricBullet()
        elif bullet_type_name == "explosive":
            new_bullet = ExplosiveBullet()
        else:
            return  # Unknown type

        self.current_weapon.set_bullet_type(new_bullet)
        print(f"Current bullet type: {bullet_type_name.capitalize()}")

    def draw(self, screen):
        pygame.draw.rect(screen, PLAYER_COLOR, (self.x, self.y, PLAYER_SIZE, PLAYER_SIZE))