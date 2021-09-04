import pygame
from .image import Image

class Tile:

    tiles = {}

    # TODO -- don't need to pass tileString, it's in the object
    @classmethod
    def addTile(cls, tile):
        cls.tiles[tile.name] = tile

    def __init__(self, name=None, image=None, solid=False):
        self.name = name
        self.image = image
        self.solid = solid
    
    def draw(self, scene, x, y, size, alpha=255):
        if self.image is None:
            return
        scene.renderer.add(Image(
            self.image,
            x, y,
            size, size,
            alpha=alpha
        ))

    def drawX(self, screen, x, y, size):
        if self.image is None:
            return
        screen.blit(pygame.transform.scale(self.image, (size,size)), (x,y))

# add the default empty tile
Tile.addTile(Tile('none'))