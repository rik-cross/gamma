import pygame

# TODO -- would prefer to pass imageTag instead of surface
# but this gives a circular import (via .gamma systems that use Image)
#from .gamma import resourceManager

from .renderable import Renderable
from .utils_draw import blit_alpha
from math import ceil

class Image(Renderable):

    def __init__(self,
    
        # requried parameters
        imageSurface, x, y,
        
        # optional parameters
        w=None, h=None,
        flipX=False, flipY=False,
        alpha=255,
        hAlign='left', vAlign='top',
        colour=None

    ):
        
        super().__init__(x, y, hAlign, vAlign, colour, alpha)

        # set additional image object parameters
        self.imageSurface = imageSurface.copy()
        self.flipX = flipX
        self.flipY = flipY
        self._w = w
        self._h = h

        self._createSurface()

    def _createSurface(self):

        self.rect = self.imageSurface.get_rect()
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
                    self.imageSurface, self.flipX, self.flipY
                ), (newWidth, newHeight)
            ),
            (newX, newY),
            self.alpha
        )
