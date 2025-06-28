
from ursina import *

# === UI Elements ===
hype_bar = None
suspicion_bar = None
crowd_counter = None

def setup_ui():
    global hype_bar, suspicion_bar, crowd_counter

    # Hype Bar
    hype_bar = Button(
        text='Hype: 0',
        color=color.lime,
        scale=(0.25, 0.05),
        position=window.top_left + Vec2(0.15, -0.05),
        highlight_color=color.azure,
        tooltip=Tooltip("Total hype from your party!")
    )
    hype_bar.tooltip.background.color = color.black66

    # Suspicion Bar
    suspicion_bar = Button(
        text='Suspicion: 0',
        color=color.red,
        scale=(0.25, 0.05),
        position=window.top_left + Vec2(0.15, -0.12),
        highlight_color=color.orange,
        tooltip=Tooltip("Don't get caught by the cops.")
    )
    suspicion_bar.tooltip.background.color = color.black66

    # Crowd Counter
    crowd_counter = Button(
        text='Guests: 0',
        color=color.violet,
        scale=(0.25, 0.05),
        position=window.top_left + Vec2(0.15, -0.19),
        highlight_color=color.yellow,
        tooltip=Tooltip("Current number of guests at the party.")
    )
    crowd_counter.tooltip.background.color = color.black66


def update_ui(hype_val=0, suspicion_val=0, guest_count=0):
    if hype_bar:
        hype_bar.text = f"Hype: {hype_val}"
    if suspicion_bar:
        suspicion_bar.text = f"Suspicion: {suspicion_val}"
    if crowd_counter:
        crowd_counter.text = f"Guests: {guest_count}"


# === Intro Panel ===
start_panel = None
game_started = False

def show_intro_screen():
    global start_panel, game_started
    start_panel = Entity(parent=camera.ui)

    # Dim background
    background = Entity(parent=start_panel, model='quad', color=color.black66, scale=(1.2, 1.2), z=-1)

    tutorial_text = (
        "SUP BRAD!\n\n"
        "Welcome to the Diddi Doit voxel test.\n\n"
        " Red square = FIRE! Stand on it to put it out.\n"
        " Pink = Mic. Say dumb stuff or hype up the crowd.\n"
        " Blue = Dance Floor. Show off your moves.\n"
        " Yellow = DJ Booth. Drop a track, boost hype.\n"
        " Green = Guest Spawner. New guests arrive here.\n\n"
        "This is a *very early* test – more chaos coming soon!\n"
        "Press F to switch camera modes."
    )

    Text(
        tutorial_text,
        position=(0, 0.25),
        origin=(0, 0),
        scale=1.2,
        parent=start_panel,
        line_height=1.5,
        color=color.green
    )

    def begin():
        global game_started
        game_started = True
        destroy(start_panel)

    Button(
        text='START THE PARTY',
        scale=(0.25, 0.1),
        position=(0, -0.35),
        on_click=begin,
        parent=start_panel
    )


def is_game_started():
    return game_started
