from ursina import *

class UIController:
    def __init__(self):
        self.hype = 0
        self.suspicion = 0
        self.guest_count = 0

        # Text elements
        self.hype_text = Text(
            text=f"Hype: {self.hype}",
            position=(-0.5, 0.45),
            scale=2,
            parent=camera.ui,
            color=color.lime
        )

        self.suspicion_text = Text(
            text=f"Suspicion: {self.suspicion}",
            position=(-0.5, 0.4),
            scale=2,
            parent=camera.ui,
            color=color.red
        )

        self.guest_count_text = Text(
            text=f"Guests: {self.guest_count}",
            position=(-0.5, 0.35),
            scale=2,
            parent=camera.ui,
            color=color.white
        )

    def update_ui(self, hype=None, suspicion=None, guest_count=None):
        if hype is not None:
            self.hype = hype
            self.hype_text.text = f"Hype: {self.hype}"

        if suspicion is not None:
            self.suspicion = suspicion
            self.suspicion_text.text = f"Suspicion: {self.suspicion}"

        if guest_count is not None:
            self.guest_count = guest_count
            self.guest_count_text.text = f"Guests: {self.guest_count}"
