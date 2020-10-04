import pygame
import sys
import random
import math
import uuid

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255, 0)
BACKGROUND_COLOR = (0,0,0)

DEFAULT_SIZE = 10

clock = pygame.time.Clock()

class Entity:

    def __init__(self, id, x = 0, y = 0, vx = 0, vy = 0, size = DEFAULT_SIZE, color = (255, 255, 255)):
        self.id = id
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.width = size
        self.height = size
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def act(self):
        # logica di azione
        # movimento
        self.__move()

    def log(self):
        print(str(self.id) + ' ' + 'x: ' + str(self.x) + ' y: ' + str(self.y))

    def __move(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy


entity_list = []

def init_entities(entity_number = 10):
    for i in range(entity_number):
        size = 10
        id = str(uuid.uuid4())
        x = random.randint(0, WIDTH - size)
        y = random.randint(0, HEIGHT - size)
        vx = random.randint(-1, 1)
        vy = random.randint(-1, 1)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        e = Entity(id, x, y, vx, vy, size, color)
        entity_list.append(e)

init_entities()

while True:

    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(BACKGROUND_COLOR)

    for e in entity_list:
        e.draw()
        e.act()
        e.log()

    clock.tick(1)
    #print('hello tick: ' + str(pygame.time.get_ticks()))

    pygame.display.update()