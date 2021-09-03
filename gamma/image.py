import pygame
from .renderable import Renderable
from .utils_draw import blit_alpha
from math import ceil

class Image(Renderable):

    def __init__(self,
    
        # requried parameters
        image, x, y,
        
        # optional parameters
        w=None, h=None,
        flipX=False, flipY=False,
        alpha=255,
        hAlign='left', vAlign='top',
        colour=None

    ):
        
        super().__init__(x, y, hAlign, vAlign, colour, alpha)

        self.image = image.copy() # do this when getting from the resourceManager
        
        self.flipX = flipX
        self.flipY = flipY

        self._w = w
        self._h = h

        self._createSurface()

    def _createSurface(self):

        self.rect = self.image.get_rect()
        self.rect.x = self._x
        self.rect.y = self._y

        if self._w is not None:
            self.rect.w = self._w
        if self._h is not None:
            self.rect.h = self._h

        self._align()

    def draw(self, surface, xOff=0, yOff=0, scale=1):

        newX = self.rect.x * scale + xOff
        newY = self.rect.y * scale + yOff
        newWidth = ceil(self.rect.w * scale)
        newHeight = ceil(self.rect.h * scale)
        
        blit_alpha(
            surface,
            pygame.transform.scale(
                pygame.transform.flip(
                    self.image, self.flipX, self.flipY
                ), (newWidth, newHeight)
            ),
            (newX, newY),
            self.alpha
        )
