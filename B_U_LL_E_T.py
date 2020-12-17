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
            self.speedy = -10
        else:
            self.speedy = 10

    def update(self):
            self.rect.x += self.speedy
        # убить, если он заходит за верхнюю часть экрана
