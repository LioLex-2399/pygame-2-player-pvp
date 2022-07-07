import pygame as pyg
display_width = 800
display_height = 600
#from disp import display_height,display_width
def display ():	
	pyg.display.set_caption('dodge the ball!!!')
	gameIcon = pyg.image.load('gmicon.png')
	pyg.display.set_icon(gameIcon)
gameDisplay = pyg.display.set_mode((display_width,display_height))