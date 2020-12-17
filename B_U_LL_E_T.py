import pygame

from levels import bullets
from main_loop import bullet_group, all_sprites
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
        self.image.fill("YELLOW")
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.bottom < 0:
            self.kill()

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet) #фиг его знает что это
        bullets.add(bullet)