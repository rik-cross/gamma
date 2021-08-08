import pygame
from .component_input import InputComponent
from .manager_input import controller, keys

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

def drawImage(s, image, x, y, xAnchor='left', yAnchor='top', scale=1):
    
    imageRect = image.get_rect()
    ow = imageRect.w
    oh = imageRect.h

    if xAnchor == 'center':
        x -= imageRect.w*scale/2
    elif xAnchor == 'right':
        x -= imageRect.w*scale

    if yAnchor == 'middle':
        y -= imageRect.h*scale/2
    elif yAnchor == 'bottom':
        y -= imageRect.h*scale
    
    s.blit(pygame.transform.scale(image, (ow*scale,oh*scale)), (x,y))

def createControllerInputComponent(controllerNumber, entityControllerFunction):

    controllerInputComponent = InputComponent(
        up=     controller[controllerNumber].dpad_up,
        down=   controller[controllerNumber].dpad_down,
        left=   controller[controllerNumber].dpad_left,
        right=  controller[controllerNumber].dpad_right,
        b1=     controller[controllerNumber].a,
        b2=     controller[controllerNumber].b,

        b3=     controller[controllerNumber].x,
        b4=     controller[controllerNumber].y,

        b9=     controller[controllerNumber].leftShoulder,
        b10=    controller[controllerNumber].rightShoulder,
        b11=    controller[controllerNumber].leftTrigger,
        b12=    controller[controllerNumber].rightTrigger,
        b13=    controller[controllerNumber].rightDir_up,
        b14=    controller[controllerNumber].rightDir_down,
        b15=    controller[controllerNumber].rightDir_left,
        b16=    controller[controllerNumber].rightDir_right,
        inputFunc= entityControllerFunction
    )

    return controllerInputComponent

def createKeyboardInputComponent(entityControllerFunction):

    keyboardInputComponent = InputComponent(
        up=keys.up,
        down=keys.down,
        left=keys.left,
        right=keys.right,
        b1=keys.enter,
        b2=keys.esc,
        inputFunc=entityControllerFunction
    )

    return keyboardInputComponent