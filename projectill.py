import pygame
import random
import player
import math


class Bullet(pygame.sprite.Sprite):
    def __init__(self, centerx, centery,angle = 90, is_enemy = True,enemy_t = 0):
        self._layer = 7
        super(Bullet,self).__init__()
        self.face = pygame.Surface((8,8))
        self.face.fill((255,220,220))
        self.face.set_alpha(175)
        self.rect = self.face.get_rect()
        self.px = centerx
        self.pfx = centery
        self.rect.center = (self.px,self.pfx)
        self.angle = angle
        self.golden_ratio = (1 + 5 ** 0.5)/2
        self.speedx = math.cos(self.angle)
        self.speedy = math.sin(self.angle)
        #print(self.speedx)
        #print(self.speedy)

    def efire(self):
        if True:
            self.px -= int((self.speedx / 0.5)*2.03)
            self.pfx -= int((self.speedy / 0.5)*2.03)
            #self.px += int(math.tan((math.pi)*(self.speedx * self.golden_ratio)))
            #self.pfx += int(math.e*((math.pi)*(self.speedy * self.golden_ratio)))
            #print(self.px)
            #print(self.pfx)
            self.rect.center = (self.px,self.pfx)
            if (self.rect.center[0] > 1040 or self.rect.center[0] < -10 or self.rect.center[1] > 1030 or self.rect.center[1] < -10):
                self.kill()

    def erestrifire(self):
        self.px += int(math.e * math.sin(math.pi * self.speedx * (self.golden_ratio*2)))
        yfact = int((math.e*2)*math.sin(math.pi * self.speedy * (self.golden_ratio*2)))
        if yfact > 0:
            yfact = yfact * -1
        elif yfact == 0:
            yfact = -1.45
        elif yfact <= -4:
            yfact += 0.7734

        self.pfx -= yfact

        #print(self.pfx)
        self.rect.center = (self.px,self.pfx)
        if (self.rect.center[0] > 1040 or self.rect.center[0] < -10 or self.rect.center[1] > 1030 or self.rect.center[1] < -10):
            self.kill()

    def pfire(self):
        self.pfx -= 10
        self.rect.center = (self.px,self.pfx)
        if (self.rect.center[0] > 1040 or self.rect.center[0] < -10 or self.rect.center[1] > 1030 or self.rect.center[1] < -10):
            self.kill()

    def collision(self, projectill):
        if(projectill is not None and self.rect.colliderect(projectill.rect)):
            projectill.kill()
            self.kill()

class Dir_bullet(pygame.sprite.Sprite):
    def __init__(self, center, bottom, x, y):
        self._layer = 7
        super(Dir_bullet,self).__init__()
        self.face = pygame.Surface((8,8))
        self.face.fill((255,220,220))
        self.rect = self.face.get_rect()
        self.rect.center = (center, bottom)
        self.speedx = x
        self.speedy = y

    def fire(self):
        self.rect.center[1] -= self.speedy
        self.rect.center[0] -= self.speedx



class Spread(pygame.sprite.Sprite):
    def __init__(self, center, bottom,angle):
        self._layer = 7
        super(Spread,self).__init__()
        self.face = pygame.Surface((6,7))
        self.face.fill((255,220,220))
        self.rect = self.face.get_rect()
        self.px = center
        self.pfx = bottom
        self.rect.center = (self.px,self.pfx)
        self.angle = angle



    def plrbeam(self):
        if self.angle < 90:
            self.px += math.sin(self.angle)
        elif self.angle > 90:
            self.px -= math.sin(self.angle)
        self.pfx -= 14
        self.rect.center = (self.px,self.pfx)
        if self.rect.y < -5:
            self.kill()
        if self.rect.x < -5:
            self.kill()
        if self.rect.x > 1040:
            self.kill()

'''
    def ebeam(self,bullets):
        count = 0
        while count < 4:
            self.rect.y -= self.yspeed+2
            if self.xspeed > 0:
                self.rect.x += self.xspeed+2
            elif self.xspeed < 0:
                self.rect.x += self.xspeed-2
            else:
                self.rect.x = self.rect.x

        if self.rect.y < -5:
            self.kill()
        if self.rect.x < -5:
            self.kill()
        if self.rect.x > 1229:
            self.kill()
'''
