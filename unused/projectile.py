class Bullet(pygame.sprite.Sprite):
    def __init__(self, bullet_image, x, y):
        super().__init__()
        self.image = pygame.transform.scale(bullet_image, (8, 23))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        # bullet position is according the player position
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -15
 
    def update(self):
        self.rect.y += self.speedy
 
        if self.rect.bottom < 35:
            self.kill()
