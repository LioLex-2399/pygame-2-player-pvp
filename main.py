##############################
#readying modules n packages##
##############################

#import
import pygame
import time
import random
"""from colors import (
blue,
red,
green,

black,
white,


)"""

#from disp import display_height,display_width,gameDisplay,display
clock = pygame.time.Clock()
pygame.init()
#
display_height=600
display_width=800
gameDisplay = pygame.display.set_mode((display_width, display_height))
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
background_colour=255,255,255
gameDisplay.fill(background_colour)
def mainmenu():
	onplay= True
    
	
	while True:
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


mainmenu()

"""	        if event.type == pygame.KEYDOWN:
	            if event.key == pygame.K_LEFT:
	                x = x - 5
	            if event.key == pygame.K_RIGHT:
	                x = x + 5
	            if event.key == pygame.K_a:
	                x = x - 5
	            if event.key == pygame.K_d:
	                x = x + 5
	            if event.key == pygame.K_SPACE:
	                print("space")
gameDisplay.blit(plyrImg,(x,y))
gameDisplay.blit(plyrImg,(e_x,e_y))
font1 = pygame.font.SysFont('chalkduster.ttf', 72)
img1 = font1.render('health', True, blue)
gameDisplay.blit(img1, (750, 30))
"""






"""
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    
#defines a Quit function that if used will stop the game almost instantly
def quitgame():
    pygame.quit()
    quit()
#an unpuaseing function 
def unpause():
    global pause
    pause = False
    
#if the game is supposed to be paused than this function is used ( pause key = p)  
##############################
##############################

##############################
######## main menu ###########
##############################
""" """  
def game_loop():
    global pause

    x = (display_width * 0.45)
    y = (display_height * 0.8)
 

 
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 20
    thing_width = 100
    thing_height = 100
 
    thingCount = 1
 
    hits_taken = 0
 
    gameExit = False
 
    while not gameExit:
 
    
                
                    
                if event.key == pygame.K_PERIOD:
                    enemy(thing_startx, thing_starty, thing_width, thing_height, block_color)
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
 
        x += x_change
        gameDisplay.fill(white)
 
        # enemy(thingx, thingy, thingw, thingh, color)
        enemy(thing_startx, thing_starty, thing_width, thing_height, block_color)
 
 
        
        thing_starty += thing_speed
        
        enemy_hits(hits_taken)
        font = pygame.font.Font("amatic-sc.bold.ttf", 25) 
#        if x > display_width - plyr_width or x < 0:
        if hits_taken >= 25 and hits_taken <= 50:
	
	        text2 = font.render("you better start taking better care of the castle behind you", True, (0,100,0))
	        gameDisplay.blit(text2,(0,20))
        elif hits_taken >= 50 and hits_taken <= 75:
	        text2 = font.render("your a bad castle keeper =P", True, (255,255,0))
	        gameDisplay.blit(text2,(0,20))
        elif hits_taken >= 75 and hits_taken <= 100:
	        text2 = font.render("your doomed =P", True, (255,165,0))
	        gameDisplay.blit(text2,(0,20))

        elif hits_taken >= 101:
           quit()

		
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            hits_taken += 1
            thing_width += (hits_taken + 1 ) 
		
        pygame.display.update()
        clock.tick(60)
### initiating stuff ###

game_loop()""" 
pygame.quit()
quit()