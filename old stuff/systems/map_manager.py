from ursina import *
from pytmx import TiledMap
import os

class MapManager:
    def __init__(self, tile_size=1):
        self.tile_size = tile_size
        self.current_map = []
        self.object_data = {}

        self.map_path = os.path.join(
            'assets', 'building and terrain parts', 'tiled projects', 'uglyhotel.tmx'
        )

    def load_map(self):
        if not os.path.exists(self.map_path):
            print(f"[MapManager] Map file not found: {self.map_path}")
            return

        print(f"[MapManager] Loading: {self.map_path}")
        tmx_data = TiledMap(self.map_path)

        # Load the tileset texture (assumes one combined image)
        tileset = tmx_data.tilesets[0]
        tileset_image_path = os.path.join(
            os.path.dirname(self.map_path),
            tileset.source.replace('.tsx', '.png')
        )
        full_texture = load_texture(tileset_image_path)

        tile_width = tmx_data.tilewidth
        tile_height = tmx_data.tileheight
        columns = full_texture.width // tile_width

        for layer in tmx_data.visible_layers:
            if hasattr(layer, 'data'):
                for x, y, gid in layer:
                    if gid == 0:
                        continue

                    tile_id = gid - tileset.firstgid
                    u = (tile_id % columns) * tile_width / full_texture.width
                    v = (tile_id // columns) * tile_height / full_texture.height

                    tile_uvs = [
                        Vec2(u, v),
                        Vec2(u + tile_width / full_texture.width, v),
                        Vec2(u + tile_width / full_texture.width, v + tile_height / full_texture.height),
                        Vec2(u, v + tile_height / full_texture.height),
                    ]

                    entity = Entity(
                        model=Mesh(
                            vertices=[
                                Vec3(-0.5, -0.5, 0), Vec3(0.5, -0.5, 0),
                                Vec3(0.5, 0.5, 0), Vec3(-0.5, 0.5, 0)
                            ],
                            triangles=[(0, 1, 2), (0, 2, 3)],
                            uvs=tile_uvs,
                            mode='triangle'
                        ),
                        texture=full_texture,
                        position=(x * self.tile_size, -y * self.tile_size, 0),
                        scale=(self.tile_size, self.tile_size),
                        collider=None
                    )

                    self.current_map.append(entity)

        # Object layer parsing
        for obj in tmx_data.objects:
            name = obj.name
            ox = obj.x / tile_width
            oy = -obj.y / tile_height + 1
            self.object_data[name] = Vec3(ox, 0, oy)
            print(f"[MapManager] Found object: {name} at {ox:.2f}, {oy:.2f}")

    def clear_map(self):
        for e in self.current_map:
            destroy(e)
        self.current_map = []
