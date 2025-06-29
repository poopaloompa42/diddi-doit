
from ursina import *
from guest_stats import GuestStats
import math
import random

class CubeGuest(Entity):
    def __init__(self, is_player=False, is_seed_guest=False):
        super().__init__()
        self.collider = 'box'
        self.is_player = is_player
        self.is_seed_guest = is_seed_guest
        self.gravity = 9.8
        self.vertical_velocity = 0
        self.speed = 5
        self.stats = GuestStats()


        # === Visuals ===
        torso_color = color.gold if self.is_seed_guest else color.random_color()
        self.torso = Entity(parent=self, model='cube', scale=(1,1.5,0.5), y=1, color=torso_color)
        self.original_color = torso_color  # <== Store the default torso color
        self.head = Entity(parent=self.torso, model='cube', scale=(1,1,0.5), y=1.5, color=color.random_color())
        self.arm_L = Entity(parent=self.torso, model='cube', scale=(0.3,1,0.3), position=(-0.75,0.25,0), origin_y=0.5, color=color.random_color())
        self.arm_R = Entity(parent=self.torso, model='cube', scale=(0.3,1,0.3), position=(0.75,0.25,0), origin_y=0.5, color=color.random_color())
        self.leg_L = Entity(parent=self, model='cube', scale=(0.4,1,0.4), position=(-0.3,0,0), origin_y=0.5, color=color.random_color())
        self.leg_R = Entity(parent=self, model='cube', scale=(0.4,1,0.4), position=(0.3,0,0), origin_y=0.5, color=color.random_color())

        # === Movement state ===
        self.walk_time = 0
        self.dancing = False
        self.dance_time = 0
        self.idle_timer = random.uniform(0, 2)
        self.stroll_dir = Vec3(random.uniform(-1,1), 0, random.uniform(-1,1)).normalized()

    def set_highlighted(self, state: bool):
        if state:
            self.torso.color = color.white.tint(0.25)
        else:
            self.torso.color = self.original_color

    def update(self):
        # === GRAVITY ===
        ray = raycast(self.world_position + Vec3(0, 0.1, 0), Vec3(0, -1, 0), distance=1.0, ignore=(self,))
        if ray.hit:
            target_y = ray.world_point.y + 0.9
            if abs(self.y - target_y) > 0.01:
                self.y = lerp(self.y, target_y, time.dt * 10)
            self.vertical_velocity = 0
        else:
            self.vertical_velocity -= self.gravity * time.dt
            self.y += self.vertical_velocity * time.dt

        # === POSITION CLAMP ===
        self.x = clamp(self.x, -48, 48)
        self.z = clamp(self.z, -48, 48)

        # === DANCING LOGIC ===
        if self.is_player and held_keys['tab']:
            self.dancing = True
        elif self.is_player:
            self.dancing = False
        elif not self.is_player and random.random() < 0.002:
            self.dancing = not self.dancing

        if self.dancing:
            self.dance_time += time.dt * 10
            self.arm_L.rotation_z = math.sin(self.dance_time) * 45
            self.arm_R.rotation_z = -math.sin(self.dance_time) * 45
            self.leg_L.rotation_x = math.cos(self.dance_time) * 45
            self.leg_R.rotation_x = -math.cos(self.dance_time) * 45
            return

        # === MOVEMENT ===
        move = Vec3(0,0,0)
        if self.is_player:
            move = Vec3(
                held_keys['d'] - held_keys['a'],
                0,
                held_keys['w'] - held_keys['s']
            ).normalized() * self.speed * time.dt

        else:
            self.idle_timer -= time.dt
            if self.idle_timer <= 0:
                self.idle_timer = random.uniform(2, 4)
                self.stroll_dir = Vec3(random.uniform(-1,1), 0, random.uniform(-1,1)).normalized()
            move = self.stroll_dir * self.speed * 0.4 * time.dt

        self.position += move

        if move != Vec3(0,0,0):
            self.look_at(self.position + move)
            self.walk_time += time.dt * 10
            self.arm_L.rotation_z = math.sin(self.walk_time) * 30
            self.arm_R.rotation_z = -math.sin(self.walk_time) * 30
            self.leg_L.rotation_x = math.sin(self.walk_time) * 30
            self.leg_R.rotation_x = -math.sin(self.walk_time) * 30
        else:
            self.arm_L.rotation_z = self.arm_R.rotation_z = 0
            self.leg_L.rotation_x = self.leg_R.rotation_x = 0
