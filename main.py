import pygame
import sys
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR
from player import Player

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Modular Weapons Game")
clock = pygame.time.Clock()

# Player and bullets
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
bullets = []

# Main loop
running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player.handle_event(event, bullets)

    # Update player
    player.handle_input()

    # Update bullets
    for bullet in bullets[:]:
        bullet.update()
        bullet.draw(screen)
        if bullet.x < 0 or bullet.x > SCREEN_WIDTH or bullet.y < 0 or bullet.y > SCREEN_HEIGHT:
            bullets.remove(bullet)

    # Draw player
    player.draw(screen)

    # Refresh screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
