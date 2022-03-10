import pygame

import random

from queue import Queue

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)

segment_width = 48
segment_height = 48
segment_margin = 2

segment_head_x = 12
segment_head_y = 12

x_change = 1 # segment_width + segment_margin
y_change = 0 # segment_height + segment_margin

score = 0

class Segment(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        
        # 設定寬與高
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(WHITE)

        # 左上角座標
        self.rect = self.image.get_rect()
        self.rect.x = x * (segment_width  + segment_margin)
        self.rect.y = y * (segment_height + segment_margin)
        
        self.x = x
        self.y = y
    
# 初始化pygame
pygame.init()

# 設定視窗大小
screen = pygame.display.set_mode([800, 600])

# 視窗標題
pygame.display.set_caption('貪食蛇')

# 所有角色的group物件
all_sprites_list = pygame.sprite.Group()

# 創造初始的貪食蛇
snake_segments = Queue()

for i in range(5):
    x = 3 + i
    y = 3
    segment = Segment(x, y)
    snake_segments.put(segment)
    all_sprites_list.add(segment)
    segment_head_x = x
    segment_head_y = y
    print(i, segment.x, segment.y)
apple_x = 6
apple_y = 6
Apple = Segment(apple_x,apple_y)
all_sprites_list.add(Apple)
Apple.image.fill(RED)

clock = pygame.time.Clock()
done = False
eat = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Set the speed based on the key pressed
        # We want the speed to be enough that we move a full
        # segment, plus the margin.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -1
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = 1
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = -1
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = 1

     
    # 創造最新的一個segment
    segment_head_x += x_change
    segment_head_y += y_change
    segment = Segment(segment_head_x, segment_head_y)

    # 將新的segment插入list中的第一位
    snake_segments.put(segment)
    all_sprites_list.add(segment)

    if segment_head_x == apple_x and segment_head_y == apple_y:
        score = score + 1
        pygame.display.set_caption("貪吃蛇|分數"+ str(score))
        eat = True
        
    if eat:
        apple_x = random.randrange(16)
        apple_y = random.randrange(12)
        all_sprites_list.remove(Apple)
        Apple = Segment(apple_x,apple_y)
        Apple.image.fill(RED)
        all_sprites_list.add(Apple)
        eat = False
    else:
        # 移除尾巴
        old_segment = snake_segments.get()
        all_sprites_list.remove(old_segment)
    # -- 畫出所有東西
    # Clear screen
    screen.fill(BLACK)
    
    all_sprites_list.draw(screen)
    
    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(5)

pygame.quit()



