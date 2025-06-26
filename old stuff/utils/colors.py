from ursina import color
import random

color_palettes = [
    [color.red, color.orange, color.yellow],
    [color.azure, color.lime, color.green],
    [color.violet, color.magenta, color.pink],
    [color.brown, color.white, color.gray],
    [color.cyan, color.blue, color.red]  # Optional: more variety
]

def random_guest_color(palette=None):
    if palette:
        return random.choice(palette)
    return random.choice(random.choice(color_palettes))
