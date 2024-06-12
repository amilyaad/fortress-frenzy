import pygame
import sys
import random
from pygame.locals import QUIT, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_w, K_a, K_s, K_d
from tilemap import tile_map_1, tile_types
from player import Player
from enemy import Enemy
from coin import Coin

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 768, 480
TILE_SIZE = 16
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fortress Frenzy: Duel of Defenders')

tile_images = {}
for tile_id, filename in tile_types.items():
    try:
        tile_images[tile_id] = pygame.image.load(filename).convert()
        tile_images[tile_id] = pygame.transform.scale(tile_images[tile_id], (TILE_SIZE, TILE_SIZE))
    except pygame.error as e:
        print(f"Unable to load image {filename}: {e}")
        sys.exit()

# Load the larger image for the bottom right corner
try:
    larger_image = pygame.image.load('castle.gif').convert()
    larger_image = pygame.transform.scale(larger_image, (180, 180))  # Adjust size as needed
except pygame.error as e:
    print(f"Unable to load larger image: {e}")
    sys.exit()

current_tile_map = tile_map_1
allowed_tile_ids = {5}

def find_valid_positions(tile_id):
    valid_positions = []
    for y, row in enumerate(current_tile_map):
        for x, tile_id_ in enumerate(row):
            if tile_id_ == tile_id:
                valid_positions.append((x * TILE_SIZE, y * TILE_SIZE))
    return valid_positions

# Create player instance
player_start_position = random.choice(find_valid_positions(5))
player = Player(player_start_position[0], player_start_position[1])
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Create multiple enemies
enemies_start_positions = random.sample(find_valid_positions(5), 5)
enemies = [Enemy(x, y) for x, y in enemies_start_positions]
all_sprites.add(*enemies)

# Create coins
coin_positions = random.sample(find_valid_positions(5), 10)
coins = [Coin(x, y) for x, y in coin_positions]
coins_group = pygame.sprite.Group(coins)
all_sprites.add(*coins)

def draw_health_bar(screen, x, y, health):
    BAR_WIDTH = 95
    BAR_HEIGHT = 10
    health_percentage = max(health, 0) / 100
    fill_width = int(BAR_WIDTH * health_percentage)
    fill_rect = pygame.Rect(x, y, fill_width, BAR_HEIGHT)
    pygame.draw.rect(screen, (255, 0, 0), fill_rect)

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player_dx, player_dy = 0, 0
    move_speed = 2  # Set a slower movement speed
    if keys[K_UP]:
        player_dy -= move_speed
    elif keys[K_DOWN]:
        player_dy += move_speed
    elif keys[K_LEFT]:
        player_dx -= move_speed
    elif keys[K_RIGHT]:
        player_dx += move_speed

    next_tile_x = (player.rect.x + player_dx) // TILE_SIZE
    next_tile_y = (player.rect.y + player_dy) // TILE_SIZE
    if current_tile_map[next_tile_y][next_tile_x] in allowed_tile_ids:
        player.move(player_dx, player_dy)

    # Enemy controls
    for enemy in enemies:
        enemy_dx, enemy_dy = 0, 0
        if keys[K_w]:
            enemy_dy -= move_speed
        elif keys[K_s]:
            enemy_dy += move_speed
        elif keys[K_a]:
            enemy_dx -= move_speed
        elif keys[K_d]:
            enemy_dx += move_speed

        next_tile_x = (enemy.rect.x + enemy_dx) // TILE_SIZE
        next_tile_y = (enemy.rect.y + enemy_dy) // TILE_SIZE
        if current_tile_map[next_tile_y][next_tile_x] in allowed_tile_ids:
            enemy.move(enemy_dx, enemy_dy)

    collided_enemies = pygame.sprite.spritecollide(player, enemies, False)
    if collided_enemies:
        player.health -= 1  # Decrease health when the player collides with an enemy

    collided_coins = pygame.sprite.spritecollide(player, coins_group, True)
    if collided_coins:
        player.health = min(player.health + 10, 190)

    # Draw the tile map
    for y, row in enumerate(current_tile_map):
        for x, tile_id in enumerate(row):
            tile_image = tile_images.get(tile_id)
            if tile_image:
                tile_rect = tile_image.get_rect()
                tile_rect.topleft = (x * TILE_SIZE, y * TILE_SIZE)
                screen.blit(tile_image, tile_rect)

    larger_rect = larger_image.get_rect()
    larger_rect.bottomright = (WIDTH, HEIGHT)
    screen.blit(larger_image, (565, 275))

    draw_health_bar(screen, 565, 455, player.health)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)  # Cap the frame rate to 60 FPS

if player.health <= 0:
    print("Game Over! You were defeated.")
    pygame.quit()
    sys.exit()

