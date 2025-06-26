import random
from characters.base_guest import BaseGuest
from characters.kid_rock import KidRock
from characters.michael import Michael
from utils.randomizer import random_guest_class, roll_stat


SPECIAL_GUESTS = {
    'Michael': Michael,
    'Kid Rock': KidRock,
}


def create_guest(spawn_point=(0, 0, 0)):
    """
    Creates and returns a new guest entity.
    Occasionally returns a special guest.
    """
    # 10% chance for special guest
    if random.random() < 0.1:
        name = random.choice(list(SPECIAL_GUESTS.keys()))
        GuestClass = SPECIAL_GUESTS[name]
        print(f"🌟 Special guest arriving: {name}")
        return GuestClass(position=spawn_point)

    # Otherwise, create a normal guest
    guest_class = random_guest_class()

    return BaseGuest(
        name='Party Guest',
        class_type=guest_class,
        sprite='white_cube',  # TODO: Replace with sprite path logic
        position=spawn_point,
        hype=roll_stat(1, 5),
        suspicion=roll_stat(1, 3)
    )
