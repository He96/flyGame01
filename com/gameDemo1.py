import pygame
from pygame.locals import *  # 导入pygame库中一些常量
from sys import exit  # sys库中的exit函数
from random import randint
import time
import base64
import os
# 加载base64图片
from bang0_png import img as bs_bang0
from bang1_png import img as bs_bang1
from bang2_png import img as bs_bang2
from bang3_png import img as bs_bang3
from bg1_jpg import img as bs_bg1
from bg2_jpg import img as bs_bg2
from dan_png import img as bs_dan
from dan1_png import img as bs_dan1
from dan3_png import img as bs_dan3
from dan4_png import img as bs_dan4
from GG1_jpg import img as bs_GG1
from me_png import img as bs_me
from other_png import img as bs_other
from gou3_png import img as bs_gou

imgArray = ['bang0.png','bang1.png','bang2.png','bang3.png','bg1.jpg','bg2.jpg','dan.png'
                ,'dan1.png','dan3.png','dan4.png','GG1.jpg','me.png','other.png','gou3.png']
tmp1 = open('bang0.png', 'wb')
tmp1.write(base64.b64decode(bs_bang0))
tmp1.close()
tmp2 = open('bang1.png', 'wb')
tmp2.write(base64.b64decode(bs_bang1))
tmp2.close()
tmp3 = open('bang2.png', 'wb')
tmp3.write(base64.b64decode(bs_bang2))
tmp3.close()
tmp4 = open('bang3.png', 'wb')
tmp4.write(base64.b64decode(bs_bang3))
tmp4.close()
tmp5 = open('bg1.jpg', 'wb')
tmp5.write(base64.b64decode(bs_bg1))
tmp5.close()
tmp6 = open('bg2.jpg', 'wb')
tmp6.write(base64.b64decode(bs_bg2))
tmp6.close()
tmp7 = open('dan.png', 'wb')
tmp7.write(base64.b64decode(bs_dan))
tmp7.close()
tmp8 = open('dan1.png', 'wb')
tmp8.write(base64.b64decode(bs_dan1))
tmp8.close()
tmp9 = open('dan3.png', 'wb')
tmp9.write(base64.b64decode(bs_dan3))
tmp9.close()
tmp10 = open('dan4.png', 'wb')
tmp10.write(base64.b64decode(bs_dan4))
tmp10.close()
tmp11 = open('GG1.jpg', 'wb')
tmp11.write(base64.b64decode(bs_GG1))
tmp11.close()
tmp12 = open('me.png', 'wb')
tmp12.write(base64.b64decode(bs_me))
tmp12.close()
tmp13 = open('other.png', 'wb')
tmp13.write(base64.b64decode(bs_other))
tmp13.close()
tmp13 = open('gou3.png', 'wb')
tmp13.write(base64.b64decode(bs_gou))
tmp13.close()
bg1 = 'bg1.jpg'
background_image = 'bg2.jpg'
plain_image = 'me.png'
dan_image = 'dan.png'
dan1_image = 'dan1.png'
dan3_image = 'dan3.png'
dan4_image = 'dan4.png'
other_image = 'other.png'
# 爆炸类
bang0_image = 'bang0.png'
bang1_image = 'bang1.png'
bang2_image = 'bang2.png'
bang3_image = 'bang3.png'
# game over
gameOver_image = 'GG1.jpg'
gou_image = 'gou3.png'

def moveImg(imgArray):
    for item in imgArray:
        os.remove(item)

