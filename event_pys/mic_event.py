from ursina import *

mic_tile_position = Vec3(-45, 0, -45)
mic_ui = None

# Shared values to be modified by mic choices
hype_delta = 0
suspicion_delta = 0

def check_mic_interaction(player):
    global mic_ui
    if distance(player.position, mic_tile_position) < 1.5:
        if not mic_ui:
            mic_ui = create_mic_options()
    else:
        if mic_ui:
            destroy(mic_ui)
            mic_ui = None

def create_mic_options():
    global hype_delta, suspicion_delta

    window_y = window.top_left.y - 0.3
    panel = Entity(parent=camera.ui)

    def hype_up():
        global hype_delta
        print("You hyped the crowd!")
        hype_delta += 1
        destroy(panel)

    def chant():
        global hype_delta, suspicion_delta
        print("You started a chant!")
        hype_delta += 1
        suspicion_delta += 1
        destroy(panel)

    def say_dumb():
        global suspicion_delta
        print("You said something dumb!")
        suspicion_delta -= 1
        destroy(panel)

    Button(text='Hype up the crowd', position=Vec2(-0.3, window_y), scale=(0.25, 0.05), on_click=hype_up, parent=panel)
    Button(text='Start a chant', position=Vec2(0, window_y), scale=(0.25, 0.05), on_click=chant, parent=panel)
    Button(text='Say something dumb', position=Vec2(0.3, window_y), scale=(0.25, 0.05), on_click=say_dumb, parent=panel)

    return panel

def consume_mic_effects():
    """Returns the accumulated changes to hype/suspicion, then resets them."""
    global hype_delta, suspicion_delta
    h, s = hype_delta, suspicion_delta
    hype_delta = 0
    suspicion_delta = 0
    return h, s
