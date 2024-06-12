import pygame 

TILE_SIZE = 16

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("playerright.gif").convert_alpha()
        self.image = pygame.transform.scale(self.image, (1.5 * TILE_SIZE, 1.5 * TILE_SIZE))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.health = 100  # Player's health

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    player_start_position = random.choice(find_valid_positions(5))
    player = Player(player_start_position[0], player_start_position[1])
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)