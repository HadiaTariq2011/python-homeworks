import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rectangle and Text Example")

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Font for text
font = pygame.font.SysFont("Arial", 36)

# Rectangle (x, y, width, height)
rect = pygame.Rect(200, 150, 200, 100)

# Text surface
text_surface = font.render("Hello Pygame!", True, BLACK)

# Game loop
running = True
while running:
    screen.fill(WHITE)  # Clear the screen

    # Draw rectangle
    pygame.draw.rect(screen, BLUE, rect)

    # Draw text
    screen.blit(text_surface, (180, 50))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()  # Refresh display

# Quit pygame
pygame.quit()
