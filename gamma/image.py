import pygame
from .renderable import Renderable
from math import ceil

class Image(Renderable):

    def __init__(self, image, x, y, w=None, h=None, flipX=False, flipY=False, alpha=255, hAlign='left', vAlign='top'):
        
        self.image = image.copy()
        self.rect = image.get_rect()

        self.rect.x = x
        self.rect.y = y
        if w is not None:
            self.rect.w = w
        if h is not None:
            self.rect.h = h

        self.flipX = flipX
        self.flipY = flipY

        self.alpha = alpha
        if self.alpha<255:
            self.image.set_alpha(alpha)
        
        # adjust x position for horizontal anchor
        if hAlign == 'center':
            self.rect.centerx = self.rect.x
        if hAlign == 'right':
            self.rect.right = self.rect.x

        # adjust y position for vertical anchor
        if vAlign == 'middle':
            self.rect.centery = self.rect.y
        if vAlign == 'bottom':
            self.rect.bottom = self.rect.y

    def draw(self, surface, xOff=0, yOff=0, scale=1):

        newWidth = ceil(self.rect.w * scale)
        newHeight = ceil(self.rect.h * scale)
        newX = self.rect.x * scale + xOff
        newY = self.rect.y * scale + yOff

        surface.blit(
            pygame.transform.scale(
                pygame.transform.flip(
                    self.image, self.flipX, self.flipY
                ), (newWidth, newHeight)
            ), (newX, newY)
        )
