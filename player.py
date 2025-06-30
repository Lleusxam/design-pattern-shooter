import pygame
import math
from typing import List, Tuple
from weapon import Weapon, Handgun, Shotgun, MachineGun, NormalBullet, FireBullet, ElectricBullet, ExplosiveBullet
from config import PLAYER_COLOR, PLAYER_SIZE, PLAYER_SPEED
from bullet import Bullet

class Player:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

        # Weapons setup
        self.weapons: List[Weapon] = [
            Handgun(NormalBullet()),
            Shotgun(NormalBullet()),
            MachineGun(NormalBullet())
        ]
        self.current_weapon_index: int = 0
        self.current_weapon: Weapon = self.weapons[self.current_weapon_index]

        # Set player as owner of weapons
        for weapon in self.weapons:
            weapon.set_owner(self)

    def handle_input(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= PLAYER_SPEED
        if keys[pygame.K_s]:
            self.y += PLAYER_SPEED
        if keys[pygame.K_a]:
            self.x -= PLAYER_SPEED
        if keys[pygame.K_d]:
            self.x += PLAYER_SPEED

    def handle_event(self, event: pygame.event.Event, bullets: List[Bullet]) -> None:
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
            if event.button == 1:
                self.shoot(bullets)

    def switch_weapon(self, index: int) -> None:
        self.current_weapon_index = index
        self.current_weapon = self.weapons[self.current_weapon_index]
        print(f"Current weapon: {self.current_weapon.name}")

    def shoot(self, bullets: List[Bullet]) -> None:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        dx: float = mouse_x - self.x
        dy: float = mouse_y - self.y
        dist: float = math.hypot(dx, dy)
        if dist == 0:
            dist = 1  # Prevent division by zero
        direction: Tuple[float, float] = (dx / dist, dy / dist)
        self.current_weapon.shoot(direction, bullets)

    def change_bullet_type(self, bullet_type_name: str) -> None:
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

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, PLAYER_COLOR, (self.x, self.y, PLAYER_SIZE, PLAYER_SIZE))
