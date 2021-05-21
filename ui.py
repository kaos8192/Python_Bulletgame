import pygame
import random

class Ui(pygame.sprite.Sprite):
    def __init__(self,disp):
        super(Ui,self).__init__()
        self.ui = pygame.Surface((280,1024))
        self.ui.fill((255,255,255))
        self.disp = disp
        self.rect = self.ui.get_rect()
        self.rect.x = 1000
        self.rect.y = 0

    def texty_text(self,score,lives):
        self.ui.fill((255,255,255))
        font1 = pygame.font.SysFont("lato", 24)
        text_surf1 = font1.render("Score: "+str(score),True,(0,0,0))
        textrec1 = text_surf1.get_rect()
        textrec1.midtop = (140,140)
        self.ui.blit(text_surf1, textrec1)

        font2 = pygame.font.SysFont("lato", 24)
        text_surf2 = font2.render("___________",True,(0,0,0))
        textrec2 = text_surf2.get_rect()
        textrec2.midtop = (140,175)
        self.ui.blit(text_surf2, textrec2)

        font3 = pygame.font.SysFont("lato", 24)
        text_surf3 = font3.render("Lives: "+str(lives),True,(0,0,0))
        textrec3 = text_surf3.get_rect()
        textrec3.midtop = (140,220)
        self.ui.blit(text_surf3, textrec3)


