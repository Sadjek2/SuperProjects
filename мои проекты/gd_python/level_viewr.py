import pygame
import sys

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480

# Classes for Level, Platforms, and Spikes
class Level:
    def __init__(self, platforms, spikes):
        self.platforms = platforms
        self.spikes = spikes

class Platform:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class Spike:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def generate_level():
    platforms = [
        Platform(0, 480 - 20, 9000, 20),  # Ground
        Platform(200, 400, 100, 20), 
         Platform(216, 400, 70, 2000), # Platform 1
        Platform(400, 350, 150, 20),  # Platform 2
        Platform(421, 350, 110, 2000),
        Platform(600, 300, 100, 20),  # Platform 3
        Platform(610, 300, 80, 2000),
    ]
    spikes = [
        Spike(1100, 420),
        Spike(1400, 420),
        Spike(1700, 420),
    ]
    return Level(platforms, spikes)

class Camera:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

def draw_level(level, screen, camera):
    # Draw platforms
    for platform in level.platforms:
        pygame.draw.rect(screen, (0, 255, 0), (platform.x - camera.x, platform.y - camera.y, platform.width, platform.height))
    
    # Draw spikes
    for spike in level.spikes:
        pygame.draw.rect(screen, (255, 0, 0), (spike.x - camera.x, spike.y - camera.y, 30, 30))  # Spikes as red squares

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Level Viewer")

    level = generate_level()
    camera = Camera(0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            camera.move(-5, 0)
        if keys[pygame.K_RIGHT]:
            camera.move(5, 0)
        if keys[pygame.K_UP]:
            camera.move(0, -5)
        if keys[pygame.K_DOWN]:
            camera.move(0, 5)

        screen.fill((0, 0, 0))  # Clear screen with black
        draw_level(level, screen, camera)  # Draw the level
        pygame.display.flip()  # Update the display
        pygame.time.Clock().tick(60)  # Limit to 60 FPS

if __name__ == "__main__":
    main()