import pygame
from pygame import *
from newplayer import Player
from blocks import Platform, Escape
import pygame
from newcamera import Camera
from game import Game
from newpolice import Policeman
from B_U_LL_E_T import Bullet
import json

# Объявляем переменные
pygame.init()
pygame.display.set_caption("CYBER CARNAGE")
DISPLAY_W, DISPLAY_H = 800, 640
DISPLAY = (DISPLAY_W, DISPLAY_H)  # Группируем ширину и высоту в одну переменную

clock = pygame.time.Clock()

background_image = image.load("blue_city.jpg")
heart_image = pygame.image.load("heart.png")
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = (255, 255, 255)



hero = Player(55, 1000)
g = Game()

bullets = pygame.sprite.Group()



def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + DISPLAY_W / 2, -t + DISPLAY_H / 2

    l = min(0, l)  # Не движемся дальше левой границы
    l = max(-(camera.width - DISPLAY_W), l)  # Не движемся дальше правой границы
    t = max(-(camera.height - DISPLAY_H), t)  # Не движемся дальше нижней границы
    t = min(0, t)  # Не движемся дальше верхней границы

    return Rect(l, t, w, h)


def level_1():
    running = True
    levelnew = True
    counter = 0
    while g.running:
        g.curr_menu.display_menu()
        g.game_loop()
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Cyber carnage")  # Пишем в шапку
    bg = Surface(DISPLAY)  # Создание видимой поверхности
    # будем использовать как фон
    bg.blit(background_image, (0,0))  # Заливаем поверхность сплошным цветом
    while levelnew < 5:
        if levelnew:

            hero = Player(55, 900)  # создаем героя по (x,y) координатам
            left = right = False  # по умолчанию - стоим
            up = False

            entities = pygame.sprite.Group()  # Все объекты
            policemen = pygame.sprite.Group()
            platforms = []  # то, во что мы будем врезаться или опираться


            entities.add(hero)

            with open ('all_levels') as f:
                data = json.load(f)
                level1 = data['level1']
                level2 = data['level2']
                level3 = data['level3']
                level4 = data['level4']

            levels_list = [level1, level2, level3, level4]

            level = [
                "----------------------------------",
                "-                                -",
                "-                                -",
                "-                               E-",
                "-              -----             -",
                "-                       ----------",
                "-                                -",
                "-------                          -",
                "-                                -",
                "-          ---                   -",
                "-                  P             -",
                "-                -----           -",
                "-                                -",
                "-                  P             -",
                "-------    -----------------------",
                "-                                -",
                "-       P                        -",
                "-     -----                      -",
                "-                                -",
                "-                 -----          -",
                "-                                -",
                "-                                -",
                "-          -----                 -",
                "-                                -",
                "-                      P         -",
                "-                    -----       -",
                "-        ------                  -",
                "-                                -",
                "-                                -",
                "----------------------------------"]

            timer = pygame.time.Clock()
            x = y = 0  # координаты
            for row in levels_list[counter]:  # вся строка
                for col in row:  # каждый символ
                    if col == "-":
                        pf = Platform(x, y)
                        entities.add(pf)
                        platforms.append(pf)

                    elif col == "E":
                        esc = Escape(x, y)
                        entities.add(esc)
                        platforms.append(esc)

                    elif col == "P":
                        pol = Policeman(x, y)
                        policemen.add(pol)
                        entities.add(pol)

                    x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
                y += PLATFORM_HEIGHT  # то же самое и с высотой
                x = 0  # на каждой новой строчке начинаем с нуля

            total_level_width = len(level[0]) * PLATFORM_WIDTH  # Высчитываем фактическую ширину уровня
            total_level_height = len(level) * PLATFORM_HEIGHT  # высоту
            camera = Camera(camera_configure, total_level_width, total_level_height)
            bullets = pygame.sprite.Group()
            levelnew = False

        while running:  # Основной цикл программы
            timer.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        left, hero.FACING_LEFT = True, True
                    elif event.key == pygame.K_RIGHT:
                        right, hero.FACING_LEFT = True, False
                    elif event.key == pygame.K_UP and hero.JUMP == False:
                        up = True
                    elif event.key == pygame.K_x:
                        hero.shoot = True
                        bullet = Bullet(hero, hero.rect.x, hero.rect.y)
                        bullets.add(bullet)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        left = False
                    elif event.key == pygame.K_RIGHT:
                        right = False
                    elif event.key == pygame.K_UP:
                        up = False

            screen.blit(bg, (0, 0))  # Каждую итерацию необходимо всё перерисовывать


            for bullet in bullets:
                bullet.update()
                for ent in entities:
                    bullet.collision(ent, ent.rect.x, ent.rect.y)
                screen.blit(bullet.current_image, camera.apply(bullet))


            camera.update(hero)  # центризируем камеру относительно персонажа
            if hero.update(left, right, up, platforms) == True:
                levelnew = True
                counter += 1
                break
            for pol in policemen:
                pol.update(False, False, False, platforms)
                if pol.see_pl(hero):
                    bullet = Bullet(pol, pol.rect.x, pol.rect.y)
                    bullets.add(bullet)
            # entities.draw(screen) # отображение
            for e in entities:
                screen.blit(e.current_image, camera.apply(e))
            if hero.lives == 3:
                screen.blit(heart_image, (100, 50))
                screen.blit(heart_image, (150, 50))
                screen.blit(heart_image, (200, 50))
            if hero.lives == 2:
                screen.blit(heart_image, (100, 50))
                screen.blit(heart_image, (150, 50))
            if hero.lives == 1:
                screen.blit(heart_image, (100, 50))


            pygame.display.update()  # обновление и вывод всех изменений на экран