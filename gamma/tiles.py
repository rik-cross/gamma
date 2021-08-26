import pygame
from .image import Image
from .gamma import resourceManager

class Tile:

    tiles = {}

    @classmethod
    def addTile(cls, tileString, tileImage):
        cls.tiles[tileString] = tileImage

    def __init__(self, image=None, solid=False):
        self.image = image
        self.solid = solid
    
    def draw(self, scene, x, y, size):
        if self.image is None:
            return
        scene.renderer.add(Image(
            self.image,
            x, y,
            size, size
        ))

    def drawX(self, screen, x, y, size):
        if self.image is None:
            return
        screen.blit(pygame.transform.scale(self.image, (size,size)), (x,y))

# add the default empty tile
Tile.addTile('none', Tile())