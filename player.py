import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("playerright.gif").convert_alpha()
        self.image = pygame.transform.scale(self.image, (24, 24))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.health = 100  # Player's health

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
