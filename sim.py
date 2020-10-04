import pygame
import sys
import random
import math

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255, 0)
BACKGROUND_COLOR = (0,0,0)

entity_size = 10

clock = pygame.time.Clock()

class Entity:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y


entity_list = []

def init_entities(entity_number = 10):
    for i in range(entity_number):
        x = random.randint(0, WIDTH - entity_size)
        y = random.randint(0, HEIGHT - entity_size)
        entity_list.append(Entity(x, y))

def draw_entities(entity_list):
    for e in entity_list:
        pygame.draw.rect(screen, RED, (e.x, e.y, 10, 10))

init_entities()

while True:

    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(BACKGROUND_COLOR)

    #pygame.draw.rect(screen, RED, (0, 0, 10, 10))
    draw_entities(entity_list)

    clock.tick(30)
    #print('hello tick: ' + str(pygame.time.get_ticks()))

    pygame.display.update()