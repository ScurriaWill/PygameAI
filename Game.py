import pygame
import sys
import math

pygame.init()

speed = [(2 + math.pi)/3, (2+math.e)/3]
black = 0, 0, 0

screen = pygame.display.set_mode(size=(0, 0), flags=pygame.FULLSCREEN)

size = width, height = pygame.display.get_window_size()

ball = pygame.image.load("BeachBall.png")
ball = pygame.transform.scale(ball, (100, 100))
ball_rect = ball.get_rect()
counter = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ball_rect = ball_rect.move(speed)
    speed[1] = speed[1] + 0.06
    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] = -speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > height:
        speed[1] = -speed[1]/1.04

    if ball_rect.bottom > 900:
        counter += 1
    else:
        counter = 0

    if counter > 120:
        speed[1] = -10
        counter = 0

    # print(counter)

    screen.fill(black)
    screen.blit(ball, ball_rect)
    pygame.display.flip()
