import pygame

# TODO -- add anchors for everything

def drawRect(s,x,y,w,h,c,a=255):
    overlay = pygame.Surface((w,h))
    overlay.set_alpha(a)
    overlay.fill(c)
    s.blit(overlay, (x,y))

def drawBox(s,x,y,w,h,c):
    # top
    pygame.draw.line(s,c,(x,y),(x+w,y))
    # bottom
    pygame.draw.line(s,c,(x,y+h),(x+w,y+h))
    # left
    pygame.draw.line(s,c,(x,y),(x,y+h))
    # right
    pygame.draw.line(s,c,(x+w,y),(x+w,y+h))

def drawImage(s, image, x, y, xAnchor='left', yAnchor='top'):
    
    imageRect = image.get_rect()

    if xAnchor == 'center':
        x -= imageRect.w/2
    elif xAnchor == 'right':
        x -= imageRect.w

    if yAnchor == 'middle':
        y -= imageRect.h/2
    elif yAnchor == 'bottom':
        y -= imageRect.h
    
    s.blit(image, (x,y))