class InputComponent:

    def __init__(self,

        # directional buttons
        up=None, down=None, left=None, right=None,
        
        # 18 buttons
        b1=None, b2=None, b3=None, b4=None,
        b5=None, b6=None, b7=None, b8=None,
        b9=None, b10=None, b11=None, b12=None,
        b13=None, b14=None, b15=None, b16=None,
        b17=None, b18=None,
        
        # entity controller
        inputContext=None
    
    ):

        self.key = 'input'

        self.up = up
        self.down = down
        self.left = left
        self.right = right

        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.b6 = b6
        self.b7 = b7
        self.b8 = b8
        self.b9 = b9
        self.b10 = b10
        self.b11 = b11
        self.b12 = b12
        self.b13 = b13
        self.b14 = b14
        self.b15 = b15
        self.b16 = b16
        self.b17 = b17
        self.b18 = b18

        self.inputContext = inputContext
