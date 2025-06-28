from ursina import *
import math

class CameraController(Entity):
    def __init__(self, target, radius=20, height=8):
        super().__init__()
        self.target = target
        self.radius = radius
        self.height = height
        self.angle = 0
        self.rotation_speed = 60
        self.target_position_offset = Vec3(0, 1.5, 0)

        # NEW: Start from correct position
        self.smooth_pos = self.calculate_desired_position()

    def calculate_desired_position(self):
        radians = math.radians(self.angle)
        offset_x = math.sin(radians) * self.radius
        offset_z = math.cos(radians) * self.radius
        return Vec3(
            self.target.x + offset_x,
            self.target.y + self.height,
            self.target.z + offset_z
        )

    def update(self):
        if not self.target or not self.target.enabled:
            return

        if held_keys['shift'] and held_keys['a']:
            self.angle -= self.rotation_speed * time.dt
        elif held_keys['shift'] and held_keys['d']:
            self.angle += self.rotation_speed * time.dt

        self.angle %= 360
        self.update_camera_position()

    def update_camera_position(self):
        desired_pos = self.calculate_desired_position()
        self.smooth_pos = lerp(self.smooth_pos, desired_pos, time.dt * 5)
        camera.position = self.smooth_pos
        camera.look_at(self.target.position + self.target_position_offset)
        camera.rotation_z = 0
