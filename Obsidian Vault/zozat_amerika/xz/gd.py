import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
PLAYER_SIZE = 20
OBSTACLE_SIZE = 20
PLAYER_SPEED = 5
OBSTACLE_SPEED = 3

# Set up some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the player
player = pygame.Rect(WIDTH / 2, HEIGHT / 2, PLAYER_SIZE, PLAYER_SIZE)

# Set up the obstacles
obstacles = [pygame.Rect(random.randint(0, WIDTH), random.randint(0, HEIGHT), OBSTACLE_SIZE, OBSTACLE_SIZE) for _ in range(10)]

# Set up the score
score = 0

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        player.y += PLAYER_SPEED
    if keys[pygame.K_LEFT]:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player.x += PLAYER_SPEED

    # Move the obstacles
    for obstacle in obstacles:
        obstacle.x -= OBSTACLE_SPEED
        if obstacle.x < 0:
            obstacle.x = WIDTH
            obstacle.y = random.randint(0, HEIGHT)

    # Check for collisions
    for obstacle in obstacles:
        if player.colliderect(obstacle):
            print("Game Over!")
            pygame.quit()
            sys.exit()

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player)
    for obstacle in obstacles:
        pygame.draw.rect(screen, WHITE, obstacle)
    pygame.display.flip()

    # Update the score
    score += 1
    pygame.display.set_caption(f"Geometry Dash - Score: {score}")

    # Cap the framerate
    pygame.time.delay(1000 // 60)