##############################
#readying modules n packages##
##############################

#import
import pygame as pyg
import time
import random
from colors import (
blue,
red,
green,
bright_blue,
black,
white,
bright_green,
bright_red
)
from functions import text_objects,enemy_hits
from enemy_n_player import plyr,plyr_width,enemy
from disp import display_height,display_width,gameDisplay,display
clock = pyg.time.Clock()
pyg.init()
display()
##############################
##############################
#pyg
##############################
###########gameDisplay############
##############################
#defining the gameDisplay width & height along with using them to create a gameDisplay and add a name n icon to it

#gameDisplay

#gameDisplay name

r=bright_blue,black
block_color = (53,115,255)
##############################
##############################
m=time

##############################
######creating a player#######
##############################


##############################
##############################

################################################
###setting the loop "fuel" to keep it running###
################################################	
pause = False
##############################
##############################

##############################
#####setting up stuff =D######
##############################
#counting how many "enemy" we have hits_taken
def enemy_hits(count):
    font = pyg.font.Font("amatic-sc.bold.ttf", 25)
    text = font.render("Dodged: "+str(count), True, blue)
    gameDisplay.blit(text,(0,0))
#making the "thing"s

 
#the objects text are written on


#sets up what happens when u collide with a thing
def collided():
    largeText = pyg.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("You Died!", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while True:
        for event in pyg.event.get():

            if event.type == pyg.QUIT:
                pyg.quit()
                quit()
        button("Play Again",150,450,100,50,green,bright_green,game_loop)
        button("Quit ",550,450,100,50,red,bright_red,quitgame)

        pyg.gameDisplay.update()
        clock.tick(15) 
#setting up buttons
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pyg.mouse.get_pos()
    click = pyg.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pyg.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action()         
    else:
        pyg.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pyg.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
    
#defines a Quit function that if used will stop the game almost instantly
def quitgame():
    pyg.quit()
    quit()
#an unpuaseing function 
def unpause():
    global pause
    pause = False
    
#if the game is supposed to be paused than this function is used ( pause key = p)
def paused():

    largeText = pyg.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    

    while pause:
        for event in pyg.event.get():

            if event.type == pyg.QUIT:
                pyg.quit()
                quit()
                
        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pyg.gameDisplay.update()
        clock.tick(15)   

##############################
##############################

##############################
######## main menu ###########
##############################
def game_intro():

    intro = True

    while intro:
        for event in pyg.event.get():

            if event.type == pyg.QUIT:
                pyg.quit()
                quit()
                
        gameDisplay.fill(white)
        largeText = pyg.font.SysFont("amatic-sc.bold.ttf",50)
        TextSurf, TextRect = text_objects("wanna play dodge ball in minecraft mode?", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!",150,450,100,50,green,bright_green,game_loop)
		
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pyg.display.update()
        clock.tick(15)
##############################
##############################
    
    
############################## 
######### game loop ##########
##############################
    
def game_loop():
    global pause

    x = (display_width * 0.45)
    y = (display_height * 0.8)
 
    x_change = 0
 
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 20
    thing_width = 100
    thing_height = 100
 
    thingCount = 1
 
    hits_taken = 0
 
    gameExit = False
 
    while not gameExit:
 
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                pyg.quit()
                quit()
 
            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_LEFT:
                    x_change = -5
                if event.key == pyg.K_RIGHT:
                    x_change = 5
                if event.key == pyg.K_a:
                    x_change = -5
                if event.key == pyg.K_d:
                    x_change = 5
                if event.key == pyg.K_p:
                    pause = True
                    paused()
                if event.key == pyg.K_PERIOD:
                    enemy(thing_startx, thing_starty, thing_width, thing_height, block_color)
 
            if event.type == pyg.KEYUP:
                if event.key == pyg.K_LEFT or event.key == pyg.K_RIGHT or event.key == pyg.K_a or event.key == pyg.K_d:
                    x_change = 0
 
        x += x_change
        gameDisplay.fill(white)
 
        # enemy(thingx, thingy, thingw, thingh, color)
        enemy(thing_startx, thing_starty, thing_width, thing_height, block_color)
 
 
        
        thing_starty += thing_speed
        plyr(x,y)
        enemy_hits(hits_taken)
        font = pyg.font.Font("amatic-sc.bold.ttf", 25) 
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
		
        pyg.display.update()
        clock.tick(60)
### initiating stuff ###
game_intro()
game_loop()
pyg.quit()
quit()