from ursina import *

# Core systems
from systems.guest_manager import GuestManager
from systems.event_system import EventSystem
from systems.ui_controller import UIController
from systems.map_manager import MapManager
from characters.base_guest import BaseGuest

# === Engine Setup ===
app = Ursina()
window.color = color.black
Text.default_font = 'VeraMono.ttf'
background_music = Audio('assets/music/madness-210344.mp3', loop=True, autoplay=True)

# === Map ===
map_manager = MapManager(tile_size=1)
map_manager.load_map()


# === Player + Guests ===
player = BaseGuest(name='Player', position=(0, 0, 0))
player.is_player = True

guests = [
    BaseGuest(name=f'Guest {i}', position=(i * 2, 0, 5)) for i in range(5)
]

# === Camera ===
camera.orthographic = True
camera.fov = 40  # Wider view
camera.position = (player.x, 35, player.z - 35)  # Further and higher
camera.rotation_x = 55

# === Game Systems ===
guest_manager = GuestManager()
event_system = EventSystem(guest_manager)
ui = UIController()

# === Main Game Loop ===
def update():
    speed = 4 * time.dt

    if held_keys['a']:
        player.x -= speed
    if held_keys['d']:
        player.x += speed
    if held_keys['w']:
        player.z += speed
    if held_keys['s']:
        player.z -= speed

    # Camera follow
    camera.position = (player.x, 20, player.z - 20)
    camera.rotation_x = 45

    # Game system updates
    guest_manager.update()
    event_system.update()
    ui.update_ui(guest_count=guest_manager.get_guest_count())

app.run()
