import pygame

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("coin.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.rect = self.image.get_rect(topleft=(x, y))
