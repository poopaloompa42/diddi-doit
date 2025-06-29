
from ursina import *
from cube_guest import CubeGuest
from event_pys.fire_event import create_fire_tile

npc_guests = []

def setup_environment():
    Sky(color=color.rgb(200, 220, 255))
    Entity(
    model='cube',
    scale=(100, 1, 100),
    texture='white_cube',
    texture_scale=(100, 100),
    color=color.azure,
    collider='box',
    y=-0.5  # adjust so top of cube is at y=0
   )

    Entity(model='cube', color=color.red, position=Vec3(0, 1, 0), scale=2)
    
    #  Fire tiles
    create_fire_tile(Vec3(2, 0, 2))
    create_fire_tile(Vec3(-3, 0, -1))

    #  Event tiles (dance floor / food zone / future triggers)
    create_event_tiles()

def create_event_tiles():
    tile_specs = [
        (Vec3(45, 0, 45), color.orange, 10),   # 🕺 Big dance floor
        (Vec3(-45, 0, -45), color.pink, 1),    # 🎤 Mic station
        (Vec3(45, 0, -45), color.green, 1),    # 🍹 Bar
        (Vec3(-45, 0, 45), color.yellow, 1),   # 🎧 DJ booth
    ]

    for pos, col, size in tile_specs:
        Entity(
            model='quad',
            texture='white_cube',
            scale=(size, size),
            position=pos + Vec3(0, 0.01, 0),
            rotation_x=90,
            color=col,
            collider='box'
        )


def spawn_guests(count=10, around=Vec3(0, 0, 0), spread=10):
    npc_guests.clear()
    for i in range(count):
        npc = CubeGuest()
        npc.position = around + Vec3(
            random.uniform(-spread, spread), 0, random.uniform(-spread, spread)
        )
        npc_guests.append(npc)
