import random
import pyxel

class Tile:
    def __init__(self, x, y, w, h, c, is_active):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c
        self.is_active = is_active
        self.WAITING_TIME = 100
        self.waiting_time = 0
        self.ACTIVE_DURATION = 10
        self.active_duration = self.ACTIVE_DURATION

    def draw(self):
        if self.is_active:
            pyxel.rect(self.x, self.y, self.w, self.h, self.c)
    
    def update(self):
        self.attenuate()
        self.randomize()
        
    def attenuate(self):
        self.waiting_time -= 1

        if self.is_active:
            self.active_duration -= 1

        if self.active_duration <= 0:
            self.is_active = False
            self.active_duration = self.ACTIVE_DURATION  
            self.waiting_time = self.WAITING_TIME

    def randomize(self):
        random_num = random.randint(0, 100)
        if random_num == 0:
            self.is_active = not self.is_active
    
    def contagion(self, object_tile, tile_margin):

        def change_onject_tile_state(object_tile):
            object_tile.is_active = True
            object_tile.c = self.c
        
        if self.is_active and self.active_duration <= self.ACTIVE_DURATION / 2 and self.waiting_time <= 0:
            if self.x == object_tile.x and self.y == object_tile.y:
                pass
            elif self.x == object_tile.x and self.y == object_tile.y + self.h + tile_margin:
                change_onject_tile_state(object_tile)
            elif self.x == object_tile.x and self.y == object_tile.y - self.h - tile_margin:
                change_onject_tile_state(object_tile)
            elif self.x == object_tile.x + self.w + tile_margin and self.y == object_tile.y:
                change_onject_tile_state(object_tile)
            elif self.x == object_tile.x - self.w - tile_margin and self.y == object_tile.y:
                change_onject_tile_state(object_tile)
            elif self.x == object_tile.x + self.w + tile_margin and self.y == object_tile.y + self.h + tile_margin:
                change_onject_tile_state(object_tile)
            elif self.x == object_tile.x - self.w - tile_margin and self.y == object_tile.y - self.h - tile_margin:
                change_onject_tile_state(object_tile)
            elif self.x == object_tile.x + self.w + tile_margin and self.y == object_tile.y - self.h - tile_margin:
                change_onject_tile_state(object_tile)
            elif self.x == object_tile.x - self.w - tile_margin and self.y == object_tile.y + self.h + tile_margin:
                change_onject_tile_state(object_tile)