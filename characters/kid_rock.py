from characters.base_guest import BaseGuest
from systems.chat_bubbles import ChatBubble
from ursina import color

class KidRock(BaseGuest):
    def __init__(self, position=(0, 0, 0)):
        super().__init__(
            name='Kid Rock',
            class_type='Hype Man',
            guest_color=color.yellow,
            sprite='kid_rock.png',  # Make sure this texture exists in assets
            position=position
        )
        self.spawn_effect()

    def spawn_effect(self):
        ChatBubble("Let's get this party started!", self)
        # TODO: Boost party hype on arrival
