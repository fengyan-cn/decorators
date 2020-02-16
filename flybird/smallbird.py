import pygame
from pygame.locals import *
import random
#首先要有三个操作对象:鸟、障碍物、地面
#画布长款
caption_width = 300
caption_height = 600
game_title = '牛逼的zhou'
speed = 10
space = 140
#障碍物长宽
obstacle_width = 80
obstacle_height = 380
#地板长宽
floor_width = caption_width
floor_height = 100
#主角大小
hero_width = 20
hero_height =20
score = 0
#设置障碍物这个对象
class Obstacle(pygame.sprite.Sprite):
    #根据change判断障碍物是否翻转并且设置相应位置
    def __init__(self,change,left,top):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('D:\\learnerZhou\\smallgame\\小游戏\\障碍物.PNG').convert_alpha()
        self.image = pygame.transform.scale(self.image,(obstacle_width,obstacle_height))
        self.rect = self.image.get_rect()
        self.rect.left = left
        if change:
            #通过flip方法对障碍物进行翻转
            self.image = pygame.transform.flip(self.image,False,True)
            #通过top位置改变长度
            self.rect.top = -(self.rect.bottom - top)
        else:
            self.rect.top = caption_height - top
    #不断改变障碍物的位置并且刷新
    def update(self):
        self.rect.left -= speed
#设置主角这个对象
class Hero(pygame.sprite.Sprite):
    def __init__(self,top = 0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('D:\\learnerZhou\\smallgame\\小游戏\\那个鸟.PNG').convert_alpha()
        self.image = pygame.transform.scale(self.image,(hero_width,hero_height))
        self.rect = self.image.get_rect()
        self.rect.left = caption_width / 2 - hero_width
        self.rect.top = caption_height /2 - hero_height - top
        self.speed = speed
    def update(self):
        self.speed += 1
        self.rect.top += self.speed
    def fly(self):
        self.speed = -speed
#设计地板这个对象
class Floor(pygame.sprite.Sprite):
    def __init__(self,left):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('D:\\learnerZhou\\smallgame\\小游戏\\地板.PNG').convert_alpha()
        self.image = pygame.transform.scale(self.image,(floor_width,floor_height))

        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = caption_height - floor_height
#因为要不断实例化障碍物，所以将他们封装成方法
def generate_Obstacle(left):
        top = random.randint(100,300)
        #实例化出两个黄瓜
        obstacle = Obstacle(False,left,top)
        obstacle_changed = Obstacle(True,left,caption_height - top - space) #space是两个障碍物之间的间隙,也可以叫生存空间
        return obstacle,obstacle_changed
def go_die():
        caption.blit(pygame.image.load(''),(0,0))
        pygame.display.update()
if __name__ == '__main__':
    #初始化pygame
    pygame.init()
    game_font = pygame.font.SysFont('windows',16,True)
    caption = pygame.display.set_mode((caption_width,caption_height))
    pygame.display.set_caption(game_title)
    background = pygame.image.load('D:\\learnerZhou\\smallgame\\小游戏\\蓝天白云.PNG')
    #缩放自动适应画布大小
    background = pygame.transform.scale(background,(caption_width,caption_height))
    #实例化主角
    hero_group = pygame.sprite.Group()
    hero = Hero()
    hero_group.add(hero)
    #实例化地板
    floor_group = pygame.sprite.Group()
    floor = Floor(0)
    floor_group.add(floor)
    #实例化障碍物对象
    obstacle_group = pygame.sprite.Group()
    obstacles1 = generate_Obstacle(300)
    obstacle_group.add(obstacles1[0])
    obstacle_group.add(obstacles1[1])
    clock = pygame.time.Clock()

    while True:
        #防止障碍速度过快
        clock.tick(25)
        #把背景图画到画布上
        caption.blit(background,(0,0))
        caption.blit(game_font.render('score:%d' %score,True,[255,255,255]),[20,20])

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    hero.fly()
        #判断障碍物是不是在画布外面，如果是需要重新生成障碍物。因为要不断的实例化，所以判断的是第一个障碍物实例对象
        if obstacle_group.sprites()[0].rect.left < -(caption_width):
            obstacle_group.remove(obstacle_group.sprites())
            #生成黄瓜
            obstacles = generate_Obstacle(caption_width)
            obstacle_group.add(obstacles[0])
            obstacle_group.add(obstacles[1])
            #每经过一个障碍物就加一分
            score += 1
        #将主角、障碍物、地板加入画布并且进行更新
        hero_group.update()
        hero_group.draw(caption)
        obstacle_group.update()
        obstacle_group.draw(caption)
        floor_group.draw(caption)
        pygame.display.update()
        #检测group之间是否发生碰撞
        if pygame.sprite.groupcollide(hero_group,floor_group,False,False)\
            or pygame.sprite.groupcollide(hero_group,obstacle_group,False,False):
            pygame.quit()
            quit()


