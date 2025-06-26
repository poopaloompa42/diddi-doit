from ursina import *
from systems.chat_bubbles import ChatBubble
from utils.colors import random_guest_color
import random

class BaseGuest(Entity):
    def __init__(self, name='Guest', class_type='Generic', sprite=None, guest_color=None, position=(0, 0, 0), **kwargs):
        super().__init__(position=position, collider='box', **kwargs)

        self.name = name
        self.class_type = class_type
        self.in_conga_line = False
        self.hype = 0
        self.suspicion = 0

        # Player AI control toggles
        self.is_player = False
        self.manual_override = False
        self.inactivity_timer = 0

        # Movement attributes
        self.wander_timer = random.uniform(1, 3)
        self.wander_direction = Vec3(0, 0, 0)

        # Stack pieces
        self.pants = Entity(parent=self, model='cube', color=guest_color or random_guest_color(), scale=(1, 0.33, 1), y=0)
        self.shirt = Entity(parent=self, model='cube', color=random_guest_color(), scale=(1, 0.33, 1), y=0.33)
        self.hat = Entity(parent=self, model='cube', color=random_guest_color(), scale=(1, 0.33, 1), y=0.66)

        if sprite:
            self.face = Entity(parent=self, model='quad', texture=sprite, scale=(0.9, 0.9), y=0.33, z=-0.51)

        self.name_text = Text(text=self.name, origin=(0, 0), scale=0.75, y=1.2, parent=self, color=color.black)

    def update(self):
        if self.is_player:
            input_active = held_keys['w'] or held_keys['a'] or held_keys['s'] or held_keys['d']

            if input_active:
                self.manual_override = True
                self.inactivity_timer = 0

                speed = 4 * time.dt
                if held_keys['w']: self.z += speed
                if held_keys['s']: self.z -= speed
                if held_keys['a']: self.x -= speed
                if held_keys['d']: self.x += speed
            else:
                self.inactivity_timer += time.dt
                if self.inactivity_timer > 5:
                    self.manual_override = False

        # AI movement
        if not self.manual_override and not self.in_conga_line:
            self.wander_timer -= time.dt
            if self.wander_timer <= 0:
                dx = random.choice([-1, 0, 1])
                dz = random.choice([-1, 0, 1])
                self.wander_direction = Vec3(dx, 0, dz).normalized() * 2
                self.wander_timer = random.uniform(1, 3)

            self.position += self.wander_direction * time.dt

    def speak(self, message, duration=2):
        ChatBubble(message, self, duration=duration)

    def join_conga(self):
        self.in_conga_line = True
        self.speak("I'm in the line!")

    def leave_conga(self):
        self.in_conga_line = False
        self.speak("Later losers.")