def play():
    # 定义窗口分辨率
    SCREEN_WIDTH = 460
    SCREEN_HEIGHT = 720
    FPS = 70  # 定义帧频率
    K_S = 10  # 攻速
    B_K = 1  # 爆炸效果
    ANIMATE_CYCLE = 30  # 定义动画周期
    ticks = 0  # 计数器
    oldTime = 0  # 计数器
    clock = pygame.time.Clock()  # 创建记录时间对象
    offset = {pygame.K_LEFT: 0, pygame.K_RIGHT: 0, pygame.K_UP: 0, pygame.K_DOWN: 0}

    # 子弹类
    class Bullet(pygame.sprite.Sprite):
        def __init__(self, bullet_surface, bullet_init_pos):
            pygame.sprite.Sprite.__init__(self)
            self.image = bullet_surface
            self.rect = self.image.get_rect()
            self.rect.topleft = bullet_init_pos
            self.speed = 4

        # 控制子弹移动
        def update(self):
            self.rect.top -= self.speed
            if self.rect.top < -self.rect.height:
                self.kill()
        # 敌方子弹移动
        def update1(self):
            self.rect.top += (self.speed*1.5)
            if self.rect.top > self.rect.height:
                self.kill()

    # 玩家类
    class Hero(pygame.sprite.Sprite):
        def __init__(self, hero_surface, hero_init_pos):
            pygame.sprite.Sprite.__init__(self)
            self.image = hero_surface
            self.rect = self.image.get_rect()
            self.rect.topleft = hero_init_pos
           # self.rect.topright = hero_init_pos
            self.speed = 6
            self.is_kill = False  # GG
            # 子弹1的Group
            self.bullets1 = pygame.sprite.Group()
            # 子弹2的Group
            self.bullets2 = pygame.sprite.Group()

        # 定义移动规则
        def move(self, offset):
            x = self.rect.left + offset[pygame.K_RIGHT] - offset[pygame.K_LEFT]
            y = self.rect.top + offset[pygame.K_DOWN] - offset[pygame.K_UP]
            if x < 0:
                self.rect.left = 0
            elif x > SCREEN_WIDTH - self.rect.width:
                self.rect.left = SCREEN_WIDTH - self.rect.width
            else:
                self.rect.left = x
            if y < 0:
                self.rect.top = 0
            elif y > SCREEN_HEIGHT - self.rect.height:
                self.rect.top = SCREEN_HEIGHT - self.rect.height
            else:
                self.rect.top = y

        # 控制射击
        def single_shoot(self, bullet1_surface):
            bullet1 = Bullet(bullet1_surface, self.rect.topleft)
            bullet2 = Bullet(bullet1_surface,self.rect.topright)
            self.bullets1.add(bullet1)
            self.bullets2.add(bullet2)
    # 敌机类
    class Enemy(pygame.sprite.Sprite):
        def __init__(self, enemy_surface, enemy_init_pos):
            pygame.sprite.Sprite.__init__(self)
            self.image = enemy_surface
            self.rect = self.image.get_rect()
            self.rect.topleft = enemy_init_pos
            self.speed = 2
            self.bullets1 = pygame.sprite.Group()
            # 爆炸动画索引
            self.down_index = 0

        def update(self):
            self.rect.top += self.speed
            if self.rect.top > SCREEN_HEIGHT:
                self.kill()

        def single_shoot(self, bullet1_surface):
            bullet1 = Bullet(bullet1_surface, self.rect.topleft)
            bullet1.update1()
            self.bullets1.add(bullet1)

    hero_down_index = 1  # 玩家爆炸效果

    # 初始化游戏

    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    # 载入背景图
    background = pygame.image.load(background_image)
    # 飞机
    plain = pygame.image.load(plain_image)
    # 敌机
    other = pygame.image.load(other_image)
    enemy1_surface = other.subsurface(pygame.Rect(0, 0, 48, 48))
    # 敌机爆炸
    bang0 = pygame.image.load(bang0_image)
    bang1 = pygame.image.load(bang1_image)
    bang2 = pygame.image.load(bang2_image)
    bang3 = pygame.image.load(bang3_image)
    enemy1_down_surface = []
    enemy1_down_surface.append(bang0.subsurface(pygame.Rect(0, 0, 16, 16)))
    enemy1_down_surface.append(bang1.subsurface(pygame.Rect(0, 0, 32, 32)))
    enemy1_down_surface.append(bang2.subsurface(pygame.Rect(0, 0, 64, 64)))
    enemy1_down_surface.append(bang3.subsurface(pygame.Rect(0, 0, 128, 128)))
    # 子弹
    dan = pygame.image.load(dan_image)
    dan1 = pygame.image.load(dan1_image)
    dan3 = pygame.image.load(dan3_image)
    dan4 = pygame.image.load(dan4_image)
    gou = pygame.image.load(gou_image)
    # GG
    gameover = pygame.image.load(gameOver_image)
    # 剪切读入的图片
    hero_surface = []
    hero1_rect = pygame.Rect(0, 0, 64, 64)
    hero2_rect = pygame.Rect(0, 4, 64, 60)
    hero1 = plain.subsurface(hero1_rect)
    hero2 = plain.subsurface(hero2_rect)
    hero_surface.append(hero1)
    hero_surface.append(hero2)
    hero_surface.append(bang1)
    hero_surface.append(bang2)
    hero_pos = [180, 700]
    # bullet1图片
    # Q
    bullet1_surface = dan.subsurface(pygame.Rect(0, 0, 16, 16))
    # W
    bullet2_surface = dan1.subsurface(pygame.Rect(0, 0, 34, 32))
    # E
    bullet3_surface = gou.subsurface(pygame.Rect(0, 0, 48, 48))
    # R
    bullet4_surface = dan4.subsurface(pygame.Rect(0, 0, 128, 128))
    # 选择技能
    bullet_surface = bullet1_surface
    # 创建玩家
    hero = Hero(hero_surface[0], hero_pos)
    # 创建敌机
    enemy1_group = pygame.sprite.Group()
    # 创建击毁敌机组
    enemy1_down_group = pygame.sprite.Group()
    # 分数
    score = 0
    # 循环事件 mainloop
    while True:
        clock.tick(FPS)  # 控制在70帧以内
        screen.blit(background, (0, 0))  # 画背景
        # 加分
        score_font = pygame.font.SysFont('SimHei', 26)
        score_text = score_font.render('得分:' + str(score), True, (191, 44, 73))
        text_rect = score_text.get_rect()
        text_rect.topleft = [10, 10]
        screen.blit(score_text, text_rect)
        nowTime = int(time.time())
        if nowTime - oldTime >= 1:
            score += 1
            oldTime = nowTime
        # x, y = pygame.mouse.get_pos()  # 获得鼠标位置
        # GG
        if hero.is_kill:
            hero.image = hero_surface[hero_down_index]
            hero_down_index += 1
            if hero_down_index > 3:
                screen.blit(hero.image, hero.rect)
                pygame.display.update()
                break
        else:
            ov = (ticks // (ANIMATE_CYCLE // 2))
            if ov > 1:
                ov = 1
            hero.image = hero_surface[ov]
        # 画上飞机
        if ticks >= ANIMATE_CYCLE:
            ticks = 0
        screen.blit(hero.image, hero.rect)
        ticks += 1
        # screen.blit(plan_cursor, (500, 600))
        # 射击
        if ticks % K_S == 0:
            hero.single_shoot(bullet_surface)
        # 控制子弹
        hero.bullets1.update()
        hero.bullets2.update()
        # 绘制子弹
        hero.bullets1.draw(screen)
        hero.bullets2.draw(screen)
        # 产生敌机
        if ticks % 30 == 0:
            enemy = Enemy(enemy1_surface,
                          [randint(0, SCREEN_WIDTH - enemy1_surface.get_width()), -enemy1_surface.get_height()])
            enemy.bullets1.update()
            enemy.bullets1.draw(screen)
            if ticks % K_S == 0:
                enemy.single_shoot(bullet1_surface)
            enemy1_group.add(enemy)
        # 控制敌机
        enemy1_group.update()
        # 绘制敌机
        enemy1_group.draw(screen)
        # 监测敌机与子弹碰撞
        enemy1_down_group.add(pygame.sprite.groupcollide(enemy1_group, hero.bullets1, True, True))
        enemy1_down_group.add(pygame.sprite.groupcollide(enemy1_group, hero.bullets2, True, True))
        for enemy1_down in enemy1_down_group:
            screen.blit(enemy1_down_surface[enemy1_down.down_index], enemy1_down.rect)
            if ticks % (ANIMATE_CYCLE // 2) == 0:
                if enemy1_down.down_index < B_K:
                    if B_K >= 2:
                        enemy1_down.down_index = B_K
                    else:
                        enemy1_down.down_index += 1
                else:
                    enemy1_down_group.remove(enemy1_down)
                    # 加分
                    score += 10
        # 监测敌机与玩家碰撞
        enemy1_down_list = pygame.sprite.spritecollide(hero, enemy1_group, True)
        if len(enemy1_down_list) > 0:
            enemy1_down_group.add(enemy1_down_list)
            hero.is_kill = True
        # 刷新画面
        pygame.display.update()
        # 处理游戏退出
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key in offset:
                    offset[event.key] = 3
            elif event.type == pygame.KEYUP:
                if event.key in offset:
                    offset[event.key] = 0
                elif event.key == 113:
                    # 触发Q技能 300ms CD
                    K_S = 10
                    B_K = 1
                    bullet_surface = bullet1_surface
                    pygame.display.update()
                elif event.key == pygame.K_w:
                    # 触发W
                    time.sleep(0.2)
                    K_S = 15
                    B_K = 2
                    bullet_surface = bullet2_surface
                    pygame.display.update()
                elif event.key == pygame.K_e:
                    # 触发E
                    time.sleep(0.2)
                    K_S = 30
                    B_K = 3
                    bullet_surface = bullet3_surface
                    pygame.display.update()
                elif event.key == pygame.K_r:
                    # 触发R
                    K_S = 25
                    B_K = 3
                    time.sleep(0.3)
                    bullet_surface = bullet4_surface
                    pygame.display.update()
                elif event.key == pygame.K_t:
                    hero.is_kill = True
        hero.move(offset)
    # 结束游戏
    screen.blit(gameover, (0, 0))
    GT_font = pygame.font.SysFont('SimHei', 56)
    GT_font.set_bold(200)
    GT_text = GT_font.render('Game Over!', True, (243, 80, 68))
    GT_rect = GT_text.get_rect()
    GT_rect.topleft = [85, 248]
    screen.blit(GT_text, GT_rect)

    GT_font1 = pygame.font.SysFont('SimHei', 36)
    GT_text1 = GT_font1.render('总得分:' + str(score), True, (46, 220, 68))
    GT_rect1 = GT_text1.get_rect()
    GT_rect1.topleft = [145, 348]
    screen.blit(GT_text1, GT_rect1)

    GT_font2 = pygame.font.SysFont('SimHei', 20)
    GT_text2 = GT_font2.render('按键 1：再来一局', True, (255, 67, 241))
    GT_rect2 = GT_text2.get_rect()
    GT_rect2.topleft = [145, 448]
    screen.blit(GT_text2, GT_rect2)

    GT_text3 = GT_font2.render('按键 2：结束游戏', True, (255, 67, 241))
    GT_rect3 = GT_text3.get_rect()
    GT_rect3.topleft = [145, 488]
    screen.blit(GT_text3, GT_rect3)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_2:
                    moveImg(imgArray)
                    pygame.quit()
                    exit()
                elif event.key == pygame.K_1:
                    play()

#开始游戏
pygame.init()
screen = pygame.display.set_mode([460, 720])
pygame.display.set_caption('菊花侠大战桃花怪')
# 开始游戏
screen.blit(pygame.image.load(bg1), (0, 0))
GS_font = pygame.font.SysFont('SimHei', 28)
GS_font.set_bold(200)
GS_text = GS_font.render('菊花侠大战桃花怪!', True, (243, 80, 68))
GS_rect = GS_text.get_rect()
GS_rect.topleft = [95, 268]
screen.blit(GS_text, GS_rect)

GS_font1 = pygame.font.SysFont('SimHei', 22)
GS_text1 = GS_font1.render('按键 1：开始游戏', True, (255, 67, 241))
GS_rect1 = GS_text1.get_rect()
GS_rect1.topleft = [125, 348]
screen.blit(GS_text1, GS_rect1)

GS_text2 = GS_font1.render('按键 2：退出游戏', True, (255, 67, 241))
GS_rect2 = GS_text2.get_rect()
GS_rect2.topleft = [125, 388]
screen.blit(GS_text2, GS_rect2)

GS_font2 = pygame.font.SysFont('SimHei', 16)
GS_text3 = GS_font2.render('提示：Q 普攻 W 技能1 R 技能2 ', True, (70, 70, 70))
GS_rect3 = GS_text3.get_rect()
GS_rect3.topleft = [106, 438]
screen.blit(GS_text3, GS_rect3)
pygame.display.update()
# 判断
while True:
    for event1 in pygame.event.get():
        if event1.type == KEYDOWN:
            if event1.key == pygame.K_2:
                moveImg(imgArray)
                pygame.quit()
                exit()
                break
            elif event1.key == pygame.K_1:
                play()


