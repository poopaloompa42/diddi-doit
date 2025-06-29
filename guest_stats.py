import random

class GuestStats:
    def __init__(self):
        # Core stats
        self.entertainment = random.randint(1, 10)  # How fun they are on stage
        self.obedience = random.uniform(0.0, 1.0)   # How likely they are to follow player orders
        self.hype_power = random.randint(0, 3)      # Boost from mic/dance

        # Personality traits
        self.likes_dancing = random.choice([True, False])
        self.likes_mic = random.choice([True, False])
        self.will_wait_in_line = random.choice([True, False])

        # Mood and state
        self.buzzed = False         # From drinks
        self.annoyed = False        # From over-interaction
        self.trust = random.uniform(0.0, 1.0)  # Grows with interactions
