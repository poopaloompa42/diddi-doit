from ursina import *
from systems.chat_bubbles import ChatBubble
from utils.colors import random_guest_color

class BaseGuest(Entity):
    def __init__(self, name='Guest', class_type='Generic', sprite=None, guest_color=None, position=(0, 0, 0), **kwargs):
        super().__init__(
            model='quad',
            texture=sprite if sprite else 'white_cube',
            scale=(1, 1.5),
            color=guest_color or random_guest_color(),
            position=position,
            collider='box',
            **kwargs
        )

        self.name = name
        self.class_type = class_type
        self.in_conga_line = False
        self.hype = 0
        self.suspicion = 0

        # Floating name label
        self.name_text = Text(
            text=self.name,
            origin=(0, 0),
            scale=0.75,
            y=1.2,
            parent=self,
            color=color.black  # This now refers safely to the Ursina color module
        )

    def update(self):
        pass

    def speak(self, message, duration=2):
        ChatBubble(message, self, duration=duration)

    def join_conga(self):
        self.in_conga_line = True
        self.speak("I'm in the line!")

    def leave_conga(self):
        self.in_conga_line = False
        self.speak("Later losers.")
