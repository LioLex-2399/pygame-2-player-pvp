import pygame as pyg
from disp import gameDisplay,display_width,display_height
from colors import black,blue

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pyg.mouse.get_pos()
    click = pyg.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pyg.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pyg.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pyg.font.SysFont("amatic-sc.bold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)