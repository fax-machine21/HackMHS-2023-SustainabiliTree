import math, random, time

from main import *
from tools import *
import pygame

pygame.init()

# Creating the screen

screen_width = 1280
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Climate Change Game Thingie")
clock = pygame.time.Clock()

# logic
click_var = 0

# pygame
start_button_width = 275
start_button_height = 50
start_button_x = (screen_width - start_button_width) / 2
start_button_y = ((screen_height - start_button_height) / 2) + 250
start_button_pos = (start_button_x, start_button_y)
start_button_elevation = 10
start_button = BUttons("Click!", start_button_width, start_button_height,
                       start_button_pos, start_button_elevation, screen, clock)
