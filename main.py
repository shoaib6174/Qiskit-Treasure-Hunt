import pygame
from sys import exit

import random

width, height = 500, 1500
FPS = 60
zero = {"pos": (31, 155), "H" : 4, "X" : 1, "Y" : 1, "root X": 3, "S" : 0, "Z" : 0, "Measure": 0, "I" : 0, "name" : '|0>'}
one = { "pos": (178, 305), "H" : 5, "X" : 0, "Y" : 0, "root X": 2, "S" : 1, "Z" : 1, "Measure": 1, "I" : 1, "name" : '|1>'}

i     = {"pos": (31, 305), "H" : 3, "X" : 3, "Y" : 2, "Z" : 3, "root X": 0, "S" : 5, "Measure": random.randint(0, 1), "I" : 2, "name" : '|i>'}
neg_i = {"pos": (179, 155), "H" : 2, "X" : 2, "Y" : 3, "Z" : 2, "root X": 1, "S" : 4, "Measure": random.randint(0, 1), "I" : 3, "name" : "|-i>"}

plus = {"pos": (104, 28), "H" : 0, "X" : 4, "Y" : 5, "root X": 4, "S" : 4, "Z" : 5, "Measure": random.randint(0, 1), "I" : 4, "name" : '|+>'}
minus = { "pos": (105, 435), "H" : 1, "X" : 5, "Y" : 4, "root X": 5, "S" : 5, "Z" : 4, "Measure": random.randint(0, 1), "I" : 5, "name" : '|->'}

states = [ zero, one, i, neg_i, plus, minus]
moves = ['H', 'X', 'Y', 'Z', 'root X', 'S', 'Measure', 'I']

currState = 0
dest = 1
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

black = pygame.Surface((350,200))
black.fill("black")

cards = [i for i in range(0,8, 2) ]

class Button():
    def __init__(self, x, y, image, move):
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        # edit
        self.move = move
    def draw(self):
        global x_curr , x_target, x_step, y_curr, y_step, y_target, currState, dest, score
        action = False

        pos = pygame.mouse.get_pos()

        # self.move = random.randint(0,7)
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked ==False:
                self.clicked = True
                action = True
                target_state = states[currState][moves[self.move]]
                currState = target_state
                if currState == dest:
                    score += 1
                    dest = random.randint(0,5)


                x_target, y_target = states[target_state]['pos']
                x_step = (x_target - x_curr) / steps
                y_step = (y_target - y_curr) / steps
                cards.remove(self.move)
                while True:
                    new_card = random.randint(0,7)
                    if  new_card != self.move and new_card not in cards:
                        cards.append(new_card)
                        break
                print(len(cards), cards, score, dest)




        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


        screen.blit(self.image , (self.rect.x, self.rect.y))
        return action


h = pygame.image.load('utils/h.png')
H = Button(5, 530, h , 0)

x = pygame.image.load('utils/x.png')
X = Button(70, 530, x, 1)

y = pygame.image.load('utils/y.png')
Y = Button(135, 530, y, 2)

z = pygame.image.load('utils/z.png')
Z = Button(200, 530, z, 3)

root_x = pygame.image.load('utils/root_x.png')
Root_X = Button(5, 600, root_x, 4)

s = pygame.image.load('utils/s.png')
S = Button(70, 600, s, 5)

m = pygame.image.load('utils/m.png')
M = Button(135, 600, m, 6)

i_img = pygame.image.load('utils/i.png')
I = Button(200, 600, i_img, 7)

buttons = [H, X, Y,  Z, Root_X, S, M, I]

map_surface = pygame.image.load('utils/map.jpg')
car = pygame.image.load('utils/rocket (2).png')
text_surface = test_font.render("Qiskit Treasure Hunt", False, 'Blue')
score = 0




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
  
    
    pygame.display.update()
    clock.tick(60)
    screen.blit(black, (0,530))
    




    for card in cards:
        buttons[card].draw()
        

    screen.blit(map_surface, (0,0))
    car.set_alpha(150)
    screen.blit(text_surface,(30, 5))




    x_curr = round(x_curr, 5)
    y_curr = round(y_curr, 5)

    
    if x_curr != x_target:
        x_curr += x_step
    if y_curr != y_target:
        y_curr += y_step

    screen.blit(car, (x_curr,y_curr))
    screen.blit(black, (270,30))

    score_text = test_font.render(f"Treasures Found: {score}", False, 'Red')
    dest_text = test_font.render(f"Next Treasure:   {states[dest]['name']}", False, 'Green')
    screen.blit(score_text,(280, 50))
    screen.blit(dest_text,(280, 90))    
    

    


    


    