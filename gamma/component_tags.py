from .component import Component

class TagsComponent(Component):

    def __init__(self):
        self.key = 'tags'
        self.tags = []
    
    def add(self, tag, *moreTags):
        for t in [tag] + list(moreTags):
            self.tags.append(t)
    
    def has(self, *tags):
        for t in tags:
            if t not in self.tags:
                return False
        return True