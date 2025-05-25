from ursina import *
from systems.guest_manager import GuestManager
from systems.event_system import EventSystem
from systems.ui_controller import UIController
from white_box_editor import WhiteBoxEditor

app = Ursina()
window.color = color.black
white_box_editor = WhiteBoxEditor()

# Camera setup
camera.orthographic = True
camera.fov = 20
camera.position = (0, 10, -30)
camera.rotation_x = 30

# Player setup
player = Entity(
    model='cube',
    color=color.orange,
    scale_y=2,
    position=(0, 0, 0)
)

# Game systems
guest_manager = GuestManager()
event_system = EventSystem(guest_manager)
ui = UIController()
def input(key):
    white_box_editor.input(key)


def update():
    # --- Player movement ---
    if held_keys['a']:
        player.x -= 4 * time.dt
    if held_keys['d']:
        player.x += 4 * time.dt

    # --- System updates ---
    guest_manager.update()
    event_system.update()

    # --- UI updates ---
    ui.update_ui(
        guest_count=guest_manager.get_guest_count()
    )

app.run()
