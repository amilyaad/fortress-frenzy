import pygame
import random
from tilemap import tile_map_1, tile_types

TILE_SIZE = 16
current_tile_map = tile_map_1

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("enemy.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (1.5 * TILE_SIZE, 1.5 * TILE_SIZE))
        self.rect = self.image.get_rect(topleft=(x, y))

    def find_valid_positions(tile_id):
        valid_positions = []
        for y, row in enumerate(current_tile_map):
            for x, tile_id_ in enumerate(row):
                if tile_id_ == tile_id:
                    valid_positions.append((x * TILE_SIZE, y * TILE_SIZE))
        return valid_positions

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    enemies_start_positions = random.sample(find_valid_positions(5), 5)
    enemies = [Enemy(x, y) for x, y in enemies_start_positions]
    all_sprites.add(*enemies)