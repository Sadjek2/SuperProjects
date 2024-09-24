import pygame
import math

# Инициализация Pygame
pygame.init()

# Установка размеров окна
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# Установка названия окна
pygame.display.set_caption("Doom на Python")

# Установка цвета фона
background_color = (0, 0, 0)

# Установка цвета стен
wall_color = (255, 255, 255)

# Установка размеров игрока
player_size = 20

# Установка начальной позиции игрока
player_x, player_y = width / 2, height / 2

# Установка скорости игрока
player_speed = 5

# Установка угла обзора игрока
player_angle = 0

# Установка расстояния до стены
wall_distance = 100

# Основной цикл игры
while True:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Движение игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_x += player_speed * math.cos(player_angle)
        player_y += player_speed * math.sin(player_angle)
    if keys[pygame.K_s]:
        player_x -= player_speed * math.cos(player_angle)
        player_y -= player_speed * math.sin(player_angle)
    if keys[pygame.K_a]:
        player_angle -= 0.1
    if keys[pygame.K_d]:
        player_angle += 0.1

    # Отрисовка фона
    screen.fill(background_color)

    # Отрисовка стен
    for i in range(360):
        angle = player_angle + math.radians(i)
        distance = wall_distance / math.cos(angle - player_angle)
        x = player_x + distance * math.cos(angle)
        y = player_y + distance * math.sin(angle)
        pygame.draw.line(screen, wall_color, (player_x, player_y), (x, y), 1)

    # Отрисовка игрока
    pygame.draw.rect(screen, (255, 0, 0), (player_x - player_size / 2, player_y - player_size / 2, player_size, player_size))

    # Обновление экрана
    pygame.display.flip()

    # Ограничение скорости игры
    pygame.time.Clock().tick(60)