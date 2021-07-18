import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.soundVolume = 1.0
        self.musicVolume = 1.0
        self.targetMusicVolume = 1.0
        self.nextMusic = None
        self.currentMusic = None
        self.sounds = {}
        self.music = {}
    def addSound(self, soundName, soundURL):
        self.sounds[soundName] = pygame.mixer.Sound(soundURL)
    def addMusic(self, musicName, musicURL):
        self.music[musicName] = musicURL
    def playSound(self, soundName, volume=None):
        if volume is None:
            volume = self.soundVolume
        self.sounds[soundName].set_volume(volume)
        self.sounds[soundName].play()
    def playMusic(self, musicName):

        # don't play the music if already playing
        if musicName is self.currentMusic:
            return
        
        pygame.mixer.music.load(self.music[musicName])
        pygame.mixer.music.set_volume(self.musicVolume)
        self.currentMusic = musicName
        pygame.mixer.music.play(-1)
    def playMusicFade(self, musicName):

        # don't play the music if already playing
        if musicName is self.currentMusic:
            return

        # add music to queue
        self.nextMusic = musicName
        # fade out current music
        self.fadeOut()
    def fadeOut(self):
        pygame.mixer.music.fadeout(500)
    def update(self):
        # raise volume if lower than target
        if self.musicVolume < self.targetMusicVolume:
            self.musicVolume = min(self.musicVolume + 0.005, self.targetMusicVolume)
            pygame.mixer.music.set_volume(self.musicVolume)
        # play next music if appropriate
        if self.nextMusic is not None:
            # if 'old' music has finished fading out
            if not pygame.mixer.music.get_busy():
                self.currentMusic = None
                self.musicVolume = 0
                pygame.mixer.music.set_volume(self.musicVolume)
                self.playMusic(self.nextMusic)
                # remove from music queue
                self.nextMusic = None