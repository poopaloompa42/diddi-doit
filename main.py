
from ursina import *
from ursina import camera, world_position_to_screen_position
from player import create_player, update_camera_third_person
from camera_modes import CameraController
from cube_guest import CubeGuest
from event_pys.fire_event import check_player_extinguish
from world import setup_environment, spawn_guests, create_event_tiles
from ui import setup_ui, update_ui
from event_pys.mic_event import check_mic_interaction, consume_mic_effects
from event_pys.guest_spawn_event import update_guest_spawner, set_npc_list_reference 
from event_pys.dance_event import check_dance_interaction, consume_dance_effects
from event_pys.dj_event import check_dj_interaction, consume_dj_effects
from ui import setup_ui, update_ui, show_intro_screen, is_game_started
from guest_ui import setup_guest_ui, update_guest_ui
from highlight_system import highlight_logic

app = Ursina()
window.title = 'Diddi Doit Voxel Test'

# === Setup environment and player ===
setup_environment()
create_event_tiles()
player_sprite = create_player(Vec3(0, 5, 0))

# === Orbit camera setup ===
orbit_sprite = CubeGuest(is_player=False)
orbit_sprite.position = player_sprite.position + Vec3(2, 0, 0)
orbit_sprite.enabled = False
cam_control = CameraController(target=orbit_sprite)

# === Spawn guests and UI ===
npc_guests = []
spawn_guests(count=0, around=Vec3(0, 5, 0))
set_npc_list_reference(npc_guests)
npc_guests.clear()
setup_ui()
setup_guest_ui()
highlighted_guest = None
clicked_guest = None
show_intro_screen()

# === Camera toggle logic ===
player_mode_enabled = True
toggle_cooldown = 0

# === Game state ===
hype = 10
suspicion = 3

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

# === Main update loop ===
def update():
    global toggle_cooldown, hype, suspicion, highlighted_guest
    global clicked_guest

    if not is_game_started():
        return

    toggle_cooldown -= time.dt
    if held_keys['f'] and toggle_cooldown <= 0:
        switch_camera_mode()
        toggle_cooldown = 0.5

    if cam_control:
        cam_control.update()

    if player_mode_enabled:
        player_sprite.update()
        update_camera_third_person(player_sprite)
        check_player_extinguish(player_sprite)
        check_mic_interaction(player_sprite)
        update_guest_spawner()
        check_dance_interaction(player_sprite)
        check_dj_interaction(player_sprite)
        hype += consume_dj_effects()
        h_dance, s_dance = consume_dance_effects()
        hype += h_dance
        suspicion = max(0, suspicion + s_dance)
        hype_delta, suspicion_delta = consume_mic_effects()
        hype += hype_delta
        suspicion = max(0, suspicion + suspicion_delta)
    else:
        orbit_sprite.update()

    for npc in npc_guests:
        npc.update()

    # === Highlight and Guest UI Logic ===
    highlighted_guest = highlight_logic(npc_guests + [player_sprite])
    update_guest_ui(highlighted_guest)
    
    # === Handle click to open guest UI ===
    if mouse.left and highlighted_guest:
        clicked_guest = highlighted_guest
        show_guest_ui(clicked_guest)

    elif mouse.left and not mouse.hovered_entity:
        clicked_guest = None
        hide_guest_ui()



    update_ui(
        hype_val=hype,
        suspicion_val=suspicion,
        guest_count=len(npc_guests) + 1
    )

app.run()
