from ursina import *

# UI element placeholders
summary_label = None
guest_ui_panel = None
guest_name_text = None
guest_class_text = None
guest_trait_text = None
converse_button = None
suggest_button = None
kickout_button = None
current_guest = None  # Tracks which guest is being interacted with

def setup_guest_ui():
    global summary_label
    global guest_ui_panel, guest_name_text, guest_class_text, guest_trait_text
    global converse_button, suggest_button, kickout_button

    summary_label = Text(
        text='',
        origin=(0, 0),
        background=True,
        color=color.white,
        enabled=False
    )

    guest_ui_panel = Entity(parent=camera.ui, enabled=False)
    Entity(parent=guest_ui_panel, model='quad', scale=(0.4, 0.3), color=color.black66, z=1)

    guest_name_text = Text("Name: ???", parent=guest_ui_panel, position=(-0.18, 0.1), scale=1.2, origin=(0, 0))
    guest_class_text = Text("Class: ???", parent=guest_ui_panel, position=(-0.18, 0.04), scale=1.2, origin=(0, 0))
    guest_trait_text = Text("Trait: ???", parent=guest_ui_panel, position=(-0.18, -0.02), scale=1.2, origin=(0, 0))

    converse_button = Button(text="Converse", parent=guest_ui_panel, scale=(0.12, 0.05), position=(-0.13, -0.12))
    suggest_button = Button(text="Suggest", parent=guest_ui_panel, scale=(0.12, 0.05), position=(0, -0.12))
    kickout_button = Button(text="Kick Out", parent=guest_ui_panel, scale=(0.12, 0.05), position=(0.13, -0.12))

    converse_button.on_click = lambda: on_converse_clicked(current_guest)

def show_guest_ui(guest):
    global current_guest
    current_guest = guest
    guest_ui_panel.enabled = True
    guest_name_text.text = "Name: ???"
    guest_class_text.text = "Class: ???"
    guest_trait_text.text = "Trait: ???"

def hide_guest_ui():
    global current_guest
    current_guest = None
    guest_ui_panel.enabled = False

def update_guest_ui(highlighted_guest):
    if highlighted_guest:
        screen_pos = camera.world_position_to_screen_position(highlighted_guest.world_position + Vec3(0, 2, 0))
        summary_label.position = screen_pos
        summary_label.enabled = True

        if highlighted_guest.stats.has_been_spoken_to:
            summary_label.text = f'{highlighted_guest.stats.name} ({highlighted_guest.stats.guest_class})'
        else:
            summary_label.text = '???'
    else:
        summary_label.enabled = False

def on_converse_clicked(guest):
    if guest and not guest.stats.has_been_spoken_to:
        guest.stats.has_been_spoken_to = True
    if guest:
        guest_name_text.text = f"Name: {guest.stats.name}"
        guest_class_text.text = f"Class: {guest.stats.guest_class}"
        guest_trait_text.text = f"Trait: {guest.stats.trait}"
