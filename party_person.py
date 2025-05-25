from ursina import *
import random
import os

class PartyPerson(Entity):
    def __init__(self, position=(0, 0, 0), base_index=0, **kwargs):
        super().__init__(position=position, **kwargs)
        self.parts = []

        # Load base idle animation
        self.base_frames = [
            f'assets/sprites/base/base{base_index}_idle{i}.png' for i in range(4)
            if os.path.exists(f'assets/sprites/base/base{base_index}_idle{i}.png')
        ]

        if self.base_frames:
            self.base = Animation(self.base_frames, parent=self, scale=2, fps=4, loop=True)
        else:
            self.base = Entity(model='quad', color=color.white, scale=2, parent=self)

        self.parts.append(self.base)

        # Add clothing layers
        self.shirt = self.add_layer('shirt', ['red', 'green', 'hoodie'])
        self.pants = self.add_layer('pants', ['jeans', 'cargos', 'shorts'])
        self.shoes = self.add_layer('shoes', ['white', 'brown', 'yellow'])

    def add_layer(self, category, options):
        choice = random.choice(options)
        texture_path = f'assets/sprites/clothes/{category}_{choice}.png'

        # Only add if texture file exists
        if os.path.exists(texture_path):
            layer = Entity(
                parent=self,
                model='quad',
                texture=texture_path,
                scale=2,
                z=-0.01 * (len(self.parts) + 1)  # offset each layer slightly to avoid z-fighting
            )
            self.parts.append(layer)
            return layer
        return None
