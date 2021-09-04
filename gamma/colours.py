from pygame import color

WHITE      = color.Color(255,255,255)
LIGHT_GREY = color.Color(150,150,150)
MID_GREY   = color.Color(100,100,100)
DARK_GREY  = color.Color(50,50,50)
BLACK      = color.Color(0,0,0)

RED        = color.Color(150,50,50)
GREEN      = color.Color(50,150,50)
BLUE       = color.Color(50,50,150)
YELLOW     = color.Color(150,150,50)

def colour(r, g, b, a=None):
    if a is not None:
        return color.Color(r, g, b)
    else:
        return color.Color(r, g, b, a)
color = colour

def getAlphaColour(colour, alpha):
    return color.Color(
        colour[0],
        colour[1],
        colour[2],
        alpha
    )
getAlphaColor = getAlphaColour
