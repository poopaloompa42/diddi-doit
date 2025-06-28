from ursina import *

fire_tiles = []

def create_fire_tile(position, size=3):
    tile = Entity(
        model='quad',
        color=color.red,
        texture='white_cube',
        scale=(size, size),
        position=position + Vec3(0, 0.01, 0),
        rotation_x=90,
        collider='box'
    )
    fire_tiles.append(tile)
    return tile

def extinguish_fire_tile(tile):
    tile.color = color.azure
    if tile in fire_tiles:
        fire_tiles.remove(tile)

def check_player_extinguish(player):
    for tile in fire_tiles[:]:
        if distance(player.position, tile.position) < 1.5:
            extinguish_fire_tile(tile)
