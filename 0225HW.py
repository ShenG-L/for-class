import pygame

from queue import  Queue

BLACK = (0,0,0)
WHITE = (255,255,255)

segment_w = 15
segment_h = 15

segment_margin = 3
segment_head_x = 0
segment_head_y = 0

x_change = segment_w + segment_margin
y_change = 0

class Segment(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()

        self.image = pygame.Surface([segment_w , segment_h])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

pygame.init()

screen = pygame.display.set_mode([800,600])

pygame.display.set_caption("貪吃蛇")

all_sprites_list = pygame.sprite.Group()

snake_segment = Queue()

for i in range(3):
    x = 0 + (segment_w + segment_margin) * i
    y = 3
    segment = Segment(x,y)
    snake_segment.put(segment)
    all_sprites_list.add(segment)
    segment_head_x = x
    segment_head_y = y

clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x_change = (segment_w + segment_margin) * (-1)
            y_change = 0
        if event.key == pygame.K_RIGHT:
            x_change = (segment_w + segment_margin)
            y_change = 0
        if event.key == pygame.K_UP:
            y_change = (segment_h + segment_margin) * (-1)
            x_change = 0
        if event.key == pygame.K_DOWN:
            y_change = (segment_h + segment_margin)
            x_change = 0


    old_segment = snake_segment.get()
    all_sprites_list.remove(old_segment)

    segment_head_x = segment_head_x + x_change
    segment_head_y = segment_head_y + y_change
    new_segment = Segment(segment_head_x,segment_head_y)
    snake_segment.put(new_segment)
    all_sprites_list.add(new_segment)


    screen.fill(BLACK)
    all_sprites_list.draw(screen)

    pygame.display.flip()

    clock.tick(3)


pygame.quit()


