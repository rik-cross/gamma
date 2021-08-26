class ImageGroupsComponent:

    def __init__(self):
        self.key = 'imagegroups'
        self.current = None
        self.animationList = {}
        self.alpha = 255
        self.hue = None
        self.playing = True
    
    def getCurrentImageGroup(self):
        if self.animationList == {} or self.current is None:
            return None
        return self.animationList[self.current]

    def add(self, state, animation):
        self.animationList[state] = animation
        if self.current == None:
            self.current = state
    
    def pause(self):
        self.playing = False

    def play(self):
        self.playing = True

    def stop(self):
        self.playing = False
        self.animationList[self.current].reset()