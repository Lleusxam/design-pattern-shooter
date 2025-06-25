import pygame
from config import PLAYER_COLOR, PLAYER_SIZE, PLAYER_SPEED
from weapon import Handgun, Shotgun, MachineGun, NormalBullet

class Player:
    def __init__(self, x, y):
        
        self.x = x
        self.y = y
        
        # Available guns
        self.weapons = [
            Handgun(NormalBullet()),
            Shotgun(NormalBullet()),
            MachineGun(NormalBullet())
        ]
        self.current_weapon_index = 0
        self.current_weapon = self.weapons[self.current_weapon_index]

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
            
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                self.switch_weapon(0)
            if event.key == pygame.K_2:
                self.switch_weapon(1)
            if event.key == pygame.K_3:
                self.switch_weapon(2)
            if event.key == pygame.K_SPACE:
                self.shoot()
    def switch_weapon(self, index):
        self.current_weapon_index = index
        self.current_weapon = self.weapons[self.current_weapon_index]
        print(f"Arma atual: {self.current_weapon.name}")
    def shoot(self):
        print(f"{self.current_weapon.name} disparando...")
        self.current_weapon.shoot()
    
    def draw(self, screen):
        pygame.draw.rect(screen, PLAYER_COLOR, (self.x, self.y, PLAYER_SIZE, PLAYER_SIZE))
