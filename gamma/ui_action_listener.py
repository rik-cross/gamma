class ActionListener:

    def __init__(self, function):
        self.function = function
    
    def execute(self):
        if self.function is not None:
            self.function()