import pygame

import random

import math

BLUE = (0,0,255)
RED = (255,0,0)
WHITE = (255,255,255)

class Ball(pygame.sprite.Sprite):
    def __init__(self,speed,x,y,raduis,color):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.Surface([raduis*2,raduis*2])
        self.image.fill(WHITE)
        pygame.draw.circle(self.image,color,(raduis,raduis),raduis)
        
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        direction = random.randint(20,70)
        radian = math.radians(direction)
        self.dx = speed * math.cos(radian)
        self.dy = -speed * math.sin(radian)
    
    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.rect.x = self.x
        self.rect.y = self.y

        if(self.rect.left <= 0 or self.rect.right >=screen.get_width()):
            self.dx *= -1
        if(self.rect.top <= 0 or self.rect.bottom >=screen.get_height()):
            self.dy *= -1

pygame.init()

screen = pygame.display.set_mode((400,300))

pygame.display.set_caption('打磚塊')

all_sprite_list = pygame.sprite.Group()

ball1 = Ball(8,100,100,10,BLUE)
all_sprite_list.add(ball1)
ball2 = Ball(6,20,250,10,RED)
all_sprite_list.add(ball2)

clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    ball1.update()
    ball2.update()

    screen.fill(WHITE)
    all_sprite_list.draw(screen)
    pygame.display.flip()
    clock.tick(30)

pygame.quit ()
