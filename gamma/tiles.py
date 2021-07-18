import pygame

class Tile:

    tiles = {}

    @classmethod
    def addTile(cls, tileString, tileImage):
        cls.tiles[tileString] = tileImage

    def __init__(self, image=None, solid=False):
        self.image = image
        self.solid = solid
    
    def draw(self, screen, x, y, w, h):
        if self.image is None:
            return
        screen.blit(pygame.transform.scale(self.image, (w,h)), (x,y))

# add the default empty tile
Tile.addTile('none', Tile())