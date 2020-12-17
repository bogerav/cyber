import pygame


from player import Player
from Cyber_Policeman import Policeman

DISPLAY_W, DISPLAY_H = 800, 640
FPS = 60

policeman = Policeman()
cat = Player()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, kind, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.kind = kind
        self.image = pygame.Surface((10, 20))
        self.current_image = pygame.image.load("smoll_laser.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x+kind.rect.width//2, y+kind.rect.height/2)
        if self.kind.FACING_LEFT:
            self.speedy = -1
        else:
            self.speedy = 1

    def update(self):
            self.rect.x += self.speedy
        # убить, если он заходит за верхнюю часть экрана


    def collision(self, x, y):
        if -30 < ((x + 50 / 2) - (self.rect.x + self.rect.w / 2)) < 30:
            if -30 < ((y + 20 / 2) - (self.rect.y + self.rect.h / 2)) < 30:
                print("жмыхнуло")
                


