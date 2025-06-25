import pygame
import sys
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR, PLAYER_COLOR, PLAYER_SIZE, PLAYER_SPEED

# Pygame Start
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Design Pattern Shooter")
clock = pygame.time.Clock()

# Player
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]

# Main loop
running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keyboard
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos[1] -= PLAYER_SPEED
    if keys[pygame.K_s]:
        player_pos[1] += PLAYER_SPEED
    if keys[pygame.K_a]:
        player_pos[0] -= PLAYER_SPEED
    if keys[pygame.K_d]:
        player_pos[0] += PLAYER_SPEED

    # Draw player
    pygame.draw.rect(screen, PLAYER_COLOR, (player_pos[0], player_pos[1], PLAYER_SIZE, PLAYER_SIZE))

    # Refresh screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
