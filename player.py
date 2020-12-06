import pygame
from spritesheet import Spritesheet

DISPLAY_W, DISPLAY_H = 1280, 720
FPS = 60


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.LEFT_KEY, self.RIGHT_KEY, self.FACING_LEFT, self.JUMP = False, False, False, False
        self.load_frames()
        self.rect = self.idle_frames_left[0].get_rect()
        self.rect.midbottom = (200, 900)
        self.current_frame = 0
        self.last_updated = 0
        self.velocity_x = 0
        self.velocity_y = 10
        self.state = 'idle'
        self.current_image = self.idle_frames_left[0]
        self.left_border, self.right_border = 0, 1920
        self.ground_y = 900
        self.box = pygame.Rect(self.rect.x, self.rect.y, self.rect.w * 2, self.rect.h)
        self.box.center = self.rect.center
        self.passed = False

    def draw(self, display):
        display.blit(self.current_image, self.rect)

    def update(self):
        self.velocity_x = 0
        if self.JUMP:
            self.rect.y -= self.velocity_y
            self.velocity_y -= 1
            if self.velocity_y < -10:
                self.JUMP = False
                self.velocity_y = 10
        if self.LEFT_KEY:
            self.velocity_x = -5
        elif self.RIGHT_KEY:
            self.velocity_x = 5
        self.rect.x += self.velocity_x
        if self.velocity_x == 0 and self.passed:
            self.passed = False
            self.box.center = self.rect.center
        if self.rect.x > self.right_border - self.rect.w:
            self.rect.x = self.right_border - self.rect.w
        elif self.rect.x <= self.left_border:
            self.rect.x = self.left_border
        self.set_state()
        self.animate()
        if self.rect.left > self.box.left and self.rect.right < self.box.right:
            pass
        else:
            self.passed = True
            if self.rect.left > self.box.left:
                self.box.left += self.velocity_x
            elif self.rect.right < self.box.right:
                self.box.left += self.velocity_x

    def set_state(self):
        self.state = ' idle'
        if self.velocity_x > 0:
            self.state = 'moving right'
        elif self.velocity_x < 0:
            self.state = 'moving left'

    def animate(self):
        now = pygame.time.get_ticks()
        if self.state == ' idle':
            if now - self.last_updated > 200:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.idle_frames_left)
                if self.FACING_LEFT:
                    self.current_image = self.idle_frames_left[self.current_frame]
                elif not self.FACING_LEFT:
                    self.current_image = self.idle_frames_right[self.current_frame]
        else:
            if now - self.last_updated > 100:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.walking_frames_left)
                if self.state == 'moving left':
                    self.current_image = self.walking_frames_left[self.current_frame]
                elif self.state == 'moving right':
                    self.current_image = self.walking_frames_right[self.current_frame]

    def load_frames(self):
        my_spritesheet = Spritesheet('hero_run.png')
        # pygame.image.load('MY_IMAGE_NAME.png').convert()
        self.idle_frames_right = [my_spritesheet.parse_sprite("poppy_idle1.png")]
        self.walking_frames_right = [my_spritesheet.parse_sprite("poppywalk1.png"),
                                    my_spritesheet.parse_sprite("poppywalk2.png"),
                                    my_spritesheet.parse_sprite("poppywalk3.png"),
                                    my_spritesheet.parse_sprite("poppywalk4.png"),
                                    my_spritesheet.parse_sprite("poppywalk5.png"),
                                    my_spritesheet.parse_sprite("poppywalk6.png"),
                                    my_spritesheet.parse_sprite("poppywalk7.png"),
                                    my_spritesheet.parse_sprite("poppywalk8.png")]
        self.idle_frames_left = []
        for frame in self.idle_frames_right:
            self.idle_frames_left.append(pygame.transform.flip(frame, True, False))
        self.walking_frames_left = []
        for frame in self.walking_frames_right:
            self.walking_frames_left.append(pygame.transform.flip(frame, True, False))

