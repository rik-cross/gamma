import pygame

class ResourceManager:
    
    def __init__(self):
        self.images = {}
        self.fonts = {}

    # images

    def addImage(self, key, url):
        self.images[key] = pygame.image.load(url)

    def getImage(self, key):
        if key not in self.images.keys():
            return None
        return self.images[key].copy()

    # fonts

    def addFont(self, key, url, size=24):
        self.fonts[key] = pygame.font.Font(url, size)
    
    def getFont(self, key):
        if key not in self.fonts.keys():
            return None
        return self.fonts[key]
