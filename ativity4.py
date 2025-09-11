import pygame
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Rectangles Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Rectangles
player = pygame.Rect(100, 150, 50, 50)  # Controlled rectangle
enemy = pygame.Rect(400, 150, 50, 50)   # Static rectangle

# Speed
speed = 5

# Game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key controls for player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += speed
    if keys[pygame.K_UP] and player.top > 0:
        player.y -= speed
    if keys[pygame.K_DOWN] and player.bottom < HEIGHT:
        player.y += speed

    # Drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, player)
    pygame.draw.rect(screen, BLUE, enemy)

    # Update screen
    pygame.display.flip()
    clock.tick(60)
