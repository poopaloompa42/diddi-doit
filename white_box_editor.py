from ursina import *
import json
import os

class WhiteBoxEditor(Entity):
    def __init__(self):
        super().__init__()
        self.cube_stacks = []
        self.grid_size = 1
        self.is_active = False

        self.colors = [color.white, color.blue, color.red]  # shoes, pants, shirt
        self.filename = 'data/clubs/editor_test.json'

    def input(self, key):
        if key == 'f1':
            self.is_active = not self.is_active
            print(f"WhiteBox Editor {'enabled' if self.is_active else 'disabled'}")

        if not self.is_active:
            return

        if key == 'left mouse down':
            self.place_stack()

        if key == 'right mouse down':
            self.delete_stack()

        if key == 'f5':
            self.save_level()

        if key == 'f9':
            self.load_level()

    def place_stack(self):
        pos = mouse.world_point
        grid_pos = Vec3(round(pos.x), 0, round(pos.z))

        stack = []
        for i, col in enumerate(self.colors):
            cube = Entity(
                model='cube',
                color=col,
                scale=Vec3(1, 1, 1),
                position=grid_pos + Vec3(0, i, 0)
            )
            stack.append(cube)
        self.cube_stacks.append(stack)

    def delete_stack(self):
        if not self.cube_stacks:
            return

        hit_pos = mouse.world_point
        for stack in self.cube_stacks:
            if distance(stack[0].position, hit_pos) < 1.0:
                for cube in stack:
                    destroy(cube)
                self.cube_stacks.remove(stack)
                break

    def save_level(self):
        data = []
        for stack in self.cube_stacks:
            base = stack[0].position
            data.append({
                'x': int(base.x),
                'z': int(base.z)
            })

        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Level saved to {self.filename}")

    def load_level(self):
        if not os.path.exists(self.filename):
            print("No saved level to load.")
            return

        for stack in self.cube_stacks:
            for cube in stack:
                destroy(cube)
        self.cube_stacks.clear()

        with open(self.filename, 'r') as f:
            data = json.load(f)

        for pos in data:
            grid_pos = Vec3(pos['x'], 0, pos['z'])
            stack = []
            for i, col in enumerate(self.colors):
                cube = Entity(
                    model='cube',
                    color=col,
                    scale=Vec3(1, 1, 1),
                    position=grid_pos + Vec3(0, i, 0)
                )
                stack.append(cube)
            self.cube_stacks.append(stack)
        print(f"Level loaded from {self.filename}")
