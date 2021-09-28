import pygame
from .renderable import Renderable
from .utils_draw import blit_alpha
from .colours import WHITE

class Circle(Renderable):

    def __init__(self,
    
        # required parameters
        x, y, radius,
        
        # optional parameters
        hAlign='left', vAlign='top',
        colour=WHITE,
        alpha=255,
        z=1,
        xParallax=False, yParallax=False

    ):

        super().__init__(x, y, z, hAlign, vAlign, colour, alpha, xParallax, yParallax)
        
        # set additional circle object parameters 
        self._radius = radius
        self._createSurface()
    
    def _createSurface(self):

        self.surface = pygame.Surface((self._radius*2, self._radius*2), pygame.SRCALPHA)
        pygame.draw.circle(self.surface, self.colour, (self._radius, self._radius), self._radius)
        self.rect = self.surface.get_rect()
        self._align()

    def draw(self, surface, xOff=0, yOff=0, scale=1):

        x = int(self.rect.x * scale + xOff)
        y = int(self.rect.y * scale + yOff)
        r = int(self.rect.w * scale)
        scaled_surface = pygame.transform.scale(self.surface, (r, r))
        blit_alpha(surface, scaled_surface, (x, y), self._alpha)

    #  radius property

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        self._radius = value
        self._createSurface()
