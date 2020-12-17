import pygame
from player import Player
from Cyber_Policeman import Policeman
from camera import *
from game import Game
import random
from levels import level_1

################################# LOAD UP A BASIC WINDOW AND CLOCK #################################

################################# LOAD PLAYER AND CAMERA###################################
g = Game()

################################# GAME LOOP ##########################
while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
level_1()
