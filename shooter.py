from pygame import *
import random
import numpy as np

init()
okno=display.set_mode((600,400))
zegar=time.Clock()

black=(0,0,0)
white=(255,255,255)
green=(23,128,28)

photo = image.load("tarcza.png")
photo=transform.scale(photo,(50,50))

photo2 = image.load("celownik.png")
photo2=transform.scale(photo2,(50,50))

class Cel(object):
	def __init__(self):
		self.x=random.randint(0,600)
		self.y=random.randint(0,400)
		self.kx=random.randint(1,5)
		self.ky=random.randint(1,5)
		
		
		
class Gra(object):
	def __init__(self):
		self.wynik=0
		self.cele=[]
		for i in range(10):
			self.cele.append(Cel())
			
	def rysuj(self):
		okno.fill(black)
		
		if celownik==1:
			draw.line(okno,white,(mouse.get_pos()[0],0),(mouse.get_pos()[0],400))
			draw.line(okno,white,(0,mouse.get_pos()[1]),(600,mouse.get_pos()[1]))
		elif celownik==2:
			draw.line(okno,white,(mouse.get_pos()[0],mouse.get_pos()[1]-10),(mouse.get_pos()[0],mouse.get_pos()[1]+10))
			draw.line(okno,white,(mouse.get_pos()[0]-10,mouse.get_pos()[1]),(mouse.get_pos()[0]+10,mouse.get_pos()[1]))
		elif celownik==3:
			draw.line(okno,white,(mouse.get_pos()[0],mouse.get_pos()[1]-30),(mouse.get_pos()[0],mouse.get_pos()[1]+30))
			draw.line(okno,white,(mouse.get_pos()[0]-30,mouse.get_pos()[1]),(mouse.get_pos()[0]+30,mouse.get_pos()[1]))
			draw.circle(okno,white,mouse.get_pos(),25,2)
			draw.circle(okno,white,mouse.get_pos(),4,4)
		elif celownik==4:
			okno.blit(photo2,(mouse.get_pos()[0]-25,mouse.get_pos()[1]-25))

		
		czcionka=font.SysFont("comicsansms",72)
		text = czcionka.render(str(int(self.wynik)),True,green)
		okno.blit(text,(20,-10))
		
		for cel in self.cele:
			okno.blit(photo,(cel.x,cel.y))
			
	def krok(self):
		for cel in self.cele:
			if cel.x>600:
				cel.x=-25
			else:
				cel.x=cel.x+cel.kx
			if cel.y>400:
				cel.y=-25
			else:
				cel.y=cel.y+cel.ky	
	def strzal(self,x,y):	
		for cel in self.cele:
			odleglosc=np.sqrt((x-cel.x-25)**2+(y-cel.y-25)**2)
			if odleglosc<25:
				self.wynik=self.wynik+25-odleglosc
				cel.x=random.randint(0,600)
				cel.y=random.randint(0,400)
				cel.kx=cel.kx+1
				cel.ky=cel.ky+1
gra=Gra()		
mouse.set_visible(False)		
koniec=False
celownik=1
while not koniec:
	for z in event.get():
		if z.type == QUIT:
			koniec=True
		if z.type == MOUSEBUTTONUP:
			gra.strzal(mouse.get_pos()[0],mouse.get_pos()[1])
	
	keys=key.get_pressed()
	if keys[K_1]:
		celownik=1
	if keys[K_2]:
		celownik=2
	if keys[K_3]:
		celownik=3
	if keys[K_4]:
		celownik=4
	if keys[K_5]:
		celownik=5
			
	gra.rysuj()
	gra.krok()
	zegar.tick(20)
	display.flip()