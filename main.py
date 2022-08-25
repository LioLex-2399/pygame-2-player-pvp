##############################
#readying modules n packages##
##############################
from plyrmanager import time
#import
import pygame
import time
#import random
from gameDisplay import (
gameDisplay
)
import skins
import winner
#from gameDisplay import (
#gameDisplay
#)

#from disp import display_height,display_width,gameDisplay,display
clock = pygame.time.Clock()
pygame.init()
#

#
blue = 0,0,255
green = 0,255,0
red= 255,0,0
greendull = 0,90,0
reddull = 90,0,0
bluedull = 0,155,0
##############################
##############################
#pygame
##############################
###########gameDisplay############
##############################
#defining the gameDisplay width & height along with using them to create a gameDisplay and add a name n icon to it

#gameDisplay

#gameDisplay name

block_color = (53,115,255)
m=time
##############################
##############################

"""
def text(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
"""
background_colour=0,0,50
gameDisplay.fill(background_colour)
def mainmenu():
	while True:
#		image1 = pygame.image.load("images/menubck.png")
#		gameDisplay.blit(image1, (40, 10))

		for event in pygame.event.get():
			

			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			elif event.type ==pygame.KEYDOWN:
				if event.key == pygame.K_q :
					pygame.quit()
					quit()
					break
				if event.key == pygame.K_s:
					
					skins.SkinGallery()
					break
					
						
					
##########################################
##########################################
		font1 = pygame.font.SysFont('chalkduster.ttf', 72)
		img1 = font1.render('BOSS BATTLE!', True, blue)
		gameDisplay.blit(img1, (200, 300))

		
##########################################
############### play button ##############
		pygame.draw.rect(gameDisplay,green,pygame.Rect(90, 400, 150, 60))
##########################################
##########################################
		font2 = pygame.font.SysFont('chalkduster.ttf', 40)
		img2 = font2.render('start(s)', True, greendull)
		gameDisplay.blit(img2, (125, 410))

		
##########################################
############### quit button ##############

		pygame.draw.rect(gameDisplay,red,pygame.Rect(490, 400, 150, 60))
##########################################
##########################################
		font2 = pygame.font.SysFont('chalkduster.ttf', 50)
		img2 = font2.render('Quit(q)', True, reddull)
		gameDisplay.blit(img2, (525, 410))
##########################################
##########################################
	
		pygame.display.update()
		clock.tick(60)
#skins.SkinGallery()
mainmenu()
plyskin="plyrs/s3.png"
ply1=3
ply2=0
#lvl
#plyrmanage
#winner.win(ply1,ply2)

