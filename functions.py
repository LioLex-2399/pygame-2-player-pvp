import pygame as pyg
from disp import gameDisplay,display_width,display_height
from colors import black,blue

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


	
def enemy_hits(count):
  font = pyg.font.Font("amatic-sc.bold.ttf", 25)
  text = font.render("Dodged: "+str(count), True, blue)
  gameDisplay.blit(text,(0,0))


def fail():
    largeText = pyg.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("You failed!TuT", largeText)
    TextRect.center = (display_width/2),(display_height/2)
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
#255,165,0