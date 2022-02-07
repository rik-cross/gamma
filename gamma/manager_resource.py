import pygame

class ResourceManager:
    
    def __init__(self):
        self.images = {}
        self.fonts = {}
        self.sounds = {}
        self.music = {}

    # images

    def addImage(self, key, url):
        self.images[key] = pygame.image.load(url).convert_alpha()

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
    
    # sound and music

    def addSound(self, key, soundURL):
        self.sounds[key] = pygame.mixer.Sound(key)
    
    def getSound(self, key):
        if key not in self.fonts.keys():
            return None
        return self.sound[key]
    
    def addMusic(self, key, url):
        self.music[key] = url
    
    def getMusic(self, key):
        if key not in self.music.keys():
            return None
        return self.music[key]
