class ImageGroupsComponent:

    def __init__(self, key=None, imageGroup=None):
        self.key = 'imagegroups'
        self.current = None
        self.animationList = {}
        self.alpha = 255
        self.hue = None
        self.playing = True
        if key is not None and imageGroup is not None:
            self.add(key, imageGroup)
    
    def setHue(self, hue):
        self.hue = hue

    def getCurrentImageGroup(self):
        if self.animationList == {} or self.current is None:
            return None
        return self.animationList[self.current]

    def add(self, state, animation):
        self.animationList[state] = animation
    
    def pause(self):
        self.playing = False

    def play(self):
        self.playing = True

    def stop(self):
        self.playing = False
        if self.current is not None:
            self.animationList[self.current].reset()