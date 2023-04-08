import pygame
import math
import time
import random
from particleStuff import Shockwave
from calcs import distance
from text import draw_text
import copy

pygame.init()

# ---------------- Setting up the screen, assigning some global variables, and loading text fonts
screen = pygame.display.set_mode((1050, 700))
clock = pygame.time.Clock()
fps = 60
screen_width = screen.get_width()
screen_height = screen.get_height()
screen2 = pygame.Surface((screen_width, screen_height)).convert_alpha()
screenT = pygame.Surface((screen_width, screen_height)).convert_alpha()
screenT.set_alpha(100)
screenUI = pygame.Surface((screen_width, screen_height)).convert_alpha()
spacerUI = 10
timer = 0
shake = [0, 0]
shake_strength = 3
scroll_counter = 0
pygame.font.get_fonts()
font15 = pygame.font.Font("freesansbold.ttf", 15)
font20 = pygame.font.Font("freesansbold.ttf", 20)
font30 = pygame.font.Font("freesansbold.ttf", 30)
font40 = pygame.font.Font("freesansbold.ttf", 40)
better_font40 = pygame.font.SysFont("keyboard.ttf", 40)
font50 = pygame.font.Font("freesansbold.ttf", 50)
font100 = pygame.font.Font("freesansbold.ttf", 100)


class Endesga:
    maroon_red = (87, 28, 39)
    lighter_maroon_red = (127, 36, 51)
    dark_green = (9, 26, 23)
    light_brown = (191, 111, 74)
    black = (19, 19, 19)
    grey_blue = (66, 76, 110)
    cream = (237, 171, 80)
    white = (255, 255, 255)
    greyL = (200, 200, 200)
    grey = (150, 150, 150)
    greyD = (100, 100, 100)
    greyVD = (50, 50, 50)
    very_light_blue = (199, 207, 221)
    my_blue = [7, 15, 21]


class Col:
    white = (250, 240, 240)
    beige = (155, 127, 88)
    dark_brown_grey = (54, 49, 54)
    brown_grey = (71, 67, 59)
    light_brown_grey = (84, 80, 76)
    dark_orange = (115, 68, 28)


# Defining some more variables to use in the game loop
oscillating_random_thing = 0
ShakeCounter = 0

level = [[2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2]]


level2 = copy.deepcopy(level)
tile_rects = []

spawn_rate = 100
wall_growth = 6
spread_rate = wall_growth - 4
iteration_count = 8
tile_size = 20
central_path_width = 0.15
path_width = 1
path_dist = 5

ty = 0
for row in level:
    tx = 0
    for t in row:
        # *** 1.514 is the ratio of the length to the width of the screen ***
        if random.randint(0, spawn_rate) == 1:
            if level[ty][tx] == 2:
                if random.randint(0, 5) == 1:
                    level[ty][tx] = 1
            else:
                level[ty][tx] = 1
        if random.randint(0, 5):
            if math.fabs(1.514 - (tx/(ty + 0.001))) < central_path_width or math.fabs(tx - path_dist) < path_width or math.fabs(tx - (len(row) - path_dist)) < path_width or math.fabs(ty - path_dist) < path_width or math.fabs(ty - (len(level) - path_dist)) < path_width:
                level[ty][tx] = 2
        if tx == 0 or tx == len(row) - 1 or ty == 0 or ty == len(level) - 1:
            level[ty][tx] = 1
        tx += 1
    ty += 1

t = 0
for i in range(iteration_count):
    ty = 0
    for row in level2:
        tx = 0
        for t in row:
            if t == 1:
                if tx != 0 and tx != len(row) - 1 and ty != 0 and ty != len(level2) - 1:
                    if tx != 0:
                        if level[ty][tx - 1] != 2:
                            if random.randint(0, spread_rate) == 1:
                                level[ty][tx - 1] = 1
                    if tx != len(row) - 1:
                        if level[ty][tx + 1] != 2:
                            if random.randint(0, spread_rate) == 1:
                                level[ty][tx + 1] = 1
                    if ty != 0:
                        if level[ty - 1][tx] != 2:
                            if random.randint(0, spread_rate) == 1:
                                level[ty - 1][tx] = 1
                    if ty != len(level2) - 1:
                        if level[ty + 1][tx] != 2:
                            if random.randint(0, spread_rate) == 1:
                                level[ty + 1][tx] = 1
                else:
                    if random.randint(0, wall_growth) == 1:
                        if tx == 0:
                            if level[ty][tx + 1] != 2:
                                level[ty][tx + 1] = 1
                        if tx == len(row) - 1:
                            if level[ty][tx - 1] != 2:
                                level[ty][tx - 1] = 1
                        if ty == 0:
                            if level[ty + 1][tx] != 2:
                                level[ty + 1][tx] = 1
                        if ty == len(level2) - 1:
                            if level[ty - 1][tx] != 2:
                                level[ty - 1][tx] = 1
            tx += 1
        ty += 1
    level2 = copy.deepcopy(level)

