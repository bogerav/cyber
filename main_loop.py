import pygame
from player import Player
from Cyber_Policeman import Policeman
from camera import *
from game import Game
import random

################################# LOAD UP A BASIC WINDOW AND CLOCK #################################
pygame.init()
pygame.display.set_caption("CYBER CARNAGE")
DISPLAY_W, DISPLAY_H = 1280, 720
canvas = pygame.Surface((1920, 1200))
window = pygame.display.set_mode(((DISPLAY_W, DISPLAY_H)))
running = True
clock = pygame.time.Clock()
house = pygame.image.load('the_art_demo.png').convert()

################################# LOAD PLAYER AND CAMERA###################################
g = Game()
policeman = Policeman()
cat = Player()
camera = Camera(cat)
follow = Follow(camera, cat)
border = Border(camera, cat)
camera.setmethod(follow)
################################# GAME LOOP ##########################
while g.running:
    g.curr_menu.display_menu()
    g.game_loop()

while running:
    clock.tick(60)

    if (cat.rect.x - cat.left_border <= camera.DISPLAY_W*(1/4)) or (cat.right_border - cat.rect.x <= camera.DISPLAY_W *(3/4) + cat.rect.w / 2):
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
            elif event.key == pygame.K_z and cat.JUMP == False:
                cat.JUMP = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                cat.LEFT_KEY = False
            elif event.key == pygame.K_RIGHT:
                cat.RIGHT_KEY = False



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        temp = random.randint(0, 1)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                cat.LEFT_KEY, cat.FACING_LEFT = True, True
            elif event.key == pygame.K_RIGHT:
                cat.RIGHT_KEY, cat.FACING_LEFT = True, False
            elif event.key == pygame.K_z and cat.JUMP == False:
                cat.JUMP = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                cat.LEFT_KEY = False
            elif event.key == pygame.K_RIGHT:
                cat.RIGHT_KEY = False

    ################################# UPDATE/ Animate SPRITE #################################
    policeman.update()
    cat.update()
    camera.scroll()
    policeman.update()
    ################################# UPDATE WINDOW AND DISPLAY #################################

    canvas.blit(house, (0 - camera.offset.x, 0 - camera.offset.y))
    canvas.blit(cat.current_image,(cat.rect.x - camera.offset.x, cat.rect.y - camera.offset.y))
    canvas.blit(policeman.current_image, (policeman.rect.x, policeman.rect.y))
    window.blit(canvas, (0, -400))
    pygame.display.update()










