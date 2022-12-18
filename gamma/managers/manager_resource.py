import pygame

class ResourceManager:
    
    def __init__(self):
        self.textures = {}
        self.fonts = {}

    # images

    def addTexture(self, key, url):
        self.textures[key] = pygame.image.load(url).convert_alpha()

    def getTexture(self, key):
        if key not in self.textures.keys():
            return None
        return self.textures[key].copy()

    # fonts

    def addFont(self, key, url, size=24):
        self.fonts[key] = pygame.font.Font(url, size)
    
    def getFont(self, key):
        if key not in self.fonts.keys():
            return None
        return self.fonts[key]
