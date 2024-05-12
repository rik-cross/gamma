import pygame
from random import randint
from ..renderables.image import Image

class Tile:

    def __init__(self,
    
        # optional parameters
        name,
        image=None,
        solid=False,
        editorOnly=False
    
    ):
    
        self.name = name
        self.image = image
        self.solid = solid
        self.editorOnly = editorOnly
    
    # just draws the tile to the surface provided
    def draw(self, scene, x, y, size, alpha=255, editorMode=False):

        # only draw if an image exists
        if self.image is None or (not editorMode and self.editorOnly):
            return

        scene.renderer.add(Image(
            self.image,
            x, y,
            size, size,
            alpha = alpha
        ))

    # renders the map for all entities with a camera
    def render(self, scene, x, y, size, alpha=255, editorMode=False):

        # only draw if an image exists
        if self.image is None or (not editorMode and self.editorOnly):
            return
        
        scene.renderer.add(Image(
            self.image,
            x, y,
            size, size,
            alpha = alpha
        ), scene = False)
