import pygame
from pygame import *
from primer_player import Player
from blocks import Platform

# Объявляем переменные
WIN_WIDTH = 800  # Ширина создаваемого окна
WIN_HEIGHT = 640  # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = (0, 0, 255)
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = (255, 0, 0)

pygame.init()  # Инициация PyGame, обязательная строчка
clock = pygame.time.Clock()

hero = Player(55, 55)  # создаем героя по (x,y) координатам


def main():
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("Cyber carnage")  # Пишем в шапку
    # будем использовать как фон
    entities = pygame.sprite.Group()  # Все объекты
    platforms = []  # то, во что мы будем врезаться или опираться
    entities.add(hero)
    level = [
        "-------------------------",
        "-                       -",
        "-                       -",
        "-                       -",
        "-                       -",
        "-                       -",
        "-                       -",
        "-                       -",
        "-                       -",
        "-                       -",
        "-                       -",
        "-      ----             -",
        "-      ----             -",
        "----------------        -",
        "----------------        -",
        "-------------------------",
        "-------------------------",
        "-------------------------",
        "-------------------------",
        "-------------------------"]
    up = False
    left = right = False  # по умолчанию — стоим
    pygame.draw.rect(screen, BACKGROUND_COLOR, (0, 0, WIN_WIDTH, WIN_HEIGHT))
    finished = False
    while not finished:  # Основной цикл программы
        clock.tick(30)
        pygame.draw.rect(screen, BACKGROUND_COLOR, (0, 0, WIN_WIDTH, WIN_HEIGHT))
        x = y = 0  # координаты
        for row in level:  # вся строка
            for col in row:  # каждый символ
                if col == "-":
                    pf = Platform(x, y)
                    entities.add(pf)
                    platforms.append(pf)
                    # создаем блок, заливаем его цветом и рисеум его
                    pygame.draw.rect(screen, PLATFORM_COLOR, (x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT))
                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == QUIT:
                finished = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYUP and e.key == K_UP:
                up = False
        hero.update(left, right, up, platforms)  # передвижение
        entities.draw(screen)  # отображение всего
        pygame.display.update()  # обновление и вывод всех изменений на экран


if __name__ == "__main__":
    main()
