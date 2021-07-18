import pygame

class ResourceManager:
    
    def __init__(self):
        self.images = {}
        self.fonts = {}

    # images

    def addImage(self, tag, url):
        self.images[tag] = pygame.image.load(url)

    def getImage(self, tag):
        if tag not in self.images.keys():
            return None
        return self.images[tag]

    # fonts

    def addFont(self, tag, url, size=24):
        self.fonts[tag] = pygame.font.Font(url, size)
    
    def getFont(self, tag):
        if tag not in self.fonts.keys():
            return None
        return self.fonts[tag]
