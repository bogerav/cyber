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
        self.current_image = image.load("platform.png")


class Escape(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.current_image = image.load("portal.png")
        