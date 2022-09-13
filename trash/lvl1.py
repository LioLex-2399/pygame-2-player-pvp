from gameDisplay import gameDisplay,pygame
clock = pygame.time.Clock()
def lvl1(skin,skin2):
	plyrskn2="plyrs/s1.png" 
	enmyskn=skin2
	bckgrd=4,156,255
	enemyhlth=100
	plyrhlth=100
	b_s_atkdam=10
	b_s_atkcldn=100
	bcooldown=0
	boss_ackdam=2
	x1=350
	y1=520
	x3=350
	y3=570
	bullet1=False
	bullet2=False
	
	x2=350
	y2=10
	x4=350
	y4=570
	while True:
		gameDisplay.fill(bckgrd)
		#player
		
		my_font = pygame.font.Font('amatic-sc.bold.ttf', 30)
		text_surface = my_font.render('health: '+str(plyrhlth)+"%", True, (0, 0, 0))
		
		gameDisplay.blit(text_surface, (4,500))
		pygame.draw.line(gameDisplay, (6,6,6), (0, 500), (800, 500),(4))

		image1 = pygame.image.load(plyrskn2)
		gameDisplay.blit(image1, (x1, y1))
#		print()


		#boss
		pygame.draw.line(gameDisplay, (6,6,6), (0, 50), (800, 50),(4))		
		image1 = pygame.image.load(enmyskn)
		gameDisplay.blit(image1, (x2, y2))
		
		my_font = pygame.font.Font('amatic-sc.bold.ttf', 30)
		text_surface = my_font.render('health: '+str(enemyhlth)+"%", True, (0, 0, 0))
		
		gameDisplay.blit(text_surface, (4,4))
		
		bcooldown += 1
		if bcooldown ==  b_s_atkcldn:
			plyrhlth-=b_s_atkdam
			bcooldown==0
		if plyrhlth <= 0 or enemyhlth<=0:
			pygame.quit()
		for event in pygame.event.get():
			

			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			elif event.type ==pygame.KEYDOWN:
				if event.key == pygame.K_a :
					x1-=10
				if event.key == pygame.K_d :
					x1+=10
				if event.key == pygame.K_w :
					bullet1=True
				if event.key == pygame.K_SPACE :
					bullet2=True
				if event.key == pygame.K_RIGHT :
					x2+=10
				if event.key == pygame.K_LEFT :
					x2-=10
		if bullet1:
			if not y3 == y2 and x3 ==x2 :
				if not y3 <=0:
					y3-=10
					image1 = pygame.image.load("bullet2/jay.png")
					gameDisplay.blit(image1, (x3, y3))
				else:
					bullet1=False
			else:
				enemyhlth-=10
				bullet1=False
		if not bullet1:
			x3=x1
			y3=y1

			
		if bullet2:
			if not y4 == y1 and x4 ==x1 :
				if not y4 <=555:
					y4+=10
					image1 = pygame.image.load("bullets/jay.png")
					gameDisplay.blit(image1, (x3, y3))
				else:
					bullet2=False
			else:
				plyrhlth-=10
				bullet2=False
		if not bullet2:
			x4=x2
			y4=y2

		
		pygame.display.update()
		clock.tick(60)

		
		
		
		
		
		
		
		
		
		
	