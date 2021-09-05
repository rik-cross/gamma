from .component import Component

# trauma component is used for screenshake
class TraumaComponent(Component):

    def init(self):
        self.key = 'trauma'
        self._traumaLevel = 0
        self.maxTrauma = 1
        self.traumaDecrement = 0.01
    
    def reset(self):
        self.traumaLevel = 0

    # trauma level property

    @property
    def traumaLevel(self):
        return self._traumaLevel

    # clamps value between 0 and 1
    @traumaLevel.setter
    def traumaLevel(self, value):
        self._traumaLevel = min(1, max(0, value))