import pygame
from player import Player
from camera import *

################################# LOAD UP A BASIC WINDOW AND CLOCK #################################
pygame.init()
DISPLAY_W, DISPLAY_H = 1000, 800
canvas = pygame.Surface((30000,2400))
window = pygame.display.set_mode(((DISPLAY_W,DISPLAY_H)))
running = True
clock = pygame.time.Clock()
house = pygame.image.load('m_merged_2.png').convert()

################################# LOAD PLAYER AND CAMERA###################################
cat = Player()
camera = Camera(cat)
follow = Follow(camera,cat)
border = Border(camera,cat)
auto = Auto(camera,cat)
camera.setmethod(follow)
################################# GAME LOOP ##########################
while running:
    clock.tick(60)

    if (cat.rect.x - cat.left_border <= camera.DISPLAY_W*(1/10)) or (cat.right_border - cat.rect.x <= camera.DISPLAY_W *(9/10) + cat.rect.w / 2):
        camera.setmethod(border)
    else:
        camera.setmethod(follow)
    ################################# CHECK PLAYER INPUT #################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                cat.LEFT_KEY, cat.FACING_LEFT = True, True
            elif event.key == pygame.K_RIGHT:
                cat.RIGHT_KEY, cat.FACING_LEFT = True, False
            elif event.key == pygame.K_1:
                camera.setmethod(follow)
            elif event.key == pygame.K_2:
                camera.setmethod(auto)
            elif event.key == pygame.K_3:
                camera.setmethod(border)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                cat.LEFT_KEY = False
            elif event.key == pygame.K_RIGHT:
                cat.RIGHT_KEY = False

    ################################# UPDATE/ Animate SPRITE #################################
    cat.update()
    camera.scroll()
    ################################# UPDATE WINDOW AND DISPLAY #################################
    canvas.blit(house, (0 - camera.offset.x, 0 - camera.offset.y))
    canvas.blit(cat.current_image,(cat.rect.x - camera.offset.x, cat.rect.y - camera.offset.y))
    window.blit(canvas, (0, -1400))
    pygame.display.update()









