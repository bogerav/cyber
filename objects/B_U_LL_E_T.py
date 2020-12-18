import pygame


from objects.player import Player
from objects.police import Policeman
from objects.blocks import Platform

DISPLAY_W, DISPLAY_H = 1024, 640
FPS = 60

policeman = Policeman(0,0)
cat = Player(0,0)
block = Platform


class Bullet(pygame.sprite.Sprite):
    def __init__(self, kind, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.kind = kind
        self.image = pygame.Surface((10, 20))
        self.current_image = pygame.image.load('../cyber/sprites/smoll_laser.png')
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x+kind.rect.width//2, y+kind.rect.height/2)
        if self.kind.FACING_LEFT:
            self.speedy = -10
        else:
            self.speedy = 10

    def update(self):
        self.rect.x += self.speedy
        if self.rect.x > DISPLAY_W or self.rect.x < 0:
            self.kill()
        # убить, если он заходит за верхнюю часть экрана

    def collision(self, kind, x, y):
        if -5 < ((x + kind.rect.width / 2) - (self.rect.x + self.rect.w / 2)) < 5:
            if -35 < ((y + kind.rect.height / 2) - (self.rect.y + self.rect.h / 2)) < 35:
                if isinstance(kind, Policeman):
                    kind.kill()
                    self.kill()
                elif isinstance(kind, Player):
                    kind.lives -= 1
                    self.kill()
        elif -32 < ((x + kind.rect.width / 2) - (self.rect.x + self.rect.w / 2)) < 32:
            if -16 < ((y + kind.rect.height / 2) - (self.rect.y + self.rect.h / 2)) < 16:
                if isinstance(kind, block):
                    self.kill()

                


