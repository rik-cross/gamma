import pygame
from math import ceil
from random import randint
from ..core.renderable import Renderable
from ..utils.utils_draw import blit_alpha

class Image(Renderable):

    def __init__(self,
    
        # requried parameters
        imageSurface, x, y,

        # optional parameters
        w=None, h=None,
        flipX=False, flipY=False,
        angle=0,
        alpha=255,
        hue=None,
        hAlign='left', vAlign='top',
        colour=None,
        z=1,
        xParallax=False, yParallax=False

    ):
        
        super().__init__(x, y, z, hAlign, vAlign, colour, alpha, xParallax, yParallax)

        # set additional image object parameters
        self.imageSurface = imageSurface.copy()

        self.flipX = flipX
        self.flipY = flipY
        self.angle = angle
        self.hue = hue

        if w is not None:
            self._w = w
        else:
            self._w = self.imageSurface.get_rect().w

        if h is not None:
            self._h = h
        else:
            self._h = self.imageSurface.get_rect().h

        self._createSurface()

    def _createSurface(self):

        self.rect = self.imageSurface.get_rect()
        self.rect.x = self._x
        self.rect.y = self._y

        if self._w is not None:
            self.rect.w = self._w
        if self._h is not None:
            self.rect.h = self._h

        if self._alpha < 255:
            self.imageSurface.set_alpha(self._alpha)

        self._align()

    def draw(self, surface, xOff=0, yOff=0, scale=1):

        if self.xp:
            newX = self.rect.x * scale + (xOff*self.z)
        else:
            newX = self.rect.x * scale + xOff
        
        if self.yp:
            newY = self.rect.y * scale + (yOff*self.z)
        else:
            newY = self.rect.y * scale + yOff

        newWidth = ceil(self.rect.w * scale)
        newHeight = ceil(self.rect.h * scale)
        
        if self.hue is not None:
            colourMask = pygame.Surface(self.imageSurface.get_size())
            colourMask.fill(self.hue)
            colouredSurface = self.imageSurface.copy()
            colouredSurface.blit(colourMask, (0,0), special_flags = pygame.BLEND_MULT)
        else:
            colouredSurface = self.imageSurface

        adjustedSurface = pygame.transform.scale(
                pygame.transform.flip(
                    colouredSurface, self.flipX, self.flipY
                ), (newWidth, newHeight)
            )

        rotatedSurface = pygame.transform.rotate(adjustedSurface, self.angle)
        surface.blit(rotatedSurface, (newX, newY))