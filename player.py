import pygame
import projectill
from projectill import Bullet,Spread
import enemii
import random
from pygame.locals import (
        K_UP,
        K_DOWN,
        K_LEFT,
        K_RIGHT,
        K_RETURN,
        K_w,
        K_a,
        K_s,
        K_d,
        K_x,
        #KMOD_NONE,
        #KMOD_SHIFT,
        K_LSHIFT,
        K_RSHIFT,
)

class Player(pygame.sprite.Sprite):
    def __init__(self,area):
        self._layer = 7
        super(Player,self).__init__()
        self.face = pygame.Surface((32,32))
        self.face.fill((255,210,255))
        self.rec = self.face.get_rect()
        self.area = area
        self.rec.centerx = 500
        self.rec.centery = 964
        self.pullets = pygame.sprite.Group()
        self.pread = pygame.sprite.Group()
        self.hold = 2
        self.defhold = self.hold
        self.slowed = False
        self.upgrades = 0
        self.spreads = 512
        self.shots = 512

    def normal_movement(self, usr_in):
        if(usr_in[K_RSHIFT] or usr_in[K_LSHIFT]):
            self.slow_movement(usr_in)
        else:
            if self.slowed:
                self.face = pygame.transform.scale(self.face,(32,32))
                self.slowed = False
            if (usr_in[K_UP] or usr_in[K_w]):
                self.rec.move_ip(0,-9)
            if (usr_in[K_DOWN] or usr_in[K_s]):
                self.rec.move_ip(0,9)
            if (usr_in[K_LEFT] or usr_in[K_a]):
                self.rec.move_ip(-9,0)
            if (usr_in[K_RIGHT] or usr_in[K_d]):
                self.rec.move_ip(9,0)
            if (usr_in[K_x] or usr_in[K_RETURN]):
                if self.hold == 0:
                    if (len(self.pullets) <= self.shots and len(self.pread) < self.spreads):
                        self.pread.add(Spread(self.rec.x+17,self.rec.y,90))
                        self.pread.add(Spread(self.rec.x+17,self.rec.y,93))
                        self.pread.add(Spread(self.rec.x+17,self.rec.y,87))
                        #self.pread.add(Spread(self.rec.x+5,self.rec.y,-2,8))
                        #self.pread.add(Spread(self.rec.x+25,self.rec.y,2,8))
                        #self.pread.add(Spread(self.rec.x+3,self.rec.y,-3,6))
                        #self.pread.add(Spread(self.rec.x+31,self.rec.y,3,6))

                        self.hold = self.defhold+6
                else:
                    self.hold -= 1
            self.rec.clamp_ip(self.area)

    def slow_movement(self, usr_in):
        if self.slowed is False:
            self.face = pygame.transform.scale(self.face,(16,16))
            self.slowed = True
        if (usr_in[K_UP] or usr_in[K_w]):
            self.rec.move_ip(0,-5)
        if (usr_in[K_DOWN] or usr_in[K_s]):
            self.rec.move_ip(0,5)
        if (usr_in[K_LEFT] or usr_in[K_a]):
            self.rec.move_ip(-5,0)
        if (usr_in[K_RIGHT] or usr_in[K_d]):
            self.rec.move_ip(5,0)
        if (usr_in[K_x] or usr_in[K_RETURN]):
            if self.hold == 0:
                if (len(self.pullets) <= self.shots and len(self.pread) < self.spreads):
                    self.pullets.add(Bullet(self.rec.x+12,self.rec.y,90,False))
                    self.hold = self.defhold+3
            else:
                self.hold -= 1
        self.rec.clamp_ip(self.area)

    def deaded(self):
        self.rec.x = 500
        self.rec.y = 964
        '''
        self.upgrades = int(self.upgrades/2)
        self.shots = int(self.shots/2)
        self.spreads = int(self.spreads/2)
        self.defhold = self.defhold + 22
        if self.shots < 10:
            self.shots = 10
        if self.spreads < 10:
            self.spreads = 10
        if self.defhold > 15:
            self.defhold = 15
        if self.upgrades > 10:
            a = int(self.upgrades/2)
            self.upgrades -= a
            if self.shots > a:
                self.shots -= a
            if self.spreads > a:
                self.spreads -= a
            if self.defhold-a < 20:
                self.defhold += a
        '''


    def collision(self, enemii = None, projectill = None):
        if(enemii is not None and self.rec.colliderect(enemii.rect)):
            enemii.kill()
            self.deaded()
            return True
        elif(projectill is not None and self.rec.colliderect(projectill.rect)):
            projectill.kill()
            self.deaded()
            return True
        else:
            return False


