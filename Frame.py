import random
from Tile import Tile
import pyxel

class Frame:
    def __init__(self, x, y, w, h, c):        
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c

        self.tiles = []
        self.num_vertical_tiles = 30
        self.num_horizontal_tiles = 30

        self.tile_margin = 1
        self.tile_w = int((self.w - (self.num_horizontal_tiles * self.tile_margin)) / self.num_horizontal_tiles)
        self.tile_h = int((self.h - (self.num_vertical_tiles * self.tile_margin)) / self.num_vertical_tiles)

        self.init_tiles()

    def init_tiles(self):
        for i in range(0, self.num_horizontal_tiles):
            for j in range(0, self.num_vertical_tiles):
                rondom_num = random.randint(0, 1)
                
                tile_color = random.randint(0, 15)
                
                is_active = False
                tile = Tile(self.x + (i * (self.tile_w + self.tile_margin)), self.y + (j * (self.tile_h + self.tile_margin)), self.tile_w, self.tile_h, tile_color, is_active)
                self.tiles.append(tile)

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, self.c)

        for tile in self.tiles:
            tile.draw()
    
    def update(self):
        self.contagion(self.tile_margin)
        for tile in self.tiles:
            tile.update()

    def contagion(self, tile_margin):
        for subject_tile in self.tiles:
            for object_tile in self.tiles:
                if subject_tile != object_tile:
                    subject_tile.contagion(object_tile, tile_margin)
