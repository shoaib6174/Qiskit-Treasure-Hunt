import pygame
from sys import exit

import random

width, height = 500, 1500
FPS = 60
zero = {"pos": (31, 155), "H" : 4, "X" : 1, "Y" : 1, "root X": 3, "S" : 0, "Z" : 0, "Measure": 0, "I" : 0, "name" : 0}
one = { "pos": (178, 305), "H" : 5, "X" : 0, "Y" : 0, "root X": 2, "S" : 1, "Z" : 1, "Measure": 1, "I" : 1, "name" : 1}

i     = {"pos": (31, 305), "H" : 3, "X" : 3, "Y" : 2, "Z" : 3, "root X": 0, "S" : 5, "Measure": random.randint(0, 1), "I" : 2, "name" : 'i'}
neg_i = {"pos": (179, 155), "H" : 2, "X" : 2, "Y" : 3, "Z" : 2, "root X": 1, "S" : 4, "Measure": random.randint(0, 1), "I" : 3, "name" : "-i"}

plus = {"pos": (104, 28), "H" : 0, "X" : 4, "Y" : 5, "root X": 4, "S" : 4, "Z" : 5, "Measure": random.randint(0, 1), "I" : 4, "name" : 4}
minus = { "pos": (105, 435), "H" : 1, "X" : 5, "Y" : 4, "root X": 5, "S" : 5, "Z" : 4, "Measure": random.randint(0, 1), "I" : 5, "name" : 5}

states = [ zero, one, i, neg_i, plus, minus]
moves = ['H', 'X', 'Y', 'Z', 'root X', 'S', 'Measure', 'I']

currState = 0
x_curr = states[currState]['pos'][0]
y_curr = states[currState]['pos'][1]

steps = 100
x_target, y_target = states[currState]['pos']
x_step , y_step = 0, 0

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Quantum Trip")
clock = pygame.time.Clock()

test_font = pygame.font.Font(None, 30)

piece = pygame.Surface((10,10))
piece.fill("blue")

card = pygame.Surface((20,40))
card.fill("blue")

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        # edit
        self.move = random.randint(0,7)
    def draw(self):
        global x_curr , x_target, x_step, y_curr, y_step, y_target, currState
        action = False

        pos = pygame.mouse.get_pos()

        self.move = random.randint(0,7)


        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked ==False:
                self.clicked = True
                action = True
                target_state = states[currState][moves[self.move]]
                x_target, y_target = states[target_state]['pos']
                x_step = (x_target - x_curr) / steps
                y_step = (y_target - y_curr) / steps

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action
card_button = Button(100, 500, card)

map_surface = pygame.image.load('utils/map.jpg')
car = pygame.image.load('utils/rocket (2).png')
text_surface = test_font.render("Quantum Trip", False, 'Green')




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(60)

    # cards
    if card_button.draw():
        print("start", x_curr, y_curr)

    screen.blit(map_surface, (0,0))
    screen.blit(piece, (200,100))
    car.set_alpha(150)
    screen.blit(text_surface,(210, 5))


    x_curr = round(x_curr, 5)
    y_curr = round(y_curr, 5)

    
    if x_curr != x_target:
        x_curr += x_step
    if y_curr != y_target:
        y_curr += y_step

    screen.blit(car, (x_curr,y_curr))


    