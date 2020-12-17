import pygame


from player import Player
from Cyber_Policeman import Policeman

DISPLAY_W, DISPLAY_H = 800, 640
FPS = 60

policeman = Policeman()
cat = Player()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        self.current_image = pygame.image.load("smoll_laser.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x+cat.rect.width//2, y+cat.rect.height/2)
        self.speedy = 1

    def update(self):
        self.rect.x += self.speedy
        # убить, если он заходит за верхнюю часть экрана