ty = 0
for row in level:
    tx = 0
    for t in row:
        if t == 1 and t != 2:
            tile_rects.append(pygame.rect.Rect(tile_size * tx, tile_size * ty, tile_size, tile_size))
        tx += 1
    ty += 1


class Player:
    def __init__(self, x, y, width, height, speed, movement, ammo_timer, timer_max, shocks, blast_radius, damage, hp, max_hp):
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.s = speed
        self.m = movement
        self.aT = ammo_timer
        self.aM = timer_max
        self.sh = shocks
        self.br = blast_radius
        self.d = damage
        self.hp = hp
        self.mhp = max_hp
        self.rect = pygame.rect.Rect(self.x, self.y, self.w, self.h)

    # left, right, up, down
    def move(self):
        if self.m[0]:
            self.x -= self.s
        if self.m[1]:
            self.x += self.s
        if self.m[2]:
            self.y -= self.s
        if self.m[3]:
            self.y += self.s

    def moveT(self, r):
        self.rect.x = self.x
        self.rect.y = self.y
        if self.m[0]:
            self.x -= self.s
        if self.m[1]:
            self.x += self.s
        if self.m[0] or self.m[1]:
            for tile in r:
                if self.rect.colliderect(tile):
                    if math.fabs(self.x - tile.x + tile.width) < tile.width / 4:
                        self.x = tile.x - tile.width
                    if math.fabs(self.x - tile.x - tile.width) < tile.width / 4:
                        self.x = tile.x + tile.width
        if self.m[2]:
            self.y -= self.s
        if self.m[3]:
            self.y += self.s
        if self.m[2] or self.m[3]:
            for tile in r:
                if self.rect.colliderect(tile):
                    if math.fabs(self.y - tile.y + tile.height) < tile.height / 4:
                        self.y = tile.y - tile.height
                    if math.fabs(self.y - tile.y - tile.height) < tile.height / 4:
                        self.y = tile.y + tile.height

    def shoot(self):
        self.sh.append(Shockwave(self.rect.x + self.rect.w / 2, self.rect.y + self.rect.h / 2, 3, 15, self.br, 5, Col.dark_orange, Col.brown_grey, 5, self.d, self.d))

    def draw(self, s, color):
        pygame.draw.rect(s, color, self.rect, 0, 2)


spawn_range = 50
players = [Player(spawn_range, spawn_range, tile_size, tile_size, 2, [False, False, False, False], 30, 120, [], 300, 100, 100, 100), Player(screen_width - spawn_range, screen_height - spawn_range, tile_size, tile_size, 2, [False, False, False, False], 30, 120, [], 300, 100, 100, 100)]
print(len(tile_rects))

