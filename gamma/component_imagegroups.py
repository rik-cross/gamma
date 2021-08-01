class ImageGroupsComponent:

    def __init__(self):
        self.key = 'imagegroups'
        self.current = None
        self.animationList = {}
        self.alpha = 255
        self.hue = None
    
    def add(self, state, animation):
        self.animationList[state] = animation
        if self.current == None:
            self.current = state