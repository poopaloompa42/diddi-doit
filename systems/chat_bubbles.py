from ursina import *

class ChatBubble(Entity):
    def __init__(self, text, parent_entity, duration=2.5):
        super().__init__(parent=parent_entity, y=2.5, z=-0.1)

        self.text_entity = Text(
            text=text,
            parent=self,
            scale=1.5,
            origin=(0, 0),
            color=color.white,
            background=True
        )

        self.timer = duration

    def update(self):
        self.timer -= time.dt
        if self.timer <= 0:
            destroy(self)
