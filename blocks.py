from pygame import *
import os


PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"
ICON_DIR = os.path.dirname(__file__)


class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
        self.current_image = image.load("thisisit.jpg")


class Escape(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        portal_surf = image.load('portal.bmp')
        portal_surf.set_colorkey((255, 255, 255))
        self.current_image = portal_surf
        