from characters.base_guest import BaseGuest
from systems.chat_bubbles import ChatBubble
from ursina import color

class Michael(BaseGuest):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            name='Michael',
            class_type='Performer',
            guest_color=color.azure,
            sprite='michael.png',  # Add this if using character-specific texture
            position=position
        )
        self.triggers_thriller = True  # Flag to trigger the special event
        self.spawn_effect()

    def spawn_effect(self):
        ChatBubble("You know it's Thriller night...", self)
        # TODO: Trigger Thriller dance event
