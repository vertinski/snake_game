#Define a python function which is a classic snake game.
#Display playing field using pygame library.

import pygame
import random
import time



pygame.init()

#define colours
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#frames per second
FPS = 10
clock = pygame.time.Clock()

#snake
snake_pos = [100,50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

#food
food_pos = [random.randrange(1, (SCREEN_WIDTH//10)) * 10, random.randrange(1, (SCREEN_HEIGHT//10)) * 10]
food_spawn = True

#direction
direction = "RIGHT"
changeto = direction

score = 0

#game over
def game_over():
    myFont = pygame.font.SysFont("monaco", 72)
    GOsurf = myFont.render("Game Over", True, RED)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 15)
    screen.blit(GOsurf, GOrect)
    show_score(0)
    pygame.display.flip()
    time.sleep(6)
    
    pygame.quit()
    sys.exit()

#show score
def show_score(choice=1):
    sFont = pygame.font.SysFont("monaco", 24)
    Ssurf = sFont.render("Score: {0}".format(score), True, BLACK)
    Srect = Ssurf.get_rect()
    if choice == 1:
        Srect.midtop = (80, 10)
    else:
        Srect.midtop = (360, 120)
    screen.blit(Ssurf, Srect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord("d"):
                changeto = "RIGHT"
            if event.key == pygame.K_LEFT or event.key == ord("a"):
                changeto = "LEFT"
            if event.key == pygame.K_UP or event.key == ord("w"):
                changeto = "UP"
            if event.key == pygame.K_DOWN or event.key == ord("s"):
                changeto = "DOWN"
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    #validation for direction
    if changeto == "RIGHT" and not direction == "LEFT":
        direction = "RIGHT"
    if changeto == "LEFT" and not direction == "RIGHT":
        direction = "LEFT"
    if changeto == "UP" and not direction == "DOWN":
        direction = "UP"
    if changeto == "DOWN" and not direction == "UP":
        direction = "DOWN"

    #change snake position
    if direction == "RIGHT":
        snake_pos[0] += 10
    if direction == "LEFT":
        snake_pos[0] -= 10
    if direction == "UP":
        snake_pos[1] -= 10
    if direction == "DOWN":
        snake_pos[1] += 10

    #body mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    #food spawn
    if food_spawn == False:
        food_pos = [random.randrange(1, (SCREEN_WIDTH//10)) * 10, random.randrange(1, (SCREEN_HEIGHT//10)) * 10]
    food_spawn = True

    #background
    screen.fill(WHITE)

    #draw snake
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

    #draw food
    pygame.draw.rect(screen, BLUE, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    #bound
    if snake_pos[0] > 790 or snake_pos[0] < 0:
        game_over()
    if snake_pos[1] > 590 or snake_pos[1] < 0:
        game_over()

    #self hit
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    show_score()
    pygame.display.flip()
    clock.tick(FPS)
