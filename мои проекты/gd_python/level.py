import pygame

class Level:
    def __init__(self, platforms, spikes):
        self.platforms = platforms
        self.spikes = spikes

def generate_level():
    platforms = [
        Platform(0, 480 - 20, 9000, 20),  # Ground
        Platform(200, 400, 100, 20), 
        Platform(216, 400, 70, 2000), # Platform 1
        Platform(460, 350, 150, 20),  # Platform 2
        Platform(481, 350, 110, 2000),
        Platform(760, 300, 100, 20),  # Platform 3
        Platform(770, 300, 80, 2000),
    ]
    spikes = [
        Spike(1100, 420),
        Spike(1400, 420),
        Spike(1700, 420),
        Spike(2200, 420),
        Spike(2200, 390),
    ]
    return Level(platforms, spikes)

class Spike:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Triangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Block:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Platform:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height