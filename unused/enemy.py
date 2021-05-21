import pygame
import random
import Player
from projectile import Bullet

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.face = pygame.Surface((24,24))
        self.face.fill((255,0,0))
        self.rect = self.face.get_rect()
        self.speedy = random.randrange(5, 20)
 
    def move(self):
        self.rect.y += self.speedy

    
    def shoot(self):
        bullet = Bullet(self.bullet_image, self.rect.centerx, self.rect.top)
        self.sprites.add(bullet)
        self.bullets.add(bullet)
    
    
