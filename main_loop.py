from menu_and_tools.game import Game
from levels.levels import level_1

g = Game()  # инициализируем запуск игры

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()

level_1()
