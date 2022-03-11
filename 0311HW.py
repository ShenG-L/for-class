from doctest import script_from_examples
import pygame

import random

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

class Block(pygame.sprite.Sprite):
    def __init__(self,color,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
    
pygame.init()

screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width,screen_height])

block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()

for i in range(50):
    block = Block(BLACK,20,15)

    block.rect.x = random.randrange(screen_width)
    block.rect.y = random.randrange(screen_height)

    block_list.add(block)

    all_sprites_list.add(block)

player = Block(RED,20,15)
all_sprites_list.add(player)

score = 0
font = pygame.font.Font(None,50)
start_ticks = pygame.time.get_ticks()

play = True
clock = pygame.time.Clock()

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    seconds = int((pygame.time.get_ticks() - start_ticks)/1000)

    if seconds > 10:
        text = font.render("GAME OVER", 50 ,BLACK)
        screen.blit(text,(100,100))
        play = False

    pos = pygame.mouse.get_pos()
    player.rect.x = pos[0]
    player.rect.y = pos[1]

    block_hit_list = pygame.sprite.spritecollide(player,block_list,True)
 
    for block in block_hit_list:
        score += 1

    screen.fill(WHITE)
    all_sprites_list.draw(screen)

    message = str(score) + "points"
    text = font.render(message , 10 ,BLACK)
    screen.blit(text,(10,10))

    t = font.render(str(seconds), 10, RED)
    screen.blit(t,(10,40))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()