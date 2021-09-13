import pygame

class SoundManager:

    def __init__(self):

        pygame.mixer.init()
        
        # sound effects
        self.sounds = {}
        self.soundVolume = 1.0

        # music
        self.music = {}
        self.musicVolume = 1.0
        self.targetMusicVolume = 1.0
        self.volumeIncrement = 0.01
        self.nextMusic = None
        self.currentMusic = None

    def addSound(self, soundName, soundURL):
        self.sounds[soundName] = pygame.mixer.Sound(soundURL)
    
    def addMusic(self, musicName, musicURL):
        self.music[musicName] = musicURL
    
    def playSound(self, soundName, volume=None):
        if volume is None:
            volume = self.soundVolume
        self.sounds[soundName].set_volume(volume)
        self.sounds[soundName].play()
    
    def playMusic(self, musicName, loop=True):
        # don't play the music if already playing
        if musicName is self.currentMusic:
            return
        pygame.mixer.music.load(self.music[musicName])
        self.currentMusic = musicName
        if loop:
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.play(0)
    
    def playMusicFade(self, musicName, duration=500):
        # don't play the music if already playing
        if musicName is self.currentMusic:
            return
        # add music to queue
        self.nextMusic = musicName
        # fade out current music
        self.fadeOut(duration)
    
    def setMusicVolume(self, volume, duration=1):
        self.volumeIncrement = 1/duration
        self.targetMusicVolume = volume
    
    def fadeOut(self, duration):
        pygame.mixer.music.fadeout(duration)
    
    def update(self):
        # raise volume if lower than target
        if self.musicVolume < self.targetMusicVolume:
            self.musicVolume = min(self.musicVolume + self.volumeIncrement, self.targetMusicVolume)
            pygame.mixer.music.set_volume(self.musicVolume)
        # lower volume if higher than target
        if self.musicVolume > self.targetMusicVolume:
            self.musicVolume = max(self.musicVolume - self.volumeIncrement, self.targetMusicVolume)
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