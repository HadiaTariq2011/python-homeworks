import pygame
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rectangle and Text Example")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Font setup
font = pygame.font.SysFont("Arial", 32)

# Rectangle
rect = pygame.Rect(200, 150, 200, 100)

# Game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill background
    screen.fill(WHITE)

    # Draw rectangle
    pygame.draw.rect(screen, BLUE, rect)

    # Render and draw text
    text = font.render("Hello, Pygame!", True, BLACK)
    screen.blit(text, (180, 50))

    # Update display
    pygame.display.flip()
    clock.tick(60)
