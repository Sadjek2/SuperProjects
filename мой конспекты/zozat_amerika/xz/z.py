import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up the game clock
clock = pygame.time.Clock()

# Define game variables
player_x = 100
player_y = 100
player_speed = 5
player_size = 20
obstacle_size = 20
obstacle_speed = 3
obstacles = []

# Define game functions
def draw_player():
    pygame.draw.rect(screen, (255, 255, 255), (player_x, player_y, player_size, player_size))

def draw_obstacles():
    for obstacle in obstacles:
        pygame.draw.rect(screen, (255, 0, 0), (obstacle[0], obstacle[1], obstacle_size, obstacle_size))

def update_player():
    global player_x, player_y
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

def update_obstacles():
    global obstacles
    for obstacle in obstacles:
        obstacle[0] += obstacle_speed
        if obstacle[0] > screen_width:
            obstacles.remove(obstacle)

def check_collision():
    global player_x, player_y
    for obstacle in obstacles:
        if (player_x + player_size > obstacle[0] and
            player_x < obstacle[0] + obstacle_size and
            player_y + player_size > obstacle[1] and
            player_y < obstacle[1] + obstacle_size):
            return True
    return False

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update player
    update_player()

    # Update obstacles
    update_obstacles()

    # Check collision
    if check_collision():
        print("Game over!")
        break

    # Draw everything
    screen.fill((0, 0, 0))
    draw_player()
    draw_obstacles()
    pygame.display.flip()
    clock.tick(60)

    # Add new obstacles
    if len(obstacles) < 5:
        obstacles.append([screen_width, random.randint(0, screen_height - obstacle_size)])