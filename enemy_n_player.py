import pygame
from disp import gameDisplay
plyr_width = 73
plyrImg = pygame.image.load('plyr_icon.png')
def plyr(x,y):
    gameDisplay.blit(plyrImg,(x,y))
def enemy(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
