from ursina import *
from systems.guest_factory import create_guest
import random


class GuestManager:
    def __init__(self, spawn_delay=30):
        self.spawn_delay = spawn_delay
        self.timer = 0
        self.guest_list = []

    def update(self):
        self.timer += time.dt
        if self.timer >= self.spawn_delay:
            self.spawn_guest()
            self.timer = 0

    def spawn_guest(self):
        spawn_x = random.uniform(-5, 5)
        spawn_point = (spawn_x, 0, 0)
        guest = create_guest(spawn_point=spawn_point)
        self.guest_list.append(guest)

    def get_guest_count(self):
        return len(self.guest_list)