# ---------------- Main Game Loop
last_time = time.time()
running = True
while running:

    # ---------------- Reset Variables and Clear screens
    oscillating_random_thing += math.pi/fps
    click = False
    mx, my = pygame.mouse.get_pos()
    screen.fill(Col.dark_brown_grey)
    screen2.fill(Col.dark_brown_grey)
    screenT.fill((0, 0, 0, 0))
    screenUI.fill((0, 0, 0, 0))
    dt = time.time() - last_time
    dt *= 60
    last_time = time.time()
    timer -= 1 * dt
    shake = [0, 0]
    if players[0].aT <= players[0].aM:
        players[0].aT += 1
    if players[1].aT <= players[1].aM:
        players[1].aT += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_a:
                players[0].m[0] = True
            if event.key == pygame.K_d:
                players[0].m[1] = True
            if event.key == pygame.K_w:
                players[0].m[2] = True
            if event.key == pygame.K_s:
                players[0].m[3] = True
            if event.key == pygame.K_q:
                if players[0].aT > players[0].aM:
                    Player.shoot(players[0])
                    players[0].aT = 0
            if event.key == pygame.K_BACKSLASH:
                if players[1].aT > players[1].aM:
                    Player.shoot(players[1])
                    players[1].aT = 0

            if event.key == pygame.K_LEFT:
                players[1].m[0] = True
            if event.key == pygame.K_RIGHT:
                players[1].m[1] = True
            if event.key == pygame.K_UP:
                players[1].m[2] = True
            if event.key == pygame.K_DOWN:
                players[1].m[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                players[0].m[0] = False
            if event.key == pygame.K_d:
                players[0].m[1] = False
            if event.key == pygame.K_w:
                players[0].m[2] = False
            if event.key == pygame.K_s:
                players[0].m[3] = False

            if event.key == pygame.K_LEFT:
                players[1].m[0] = False
            if event.key == pygame.K_RIGHT:
                players[1].m[1] = False
            if event.key == pygame.K_UP:
                players[1].m[2] = False
            if event.key == pygame.K_DOWN:
                players[1].m[3] = False

    for t in tile_rects:
        pygame.draw.rect(screen2, Col.brown_grey, (t.x - t.width / 7, t.y + t.height / 7, t.width, t.height))

    for t in tile_rects:
        pygame.draw.rect(screen2, Col.light_brown_grey, t)

    for p in players:
        Player.moveT(p, tile_rects)
        Player.draw(p, screen2, Col.beige)

    for shock in players[0].sh:
        Shockwave.expand(shock)
        shock.d = shock.size * shock.od / shock.max_size
        if shock.width < 1.5:
            players[0].sh.remove(shock)
        if distance((shock.x, shock.y), (players[1].x, players[1].y)) < shock.size:
            players[1].hp -= 1000 / shock.d
            players[0].sh.remove(shock)
        Shockwave.blit(shock, screen2)

    for shock2 in players[1].sh:
        Shockwave.expand(shock2)
        shock2.d = shock2.size * shock2.od / shock2.max_size
        if shock2.width < 1.5:
            players[1].sh.remove(shock2)
        if distance((shock2.x, shock2.y), (players[0].x, players[0].y)) < shock2.size:
            players[0].hp -= 1000 / shock2.d
            players[1].sh.remove(shock2)
        Shockwave.blit(shock2, screen2)
    
    pygame.draw.rect(screenUI, Col.white, pygame.rect.Rect(spacerUI, spacerUI, players[0].aT - 1, spacerUI), 0, 4)
    pygame.draw.rect(screenUI, Col.white, pygame.rect.Rect(spacerUI, spacerUI, players[0].aM, spacerUI), 3, 2)

    pygame.draw.rect(screenUI, Col.white, pygame.rect.Rect(screen_width - spacerUI - players[1].aM, spacerUI, players[1].aT - 1, spacerUI), 0, 4)
    pygame.draw.rect(screenUI, Col.white, pygame.rect.Rect(screen_width - spacerUI - players[1].aM, spacerUI, players[1].aM, spacerUI), 3, 2)

    pygame.draw.rect(screenUI, Col.white, pygame.rect.Rect(spacerUI, spacerUI * 3, players[0].hp - 1, spacerUI), 0, 4)
    pygame.draw.rect(screenUI, Col.white, pygame.rect.Rect(spacerUI, spacerUI * 3, players[0].mhp, spacerUI), 3, 2)

    pygame.draw.rect(screenUI, Col.white, pygame.rect.Rect(screen_width - spacerUI - players[1].aM, spacerUI * 3, players[1].hp - 1, spacerUI), 0, 4)
    pygame.draw.rect(screenUI, Col.white, pygame.rect.Rect(screen_width - spacerUI - players[1].aM, spacerUI * 3, players[1].mhp, spacerUI), 3, 2)

    pygame.mouse.set_visible(False)
    pygame.draw.circle(screenUI, Col.white, (mx, my), 5, 1)
    screen.blit(screen2, (shake[0], shake[1]))
    screen.blit(screenT, (0, 0))
    screen.blit(screenUI, (0, 0))
    pygame.display.update()
    clock.tick(fps)
