class ActionListener:
    def __init__(self, f):
        self.action = f
    def execute(self):
        if self.action is not None:
            self.action()