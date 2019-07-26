import pygame
import random
pygame.init()

# board size
WIDTH = 700
HEIGHT = 500

# snake node size
SNAKE_NODE_SIZE = 46
SNAKE_BORDER = 2
SPEED_X = 50
SPEED_Y = 0

# colors
BODY = (0, 250, 0)
HEAD = (0, 156, 0)
FOOD = (254, 0, 0)

# food
is_food = False
FOOD_X = -1
FOOD_Y = -1

# score
SCORE = 1

# pygame settings
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")


class Snake_Node:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y


Snake = [Snake_Node(325, 225)]  # create a Snake with only head


def Draw_Snake():
    for i, node in enumerate(Snake):  # drawing snake
        pygame.draw.rect(win, HEAD if i == 0 else BODY, (node.x - SNAKE_NODE_SIZE / 2,
                                                         node.y - SNAKE_NODE_SIZE / 2, SNAKE_NODE_SIZE, SNAKE_NODE_SIZE))

    # drawing food
    if is_food:
        pygame.draw.rect(win, FOOD, (FOOD_X-SNAKE_NODE_SIZE/2,
                                     FOOD_Y-SNAKE_NODE_SIZE/2, SNAKE_NODE_SIZE, SNAKE_NODE_SIZE))

# move snake


def Move_Snake():
    x = Snake[0].x
    y = Snake[0].y
    Snake.insert(0, Snake_Node(x + SPEED_X, y + SPEED_Y))

    if Snake[0].x == FOOD_X and Snake[0].y == FOOD_Y:
        global SCORE, is_food
        SCORE += 1
        is_food = False
    else:
        Snake.pop(-1)


def Spawn_Food():

    x = random.randint(0, (WIDTH - 50) / 50) * 50 + 25
    y = random.randint(0, (HEIGHT - 50) / 50) * 50 + 25

    for j in Snake:
        if x == j.x or y == j.y:
            return Spawn_Food()

    global is_food, FOOD_X, FOOD_Y

    is_food = True
    FOOD_X = x
    FOOD_Y = y


def Check_Bound():
    x = Snake[0].x
    y = Snake[0].y

    if x < (SNAKE_NODE_SIZE + 2 * SNAKE_BORDER) / 2 or y < (SNAKE_NODE_SIZE + 2 * SNAKE_BORDER) / 2:
        return True
    if x > WIDTH - (SNAKE_NODE_SIZE + 2 * SNAKE_BORDER) / 2 or y > HEIGHT - (SNAKE_NODE_SIZE + 2 * SNAKE_BORDER) / 2:
        return True

    return False


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))
    Draw_Snake()
    pygame.display.update()

    keys = pygame.key.get_pressed()

    # input handling
    if keys[pygame.K_LEFT]:
        if len(Snake) > 1:
            if Snake[0].x != Snake[1].x + SNAKE_NODE_SIZE:
                SPEED_X = -50
                SPEED_Y = 0
        else:
            SPEED_X = -50
            SPEED_Y = 0
    if keys[pygame.K_RIGHT]:
        if len(Snake) > 1:
            if Snake[0].x != Snake[1].x - SNAKE_NODE_SIZE:
                SPEED_X = 50
                SPEED_Y = 0
        else:
            SPEED_X = 50
            SPEED_Y = 0
    if keys[pygame.K_UP]:
        if len(Snake) > 1:
            if Snake[0].y != Snake[1].y + SNAKE_NODE_SIZE:
                SPEED_X = 0
                SPEED_Y = -50
        else:
            SPEED_X = 0
            SPEED_Y = -50
    if keys[pygame.K_DOWN]:
        if len(Snake) > 1:
            if Snake[0].y != Snake[1].y - SNAKE_NODE_SIZE:
                SPEED_X = 0
                SPEED_Y = 50
        else:
            SPEED_X = 0
            SPEED_Y = 50

    pygame.time.delay(150)

    Move_Snake()

    if Check_Bound():
        run = False

    if is_food == False:
        Spawn_Food()


win.fill((0, 0, 0))
myfont = pygame.font.SysFont("monospace", 70)
label = myfont.render("Score : {}".format(SCORE), 40, (255, 255, 255))
win.blit(label, (WIDTH/4 , HEIGHT/2.3))
pygame.display.update()

while True:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
