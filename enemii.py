import pygame
import player
import math
from projectill import Bullet,Spread

class Enemy(pygame.sprite.Sprite):
    def __init__(self,place=500,placey=-100,mv_type = 0, ft = "cc", side = "r", xspeed = 0, yspeed = 3,type_count=500, ang = -90,hpboost=1,colorr = 200, colorg = 12, colorb = 12, wait = 0, stop = 256):
        self._layer = 7
        super(Enemy,self).__init__()
        #self.golden_ratio = (1 + 5 ** 0.5)/2
        self.face = pygame.Surface((74,75))
        self.face.fill((colorr,colorg,colorb))
        self.rect = self.face.get_rect()
        self.rect.centerx = place
        self.rect.centery = placey
        self.max_bullets = type_count
        self.strt_amt = self.max_bullets
        self.hold = 0
        self.defhold = self.hold
        self.health = hpboost
        self.half = False
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.mv_type = mv_type
        self.ang = ang
        self.side = side
        self.wait = wait
        self.ft = ft
        self.stop = stop

    def move(self):
        if self.wait <= 0:
            if self.mv_type == 0:
                if (self.rect.centery <= self.stop + 54):
                    self.rect.centery += self.yspeed
                    if (self.rect.centery <= (self.stop - self.stop/9)):
                        if self.side == "r":
                            self.rect.centerx -= self.xspeed
                        else:
                            self.rect.centerx += self.xspeed

                if self.max_bullets <= 0:
                    if self.side == "r":
                        self.rect.centerx -= (4 + self.xspeed)
                        self.rect.centery -= (self.yspeed + 1)
                    else:
                        self.rect.centerx += (4 + self.xspeed)
                        self.rect.centery -= (self.yspeed + 1)
            '''
            if self.rect.centery < 215:
                self.rect.centery += self.yspeed
            else:
                if self.max_bullets != 0:
                    if self.side == "r":
                        if self.rect.right +45 >= 1000:
                            self.side = "l"
                        else:
                            self.rect.centerx += self.xspeed
                    else:
                        if self.rect.left -45 <= 0:
                            self.side = "r"
                        else:
                            self.rect.centerx -= self.xspeed
                else:
                    self.deaded()
            '''
        else:
            self.wait -= 1


    def roshoot(self,bullets):
        if self.rect.centery > self.stop-12:
            if self.max_bullets > 0:
                if self.hold == 0:
                    bullets.add(Bullet(centerx = self.rect.centerx, centery = self.rect.centery, angle = self.ang))
                    self.max_bullets -= 1
                    if self.ft == "cc":
                        if self.ang < 181:
                            self.ang += 3
                        elif self.ang >= 181:
                            self.ang = -1
                        elif self.ang > -181:
                            self.ang += -1
                        elif self.ang <= -181:
                            self.ang = 0
                        else:
                            self.ang = 0
                    else:
                        if self.ang < 181:
                            self.ang -= 1
                        elif self.ang >= 181:
                            self.ang = -1
                        elif self.ang > -181:
                            self.ang -= -3
                        elif self.ang <= -181:
                            self.ang = 0
                        else:
                            self.ang = 0
                    if (self.max_bullets == (self.strt_amt/2)):
                        if self.ft == "cc":
                            self.ft = "cw"
                        else:
                            self.ft = "cc"
                    self.hold = self.defhold

                else:
                    self.hold -= 1



            #self.bullets.add(Bullet(self.rect.centerx, self.rect.bottom))

        #for i in self.bullets:
            #i.fire()
    def deaded(self):
        self.kill()

    def collision(self, projectill = None, damage = 0):
        if(projectill is not None and self.rect.colliderect(projectill.rect)):
            self.health -= damage
            projectill.kill()
            if self.health <= 0:
                self.deaded()
                return True
            #projectill.kill()
            #self.deaded()
            return False
        else:
            return False


class Small_e(Enemy):
    def __init__(self):
        super(Small_e,self).__init__()

    def move(self):
        if self.wait <= 0:
            if self.mv_type == 0:
                if self.rect.centery < 228:
                    self.rect.centery += self.yspeed
                    if self.rect.centery >= 186:
                        if self.side == "r":
                            self.rect.centerx -= (4 + self.xspeed)
                        else:
                            self.rect.centerx += (4 + self.xspeed)
                if self.max_bullets <= 0:
                    if self.side == "r":
                        self.rect.centerx -= (4 + self.xspeed)
                        self.rect.centery -= (self.yspeed + 1)
                    else:
                        self.rect.centerx += (4 + self.xspeed)
                        self.rect.centery -= (self.yspeed + 1)




    def direct_shoot(self,bullets, playerx, playery):
        if self.rect.centery > 50:
            if self.max_bullets > 0:
                if self.hold == 0:
                    bullets.add(Dir_bullet(self.rect.centerx, self.rect.bottom,  self.x - playerx, self.y - playery))
                    self.max_bullets -= 1
                    self.hold = self.defhold
                else:
                    self.hold -= 1










