import pygame
import os
from ..utils.utils import createTexture
from ..globals import ROOT_DIR

pygame.font.init()

# add image resources
textureGamma = createTexture(os.path.join(ROOT_DIR, 'images', 'gamma.png'))
textureTileOutline = createTexture(os.path.join(ROOT_DIR, 'images', 'tile_outline.png'))
textureEmoteBox = createTexture(os.path.join(ROOT_DIR, 'images', 'emote_box.png'))

# add default fonts
fontDefaultSmall = pygame.font.Font(os.path.join(ROOT_DIR, 'fonts', 'munro.ttf'), size=18)
fontDefaultMedium = pygame.font.Font(os.path.join(ROOT_DIR, 'fonts', 'munro.ttf'), size=24)
fontDefaultLarge = pygame.font.Font(os.path.join(ROOT_DIR, 'fonts', 'munro.ttf'), size=60)