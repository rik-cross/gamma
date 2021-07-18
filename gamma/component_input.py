# TODO -- add other inputs...

class Input:
    def __init__(self, up, down, left, right, b1, b2, inputFunc=None):
        self.key = 'input'
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.b1 = b1
        self.b2 = b2
        self.inputFunc = inputFunc