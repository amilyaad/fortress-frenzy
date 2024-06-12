import pygame

TILE_SIZE = 16

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("coin.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect(topleft=(x, y))

    coin_positions = random.sample(find_valid_positions(5), 10)
    coins = [Coin(x, y) for x, y in coin_positions]
    coins_group = pygame.sprite.Group(coins)
    all_sprites.add(*coins)