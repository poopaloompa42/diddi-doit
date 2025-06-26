from ursina import *
from player import CubeGuest
from camera_control import CameraController

app = Ursina()
window.title = 'Diddi Cube Test'
window.size = (1280, 720)
window.color = color.rgb(200, 220, 255)

background_music = Audio('assets/music/madness-210344.mp3', loop=True, autoplay=True)

# Environment
ground = Entity(
    model='plane',
    scale=100,
    texture='white_cube',
    texture_scale=(100, 100),
    color=color.gray,
    collider='box',
    y=0
)

# Sky Dome
sky = Entity(
    model='sphere',
    scale=200,
    double_sided=True,
    color=color.rgba(200, 220, 255, 90)
)

# Player Setup
player = CubeGuest(is_player=True)
player.y = 5
cam_control = CameraController(target=player)

# FPV Mode Vars
is_fpv = False
fpv_cooldown = 0

# Guests
npc_guests = []
for i in range(10):
    npc = CubeGuest()
    npc.position = Vec3(random.uniform(-8, 8), 5, random.uniform(-8, 8))
    npc_guests.append(npc)

# Mouse rotation vars
yaw = 0
pitch = 0
mouse_sensitivity = 100

def enable_fpv():
    global is_fpv
    camera.parent = player.head
    camera.position = (0, 0.25, 0.5)  # Slight forward for visibility
    camera.rotation = (0, 0, 0)
    mouse.locked = True
    is_fpv = True

def disable_fpv():
    global is_fpv
    camera.parent = None
    camera.position = (0, 15, -25)
    camera.look_at(player)
    mouse.locked = False
    is_fpv = False

disable_fpv()

def update():
    global fpv_cooldown, yaw, pitch

    # Handle FPV toggle
    fpv_cooldown -= time.dt
    if held_keys['f'] and fpv_cooldown <= 0:
        if is_fpv:
            disable_fpv()
        else:
            enable_fpv()
        fpv_cooldown = 0.4  # Cooldown to prevent rapid toggling

    # Handle FPV camera rotation
    if is_fpv:
        yaw += mouse.velocity[0] * mouse_sensitivity
        pitch -= mouse.velocity[1] * mouse_sensitivity
        pitch = clamp(pitch, -90, 90)
        camera.rotation_x = pitch
        player.head.rotation_y = yaw

    # Normal player update
    if not held_keys['shift']:
        player.update()

    for npc in npc_guests:
        npc.update()

app.run()
