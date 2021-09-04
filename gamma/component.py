# base class for all components
class Component:

    def __init__(self):
        self.init()

    def init(self):
        self.key = None

    def reset(self):
        pass