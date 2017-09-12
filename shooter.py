from pygame import *
import random
import numpy as np

init()
window=display.set_mode((600,400))
clock=time.Clock()

black=(0,0,0)
white=(255,255,255)
green=(23,128,28)

photo = image.load("tarcza.png")
photo=transform.scale(photo,(50,50))

photo2 = image.load("celownik.png")
photo2=transform.scale(photo2,(50,50))

class Aim(object):
	def __init__(self):
		self.x=random.randint(0,600)
		self.y=random.randint(0,400)
		self.kx=random.randint(1,5)
		self.ky=random.randint(1,5)
		
		
		
class Game(object):
	def __init__(self):
		self.score=0
		self.aims=[]
		for i in range(10):
			self.aims.append(Aim())
			
	def draw(self):
		window.fill(black)
		
		if view==1:
			draw.line(window,white,(mouse.get_pos()[0],0),(mouse.get_pos()[0],400))
			draw.line(window,white,(0,mouse.get_pos()[1]),(600,mouse.get_pos()[1]))
		elif view==2:
			draw.line(window,white,(mouse.get_pos()[0],mouse.get_pos()[1]-10),(mouse.get_pos()[0],mouse.get_pos()[1]+10))
			draw.line(window,white,(mouse.get_pos()[0]-10,mouse.get_pos()[1]),(mouse.get_pos()[0]+10,mouse.get_pos()[1]))
		elif view==3:
			draw.line(window,white,(mouse.get_pos()[0],mouse.get_pos()[1]-30),(mouse.get_pos()[0],mouse.get_pos()[1]+30))
			draw.line(window,white,(mouse.get_pos()[0]-30,mouse.get_pos()[1]),(mouse.get_pos()[0]+30,mouse.get_pos()[1]))
			draw.circle(window,white,mouse.get_pos(),25,2)
			draw.circle(window,white,mouse.get_pos(),4,4)
		elif view==4:
			window.blit(photo2,(mouse.get_pos()[0]-25,mouse.get_pos()[1]-25))

		
		Font=font.SysFont("comicsansms",72)
		text = Font.render(str(int(self.score)),True,green)
		window.blit(text,(20,-10))
		
		for aim in self.aims:
			window.blit(photo,(aim.x,aim.y))
			
	def move(self):
		for aim in self.aims:
			if aim.x>600:
				aim.x=-25
			else:
				aim.x=aim.x+aim.kx
			if aim.y>400:
				aim.y=-25
			else:
				aim.y=aim.y+aim.ky	
	def shoot(self,x,y):	
		for aim in self.aims:
			distance=np.sqrt((x-aim.x-25)**2+(y-aim.y-25)**2)
			if distance<25:
				self.score=self.score+25-distance
				aim.x=random.randint(0,600)
				aim.y=random.randint(0,400)
				aim.kx=aim.kx+1
				aim.ky=aim.ky+1
game=Game()		
mouse.set_visible(False)		
end=False
view=1
while not end:
	for z in event.get():
		if z.type == QUIT:
			end=True
		if z.type == MOUSEBUTTONUP:
			game.shoot(mouse.get_pos()[0],mouse.get_pos()[1])
	
	keys=key.get_pressed()
	if keys[K_1]:
		view=1
	if keys[K_2]:
		view=2
	if keys[K_3]:
		view=3
	if keys[K_4]:
		view=4
	if keys[K_5]:
		view=5
			
	game.draw()
	game.move()
	clock.tick(20)
	display.flip()