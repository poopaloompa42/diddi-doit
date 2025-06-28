
from ursina import *
from player import create_player, update_camera_third_person
from camera_modes import CameraController
from cube_guest import CubeGuest
from event_pys.fire_event import create_fire_tile, check_player_extinguish

app = Ursina()
window.title = 'Diddi Doit Voxel Test'

Sky(color=color.rgb(200, 220, 255))

Entity(
    model='plane',
    scale=100,
    texture='white_cube',
    texture_scale=(100, 100),
    color=color.azure,
    collider='box'
)

Entity(model='cube', color=color.red, position=Vec3(0, 1, 0), scale=2)

# === Globals ===
player_mode_enabled = True
toggle_cooldown = 0
npc_guests = []
cam_control = None

# === Create Both Player and Orbit Target Once ===
player_sprite = create_player(Vec3(0, 5, 0))
orbit_sprite = CubeGuest(is_player=False)
orbit_sprite.position = player_sprite.position + Vec3(2, 0, 0)
orbit_sprite.enabled = False
cam_control = CameraController(target=orbit_sprite)

def switch_camera_mode():
    global player_mode_enabled, cam_control

    player_mode_enabled = not player_mode_enabled

    if player_mode_enabled:
        orbit_sprite.enabled = False
        player_sprite.enabled = True
        if cam_control:
            destroy(cam_control)
            cam_control = None
    else:
        player_sprite.enabled = False
        orbit_sprite.enabled = True
        cam_control = CameraController(target=orbit_sprite)

def spawn_guests(count=10, around=Vec3(0, 0, 0), spread=10):
    npc_guests.clear()
    for i in range(count):
        npc = CubeGuest()
        npc.position = around + Vec3(
            random.uniform(-spread, spread), 0, random.uniform(-spread, spread))
        npc_guests.append(npc)

# Start game
spawn_guests(count=10, around=Vec3(0, 5, 0))

def update():
    global toggle_cooldown, cam_control

    toggle_cooldown -= time.dt
    if held_keys['f'] and toggle_cooldown <= 0:
        switch_camera_mode()
        toggle_cooldown = 0.5

    if cam_control:
        cam_control.update()

    if player_mode_enabled:
        player_sprite.update()
        update_camera_third_person(player_sprite)
        check_player_extinguish(player_sprite)  # 🔥 Correct usage here
    else:
        orbit_sprite.update()

    for npc in npc_guests:
        npc.update()


app.run()

