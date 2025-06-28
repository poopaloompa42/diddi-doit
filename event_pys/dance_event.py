# event_pys/dance_event.py
from ursina import *

dance_tile_position = Vec3(45, 0, 45)
dance_ui = None
dance_hype_delta = 0
dance_suspicion_delta = 0

def check_dance_interaction(player):
    global dance_ui
    if distance(player.position, dance_tile_position) < 1.5:
        if not dance_ui:
            dance_ui = create_dance_options()
    else:
        if dance_ui:
            destroy(dance_ui)
            dance_ui = None

def create_dance_options():
    global dance_hype_delta, dance_suspicion_delta
    window_y = window.top_left.y - 0.4
    panel = Entity(parent=camera.ui)

    def twerk():
        global dance_hype_delta, dance_suspicion_delta
        print("You performed the Twerk of Legends!")
        dance_hype_delta += 2
        dance_suspicion_delta += 1
        destroy(panel)

    def moonwalk():
        global dance_hype_delta
        print("You moonwalked like MJ.")
        dance_hype_delta += 1
        destroy(panel)

    def sprinkler():
        global dance_hype_delta, dance_suspicion_delta
        print("You did the sprinkler. Surprisingly charming.")
        dance_hype_delta += 1
        dance_suspicion_delta -= 1
        destroy(panel)

    Button(text='Twerk', position=Vec2(-0.3, window_y), scale=(0.25, 0.05), on_click=twerk, parent=panel)
    Button(text='Moonwalk', position=Vec2(0, window_y), scale=(0.25, 0.05), on_click=moonwalk, parent=panel)
    Button(text='Sprinkler', position=Vec2(0.3, window_y), scale=(0.25, 0.05), on_click=sprinkler, parent=panel)

    return panel

def consume_dance_effects():
    global dance_hype_delta, dance_suspicion_delta
    h, s = dance_hype_delta, dance_suspicion_delta
    dance_hype_delta = 0
    dance_suspicion_delta = 0
    return h, s
