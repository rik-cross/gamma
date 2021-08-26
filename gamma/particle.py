from .circle import Circle

class Particle:
    
    def __init__(self, pos, velocity, size, colour):

        self.pos = pos
        self.velocity = velocity
        self.size = size
        self.colour = colour
        self.destroy = False
    
    def update(self):

        # update size
        self.size -= 0.5
        if self.size <= 0:
            self.destroy = True
    
        # update position
        self.pos += self.velocity
    
    def draw(self, scene):
        scene.renderer.add(Circle(
            self.pos.x, self.pos.y, self.size, self.colour, 255
        ))


