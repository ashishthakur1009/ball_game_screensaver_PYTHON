import pygame,random

pygame.init()

width=500
height=500
screen=pygame.display.set_mode((width,height))
WHITE=255,255,255
RED=255,0,0

class Ball:
    def _init(self):
        self.x=0
        self.y=0
        self.moveX=1
        self.moveY=1
        self.radius=20
        self.color=random.randint(0,255)
    def update(self):
        self.x=self.moveX
        self.y=self.moveY
        if self.y>height-55:
            moveY=-1
        elif self.y<0:
            moveY=1
        elif self.x<0:
            moveX=1
        elif self.x>width-55:
            moveX=-1
while True:
    for event in pygame.event.get():
        #print(event)
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()