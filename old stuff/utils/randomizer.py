import random

guest_classes = [
    'Wallflower',
    'Hype Man',
    'Dancer',
    'Disruptor',
    'VIP'
]

def random_guest_class(pool=None):
    """
    Return a random guest class.
    If a pool is provided, use that list instead.
    """
    return random.choice(pool if pool else guest_classes)

def roll_stat(min_val=1, max_val=10):
    """
    Roll a stat between min and max (inclusive).
    """
    return random.randint(min_val, max_val)
