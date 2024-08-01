class ActionListener:

    def __init__(self, function, *args):
        self.function = function
        self.args = args
    
    def execute(self):
        if self.function is not None:
            self.function(*self.args)