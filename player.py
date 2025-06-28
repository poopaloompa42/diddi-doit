from ursina import *
from cube_guest import CubeGuest

def create_player(pos):
    player = CubeGuest(is_player=True)
    player.position = pos
    mouse.locked = False
    camera.fov = 90
    return player

def update_camera_fpv(player):
    """Attach camera to head without flipping."""
    camera.parent = player.head
    camera.position = (0, 0.25, 0.5)  # Forward-facing
    camera.rotation = (0, 0, 0)
    camera.fov = 90

def update_camera_third_person(player):
    """Smoothly follow player from behind."""
    camera.parent = None
    desired_pos = player.world_position + Vec3(0, 2, -5)
    camera.position = lerp(camera.position, desired_pos, time.dt * 5)
    camera.look_at(player.position + Vec3(0, 1, 0))
    camera.rotation_z = 0
