
import pygame
import random
import math
import time

BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)

class Ball(pygame.sprite.Sprite):    
    def __init__(self,speed,x,y,radius,color):
        super().__init__()
        self.x = x
        self.y = y        
        self.image = pygame.Surface([radius*2,radius*2])
        self.image.fill(WHITE)
        pygame.draw.circle(self.image, color, (radius,radius), radius)
        
        self.rect = self.image.get_rect()   #取得球體區域
        self.rect.center = (x,y)            #初始位置
        direction = random.randint(20,70)   #移動角度
        radian = math.radians(direction)    #角度轉為弳度
        self.dx = speed * math.cos(radian)  #球水平運動速度
        self.dy = -speed * math.sin(radian) #球垂直運動速度
        
    def update(self):
        self.x += self.dx  #計算球新餘標
        self.y += self.dy
        self.rect.x = self.x  #移動球圖形
        self.rect.y = self.y
        
        if(self.rect.left <= 0 or self.rect.right >= screen.get_width()):  #到達左右邊界
            self.dx *= -1  #水平速度變號
        if(self.rect.top <= 0):  #到達上邊界
            self.dy *= -1  #垂直速度變號
        if(self.rect.bottom >= screen.get_height()):#到達下邊界
            return False
        return True

class Brick(pygame.sprite.Sprite):
    def __init__(self,color,x,y):
        super().__init__()
        self.image = pygame.Surface([38, 13])  #磚塊38x13
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./media/pad.png")  #滑板圖片
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.x = int((screen.get_width() - self.rect.width)/2)  #滑板位置
        self.rect.y = screen.get_height() - self.rect.height - 20
 
    def update(self):  #滑板位置隨滑鼠移動
        pos = pygame.mouse.get_pos()  #取得滑鼠坐標
        self.rect.x = pos[0]  #滑鼠x坐標
        if self.rect.x > screen.get_width() - self.rect.width:  #不要移出右邊界
            self.rect.x = screen.get_width() - self.rect.width

def gameover(message):
    global done            
    text = font1.render(message, 1, (255,0,255))  #顯示訊息
    screen.blit(text, (screen.get_width()/2-100,screen.get_height()/2-20))
    pygame.display.update()  #更新畫面
    time.sleep(3)  #暫停3秒
    done = True  #結束程式
    
pygame.init()

font = pygame.font.SysFont("SimHei", 20)  #下方訊息字體
font1 = pygame.font.SysFont("SimHei", 32)  #結束程式訊息字體
soundhit = pygame.mixer.Sound("./media/hit.wav")
soundpad = pygame.mixer.Sound("./media/pad.wav")

screen = pygame.display.set_mode((600,400))

pygame.display.set_caption("打磚塊完整版")

all_sprites_list = pygame.sprite.Group()  #建立角色群組
bricks = pygame.sprite.Group()

Brick_Color_list = (GREEN,GREEN,BLUE,BLUE)

for i in range(4):
    for j in range(15):
        brick = Brick(Brick_Color_list[i], j * 40 + 1, 1 + i * 15)
        all_sprites_list.add(brick)
        bricks.add(brick)

ball = Ball(10, 200, 250, 10, RED)  #建立紅色球物件
all_sprites_list.add(ball)

paddle = Paddle()
all_sprites_list.add(paddle)

clock = pygame.time.Clock()
done = False
playing = False
scores = 0
msgstr = 'Click left button to start'

while not done:
    # 事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    buttons = pygame.mouse.get_pressed()  #檢查滑鼠按鈕
    if buttons[0] == True:  #按滑鼠左鍵後球可移動
        playing = True
    
    
    if playing:
        # 依據事件更新位置
        conti = ball.update()
        
        hitbrick = pygame.sprite.spritecollide(ball, bricks, True)  #檢查球和磚塊碰撞
        if len(hitbrick) > 0:  #球和磚塊發生碰撞
            scores += len(hitbrick)  #計算分數
            soundhit.play()  #球撞磚塊聲
            ball.rect.y += 20  #球向下移
            ball.dy *= -1  #球反彈
            if len(bricks) == 0:  #所有磚塊消失
                gameover("WIN!!")
                
        hitpad = pygame.sprite.collide_rect(ball, paddle)  #檢查球和滑板碰撞
        if hitpad:  #球和滑板發生碰撞
            soundpad.play()  #球撞滑板聲
            ball.dy *= -1  #球反彈
        paddle.update()
        
        if not conti:
            gameover('GAME OVER!')
        
        msgstr = 'Score : ' +str(scores)
        # 畫出圖形
        screen.fill(WHITE)  #清除繪圖視窗
        all_sprites_list.draw(screen)
    
    msg = font.render(msgstr, 1, (255,0,255))
    screen.blit(msg, (screen.get_width()/2-60,screen.get_height()-20))  #繪製訊息
    
    pygame.display.flip()
    # 每秒跑30次
    clock.tick(30)
pygame.quit()
