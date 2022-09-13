import pygame,random
from gameDisplay import gameDisplay
clock = pygame.time.Clock()
from winner import win
pygame.init()
def lvl1(p1skin,p2skin,att1,att2):
	
	
	p1atckskin=""
	bckgrd=4,156,255
	enemyhlth=100
	plyrhlth=100
	p2bullet=False
	p1countdown=0
	p2countdown=2
	x1=350
	y1=500
	x3=350
	y3=500
	p1bullet=False
	x2=350
	y2=10
	x4=350
	y4=10

	while True:
		background_colour=0,200,55
		gameDisplay.fill(background_colour)
		#player
		my_font = pygame.font.Font('amatic-sc.bold.ttf', 30)
		text_surface = my_font.render('health: '+str(plyrhlth)+"%", True, (0, 0, 0))
		
		gameDisplay.blit(text_surface, (4,490))		
		pygame.draw.line(gameDisplay, (6,6,6), (0, 480), (800, 480),(4))
		image1 = pygame.image.load(p1skin)
		gameDisplay.blit(image1, (x1, y1))
#		print()


		#boss
		pygame.draw.line(gameDisplay, (6,6,6), (0, 50), (800, 50),(4))		
		image1 = pygame.image.load(p2skin)
		gameDisplay.blit(image1, (x2, y2))
		
		my_font = pygame.font.Font('amatic-sc.bold.ttf', 30)
		text_surface = my_font.render('health: '+str(enemyhlth)+"%", True, (0, 0, 0))
		
		gameDisplay.blit(text_surface, (4,4))
		

		if plyrhlth <= 0 or enemyhlth<=0:
			win(plyrhlth,enemyhlth)
			
		for event in pygame.event.get():
			

			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			elif event.type ==pygame.KEYDOWN:
				if event.key == pygame.K_a :
					x1-=20
				elif event.key==pygame.K_d:
					x1+=20
				elif event.key == pygame.K_w:
					p1bullet=True
				elif event.key == pygame.K_UP:
					p2bullet=True
				if event.key == pygame.K_LEFT :
					x2-=20
				elif event.key==pygame.K_RIGHT:
					x2+=20
		if p1bullet:
			y3-=10
			image1 = pygame.image.load(att1)
			gameDisplay.blit(image1, (x3, y3))
			print(y3)
		if y3 == y2 and x3 == x2:
			enemyhlth-= 10
			x3=x1
			y3=y1
			p1bullet=False
		if y3 == 0:
			x3=x1
			y3=y1
			p1bullet=False
		if not p1bullet:
			x3=x1
			y3=y1
			
#######__ loop tab = 2	
		"""
		bosscld=random.randint(80,200)
#		print(bosscld)
		countdown+=1
		if countdown == bosscld:
			countdown=0
			p2bullet=True
			print("ddddd")
		"""
		
		if p2bullet:
			y4+=10
			image1 = pygame.image.load(att2)
			gameDisplay.blit(image1, (x4, y4))
		if y4 == y1 and x4 == x1:
			plyrhlth-= 10
			x4=x2
			y4=y2
			p2bullet=False
		if y4 == 500:
			x4=x2
			y4=y2
			p2bullet=False
		if not p2bullet:
			x4=x2
			y4=y2
		if x1 <= 100:
			x1+=20
		
		
			
			
			
			
			
			
			
			
			
			

			
			
			
			

			

			
			
#		print(y3)
		pygame.display.update()
		clock.tick(60)

		