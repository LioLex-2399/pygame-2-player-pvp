import pygame
from gameDisplay import(
gameDisplay
) 
from time import sleep

plyrskin="plyrs/s1.png"
s1="plyrs/s1.png"
s2="plyrs/s2.png"
s3="plyrs/s3.png"
s4="plyrs/s4.png"
s5="plyrs/s5.png"
s6="plyrs/s6.png"
s7="plyrs/s7.png"
s8="plyrs/s8.png"
s9="plyrs/s9.png"
clock = pygame.time.Clock()
background_colour=255,255,255
gameDisplay.fill(background_colour)
def SkinGallery():
	plyskin=plyrskin
	s1="plyrs/s1.png"
	s2="plyrs/s2.png"
	s3="plyrs/s3.png"
	s4="plyrs/s4.png"
	s5="plyrs/s5.png"
	s6="plyrs/s6.png"
	s7="plyrs/s7.png"
	s8="plyrs/s8.png"
	s9="plyrs/s9.png"
	
	s1p="plyr-2/p1p.png"
	s2p="plyr-2/p2p.png"
	s3p="plyr-2/p3p.png"    
	s4p="plyr-2/p4p.png"
	s5p="plyr-2/p5p.png"
	s6p="plyr-2/p6p.png"
	s7p="plyr-2/p7p.png"
	s8p="plyr-2/p8p.png"
	s9p="plyr-2/p9p.png"
	bckgrd=1,4,54
	gameDisplay.fill(bckgrd)
	while True:
		
		image1 = pygame.image.load(s1)
		gameDisplay.blit(image1, (40, 10))
		
		image2 = pygame.image.load(s2)
		gameDisplay.blit(image2, (80, 10))		
		image3 = pygame.image.load(s3)
		gameDisplay.blit(image3, (120, 10))
		image4 = pygame.image.load(s4)
		gameDisplay.blit(image4, (160, 10))
		image5 = pygame.image.load(s5)
		gameDisplay.blit(image5, (200, 10))
		image6 = pygame.image.load(s6)
		gameDisplay.blit(image6, (240, 10))
		image7 = pygame.image.load(s7)
		gameDisplay.blit(image7, (280, 10))
		image8 = pygame.image.load(s8)
		gameDisplay.blit(image8, (320, 10))
		image9 = pygame.image.load(s9)
		gameDisplay.blit(image9, (360, 10))

		
#		image = pygame.image.load(plyskin)
#		gameDisplay.blit(image, (300, 400))
		for event in pygame.event.get():
			

			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			elif event.type ==pygame.KEYDOWN:
				if event.key == pygame.K_1 :
					plyskin=s1
				if event.key == pygame.K_2:
					plyskin=s2
				if event.key == pygame.K_3 :
					plyskin=s3
				if event.key == pygame.K_4:
					plyskin=s4
				if event.key == pygame.K_5 :
					plyskin=s5
				if event.key == pygame.K_6:
					plyskin=s6
				if event.key == pygame.K_7 :
					plyskin=s7
				if event.key == pygame.K_8:
					plyskin=s8
				if event.key == pygame.K_9 :
					plyskin=s9
				if event.key == pygame.K_RETURN:
					lvl1(plyskin)
		
		if plyskin == s1:
			image = pygame.image.load(s1p)
			gameDisplay.blit(image, (200, 300))
			
		if plyskin == s2:
			image = pygame.image.load(s2p)
			gameDisplay.blit(image, (200, 300))
			
		if plyskin == s3:
			image = pygame.image.load(s3p)
			gameDisplay.blit(image, (200, 300))

		if plyskin == s4:
			image = pygame.image.load(s4p)
			gameDisplay.blit(image, (200, 300))
		
		if plyskin == s5:
			image = pygame.image.load(s5p)
			gameDisplay.blit(image, (200, 300))
			
		if plyskin == s6:
			image = pygame.image.load(s6p)
			gameDisplay.blit(image, (200, 300))
			
		if plyskin == s7:
			image = pygame.image.load(s7p)
			gameDisplay.blit(image, (200, 300))
			
		if plyskin == s8:
			image = pygame.image.load(s8p)
			gameDisplay.blit(image, (200, 300))
			
		if plyskin == s9:
			image = pygame.image.load(s9p)
			gameDisplay.blit(image, (200, 300))
		##tips!##
		pygame.draw.rect(gameDisplay, (100,100,205), (9,90,150,450),(2000))
		font1 = pygame.font.Font('amatic-sc.bold.ttf', 32)
		img1 = font1.render('___tips!___', True, (0,255,0))
		gameDisplay.blit(img1, (12, 93))

		font1 = pygame.font.Font('amatic-sc.bold.ttf', 22)
		img1 = font1.render('-use the keys 1 to 9 ', True, (2,240,0))
		gameDisplay.blit(img1, (12, 123))
		

		font1 = pygame.font.Font('amatic-sc.bold.ttf', 22)
		img1 = font1.render('to navigate through ', True, (2,240,0))
		gameDisplay.blit(img1, (12, 143))

		font1 = pygame.font.Font('amatic-sc.bold.ttf', 22)
		img1 = font1.render('skins', True, (2,240,0))
		gameDisplay.blit(img1, (12, 163))

		font1 = pygame.font.Font('amatic-sc.bold.ttf', 22)
		img1 = font1.render('- finished yet?   ', True, (2,240,0))
		gameDisplay.blit(img1, (12, 183))

		
		font1 = pygame.font.Font('amatic-sc.bold.ttf', 22)
		img1 = font1.render('press "Enter" if yes', True, (2,240,0))
		gameDisplay.blit(img1, (12, 203))

		
		pygame.display.update()
		clock.tick(60)

#	plyrskin=plyskin
plyrskin=plyrskin
pygame.font.init()

###################################
###################################
###################################
def lvl1(skin):
	plyrskn2=skin 
	enmyskn="bosses/boss1.png"
	bckgrd=4,156,255
	enemyhlth=200
	plyrhlth=50
	b_s_atkdam=10
	b_s_atkcldn=100
	bcooldown=0
	boss_ackdam=2
	x1=350
	y1=570
	
	x2=350
	y2=10
	while True:
		gameDisplay.fill(bckgrd)
		#player
		pygame.draw.line(gameDisplay, (6,6,6), (0, 550), (800, 550),(4))

		image1 = pygame.image.load(plyrskn2)
		gameDisplay.blit(image1, (350, 570))
#		print()


		#boss
		pygame.draw.line(gameDisplay, (6,6,6), (0, 50), (800, 50),(4))		
		image1 = pygame.image.load(enmyskn)
		gameDisplay.blit(image1, (350, 10))
		
		my_font = pygame.font.Font('amatic-sc.bold.ttf', 30)
		text_surface = my_font.render('health: '+str(enemyhlth)+"%", True, (0, 0, 0))
		
		gameDisplay.blit(text_surface, (4,4))
		
		bcooldown += 1
		if bcooldown ==  b_s_atkcldn:
			plyrhlth-=b_s_atkdam
			bcooldown==0
		if plyrhlth <= 0 or enemyhlth<=0:
			print()
		for event in pygame.event.get():
			

			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			elif event.type ==pygame.KEYDOWN:
				if event.key == pygame.K_a :
					print()
		pygame.display.update()
		clock.tick(60)

		