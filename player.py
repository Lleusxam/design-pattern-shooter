import pygame
from config import PLAYER_COLOR, PLAYER_SIZE, PLAYER_SPEED

class Player:
    def __init__(self, x, y):
        
        self.x = x
        self.y = y

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

    def draw(self, screen):
        pygame.draw.rect(screen, PLAYER_COLOR, (self.x, self.y, PLAYER_SIZE, PLAYER_SIZE))
