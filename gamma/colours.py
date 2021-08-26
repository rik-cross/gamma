from pygame import color

WHITE      = color.Color(255,255,255)
LIGHT_GREY = color.Color(150,150,150)
DARK_GREY  = color.Color(50,50,50)
BLACK      = color.Color(0,0,0)

RED        = color.Color(150,50,50)
GREEN      = color.Color(50,150,50)
BLUE       = color.Color(50,50,150)

def getAlphaColour(colour, alpha):
    r = colour[0]
    g = colour[1]
    b = colour[2]
    a = alpha
    return color.Color(r,g,b,a)
