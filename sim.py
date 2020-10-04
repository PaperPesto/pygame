import pygame
import sys
import random
import math
import uuid

pygame.init()
pygame.display.set_caption('sim')

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255, 0)
BACKGROUND_COLOR = (0,0,0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

DEFAULT_SIZE = 10

clock = pygame.time.Clock()

class Entity:

    def __init__(self, uuid, x = 0, y = 0, vx = 0, vy = 0, size = DEFAULT_SIZE, color = (255, 255, 255)):
        self.uuid = uuid
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
        return self.id() + " " + "x: " + str(self.x) + " y: " + str(self.y)

    def id(self):
        return str(self.uuid[0:4])

    def __move(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy


entity_list = []
selected_entity = None
show_popup = False  # flag per visualizzazione del popup delle statistiche dell'entità

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

def search_entities(x, y):
    for e in entity_list:
        if (x >= e.x and x < e.x + e.width) and (y >= e.y and y < e.y + e.height):
            return e
    return None

init_entities()

while True:

    #screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            e = search_entities(event.pos[0], event.pos[1])
            if e:
                print('found ' + e.id())
                show_popup = True
                selected_entity = e
            else:
                show_popup = False


    screen.fill(BACKGROUND_COLOR)

    for e in entity_list:
        e.draw()
        e.act()
        #print(e.log())
    
    if show_popup:
        font = pygame.font.SysFont("monospace", 35)
        text = font.render(selected_entity.log(), True, green, blue)
        text_rect = text.get_rect()
        text_rect.center = (400, 300)
        screen.blit(text, text_rect)

    clock.tick(30)

    pygame.display.update()