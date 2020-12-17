import pygame


from player import Player
from Cyber_Policeman import Policeman

DISPLAY_W, DISPLAY_H = 1280, 720
FPS = 60

policeman = Policeman()
cat = Player()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.current_image = pygame.image.load("smoll_laser.png")
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.bottom < 0:
            self.kill()
