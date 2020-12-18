import pygame


from spritesheet import Spritesheet
import blocks

DISPLAY_W, DISPLAY_H = 800, 640
FPS = 60
MOVE_SPEED = 5
WIDTH = 20
HEIGHT = 64
JUMP_POWER = 10
GRAVITY = 0.35 # Сила, которая будет тянуть нас вниз


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.startX = x
        self.startY = y
        self.LEFT_KEY, self.RIGHT_KEY, self.FACING_LEFT, self.JUMP = False, False, False, False
        self.load_frames()
        self.rect = self.idle_frames_left[0].get_rect()
        self.rect.midbottom = (200, 900)
        self.current_frame = 0
        self.last_updated = 0
        self.xvel = 0
        self.yvel = 0
        self.state = 'idle'
        self.current_image = self.idle_frames_left[0]
        self.left_border, self.right_border = 0, 1920
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)
        self.onGround = False  # На земле ли я?
        self.lives = 3
        self.shoot = False
        self.counter = 0

    def update(self, left, right, up, platforms):
        if up:
            if self.onGround:  # прыгаем, только когда можем оттолкнуться от земли
                self.yvel = -JUMP_POWER
        if left:
            self.xvel = -MOVE_SPEED  # Лево = x- n

        if right:
            self.xvel = MOVE_SPEED  # Право = x + n

        if not (left or right):  # стоим, когда нет указаний идти
            self.xvel = 0
        if not self.onGround:
            self.yvel += GRAVITY

        if self.lives == 0:
            self.kill()
            quit()

        self.onGround = False;  # Мы не знаем, когда мы на земле((
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)


        self.rect.x += self.xvel  # переносим свои положение на xvel
        temp = self.collide(self.xvel, 0, platforms)
        self.set_state()
        self.animate()
        return temp

    def collide(self, xvel, yvel, platforms):
        temp = False
        for p in platforms:
            if pygame.sprite.collide_rect(self, p): # если есть пересечение платформы с игроком
                if isinstance(p, blocks.Escape):  # если коснулись п
                    self.counter += 1  # победили!!!
                    temp = True
                    break
                if xvel > 0:                      # если движется вправо
                    self.rect.right = p.rect.left # то не движется вправо

                if xvel < 0:                      # если движется влево
                    self.rect.left = p.rect.right # то не движется влево

                if yvel > 0:                      # если падает вниз
                    self.rect.bottom = p.rect.top # то не падает вниз
                    self.onGround = True          # и становится на что-то твердое
                    self.yvel = 0                 # и энергия падения пропадает

                if yvel < 0:                      # если движется вверх
                    self.rect.top = p.rect.bottom # то не движется вверх
                    self.yvel = 0                 # и энергия прыжка пропадает
        return temp

    def set_state(self):
        self.state = ' idle'
        if self.xvel > 0:
            self.state = 'moving right'
        elif self.xvel < 0:
            self.state = 'moving left'
        elif self.shoot and self.FACING_LEFT == False:
            self.state = 'shooting right'
        elif self.shoot and self.FACING_LEFT == True:
            self.state = 'shooting left'



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
        elif self.state == 'moving left' or self.state == 'moving right':
            if now - self.last_updated > 100:
                self.last_updated = now
                self.current_frame = (self.current_frame + 1) % len(self.walking_frames_left)

                if self.state == 'moving left':
                    if self.shoot:
                        self.current_image = self.shooting_frame_left
                        self.shoot = False
                    else:
                        self.current_image = self.walking_frames_left[self.current_frame]

                elif self.state == 'moving right':
                    if self.shoot:
                        self.current_image = self.shooting_frame_right
                        self.shoot = False
                    else:
                        self.current_image = self.walking_frames_right[self.current_frame]
        else:
            if self.state == 'shooting right':
                self.current_image = self.shooting_frame_right
                self.shoot = False
            if self.state == 'shooting left':
                self.current_image = self.shooting_frame_left
                self.shoot = False

    def load_frames(self):
        my_spritesheet = Spritesheet('hero_run.png')
        my_one_marv_spritesheet = Spritesheet('marv_deadshot.png')

        # pygame.image.load('MY_IMAGE_NAME.png').convert()
        self.idle_frames_right = [my_spritesheet.parse_sprite("poppy_idle1.png")]
        self.walking_frames_right = [my_spritesheet.parse_sprite("poppywalk1.png"),
                                    my_spritesheet.parse_sprite("poppywalk2.png"),
                                    my_spritesheet.parse_sprite("poppywalk3.png"),
                                    my_spritesheet.parse_sprite("poppywalk4.png"),
                                    my_spritesheet.parse_sprite("poppywalk5.png"),
                                    my_spritesheet.parse_sprite("poppywalk6.png"),
                                    my_spritesheet.parse_sprite("poppywalk7.png"),
                                    my_spritesheet.parse_sprite("poppywalk8.png"),
                                    my_spritesheet.parse_sprite("poppywalk9.png")]

        self.shooting_frame_right = my_one_marv_spritesheet.parse_sprite("marv_frame_shot_1.png")

        self.shooting_frame_left = pygame.transform.flip(self.shooting_frame_right, True, False)
        self.idle_frames_left = []
        for frame in self.idle_frames_right:
            self.idle_frames_left.append(pygame.transform.flip(frame, True, False))
        self.walking_frames_left = []
        for frame in self.walking_frames_right:
            self.walking_frames_left.append(pygame.transform.flip(frame, True, False))




