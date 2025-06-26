from ursina import *
import math

class CameraController(Entity):
    def __init__(self, target, radius=20, height=8):
        super().__init__()
        self.target = target
        self.radius = radius
        self.height = height
        self.angle = 0
        self.rotation_speed = 60  # degrees per second

        self.update_camera_position()

    def update(self):
        if held_keys['shift'] and held_keys['a']:
            self.angle -= self.rotation_speed * time.dt
        elif held_keys['shift'] and held_keys['d']:
            self.angle += self.rotation_speed * time.dt

        self.angle %= 360
        self.update_camera_position()

    def update_camera_position(self):
        radians = math.radians(self.angle)
        offset_x = math.sin(radians) * self.radius
        offset_z = math.cos(radians) * self.radius

        # Stable circular orbit on XZ plane
        camera.position = Vec3(
            self.target.x + offset_x,
            self.target.y + self.height,
            self.target.z + offset_z
        )

        # Look at player, but force camera roll (z-rotation) to zero
        camera.look_at(self.target.position + Vec3(0, 1.5, 0))
        camera.rotation_z = 0  # force horizon level
