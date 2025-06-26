from ursina import *  # Ursina Engine import
from PIL import Image

def build_hotel(image_path='assets/other related art/bar_greyscale.png'):
    print(f"Loading hotel layout from {image_path}")
    img = Image.open(image_path).convert('L')  # Grayscale
    pixels = img.load()
    width, height = img.size

    max_width = 100   # Adjust to suit performance
    max_height = 100

    scale_x = width / max_width
    scale_y = height / max_height

    tile_size = 1.0  # Size of each tile in the world

    for y in range(max_height):
        for x in range(max_width):
            px = int(x * scale_x)
            py = int(y * scale_y)
            shade = pixels[px, py]
            world_x = x * tile_size
            world_z = (max_height - y - 1) * tile_size  # Flip vertically for Ursina

            if shade < 40:
                continue

            if shade < 100:
                color_code = color.azure  # DJ Booth
            elif shade < 150:
                color_code = color.red    # Dance floor
            elif shade < 200:
                color_code = color.brown  # Bar/seating
            else:
                color_code = color.white  # Patio/sidewalk

            Entity(
                model='cube',
                scale=(1, 0.1, 1),
                color=color_code,
                position=(world_x, -0.05, world_z),
                collider='box' if shade < 60 else None
            )
