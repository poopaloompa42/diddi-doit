from ursina import *
import random

class EventSystem:
    def __init__(self, guest_manager):
        self.timer = 0
        self.interval = 45  # Time between potential doom events
        self.guest_manager = guest_manager

        # Optional: preload event types
        self.event_types = [
            self.fire_event,
            self.police_raid_event,
            self.dance_battle_event
        ]

    def update(self):
        self.timer += time.dt
        if self.timer >= self.interval:
            self.trigger_random_event()
            self.timer = 0

    def trigger_random_event(self):
        if not self.event_types:
            print("No events available.")
            return

        event = random.choice(self.event_types)
        print("⚠️  A chaotic event is happening:", event.__name__)
        event()

    # --------------------
    # Event stubs
    # --------------------

    def fire_event(self):
        print("🔥 Fire breaks out! Guests panic!")
        # Later: mark some guests as fleeing or stunned

    def police_raid_event(self):
        print("🚨 Police raid! Suspicion spikes!")
        # Later: increase suspicion, kick guests out, call bouncers

    def dance_battle_event(self):
        print("🎵 Dance battle time! Guests show off moves!")
        # Later: force player or guests into dance-off mini-event
