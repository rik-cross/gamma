class ImageGroups:

    def __init__(self):
        self.key = 'imagegroups'
        self.animationList = {}
        self.alpha = 255
        self.hue = None
    
    def add(self, state, animation):
        self.animationList[state] = animation
        #don't use 'state' -- instead store 'current', which initially can be in step with the key