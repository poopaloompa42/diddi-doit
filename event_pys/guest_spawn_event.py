from ursina import time, Vec3
from random import random
from cube_guest import CubeGuest

spawn_timer = 0
npc_list = None
spawn_position = Vec3(45, 0, -45)  # spawn tile

def set_npc_list_reference(npc_ref):
    global npc_list
    npc_list = npc_ref

def update_guest_spawner():
    global spawn_timer

    if npc_list is None:
        print("No guest list connected to spawn system.")
        return

    spawn_timer += time.dt
    if spawn_timer >= 30:
        spawn_timer = 0

        # === Chance-based VIP logic ===
        is_seed_guest = random() < 0.3  # 30% chance guest is a VIP seed celeb
        new_guest = CubeGuest(is_player=False, is_seed_guest=is_seed_guest)
        new_guest.position = spawn_position
        npc_list.append(new_guest)

        print(f"{'SEED CELEB' if is_seed_guest else 'Normal'} guest arrived!")
