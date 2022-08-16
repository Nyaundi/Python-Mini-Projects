from turtle import Screen
import pygame
from pygame.locals import *

size = width, height =(800, 800)
road_w = int(width/1.6)
roadmark_w = int(width/80)

pygame.init()
running = True
#set window size 
screen = pygame.display.set_mode(size)
#set Title 
pygame.display.set_caption("James' Car Game")
#set background color
screen.fill((60, 220, 0))

#Apply Changes
pygame.display.update()

#load Player Car
car = pygame.image.load("car.png")
car_loc = car.get_rect()
car_loc.center = width/2 + road_w/4, height*0.8

#Load Enemy Car
car2 = pygame.image.load("car2.png")
car2_loc = car2.get_rect()
car2_loc.center = width/2 - road_w/4, height*0.2

#game loop
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running == False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w/2), 0])
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w/2), 0])

#draw graphics
    pygame.draw.rect(
        screen, 
        (50, 50, 50), 
        (width/2-road_w/2, 0, road_w, height))

    pygame.draw.rect(
        screen,
        (255, 240, 60), 
        (width/2-roadmark_w/2, 0, roadmark_w, height))

    pygame.draw.rect(
        screen,
        (255, 255, 255), 
        (width/2-road_w/2+ roadmark_w*2, 0, roadmark_w, height))

    pygame.draw.rect(
        screen,
        (255, 255, 255), 
        (width/2+road_w/2- roadmark_w*3, 0, roadmark_w, height))

    screen.blit(car, car_loc)
    pygame.display.update()
    screen.blit(car2, car2_loc)
    pygame.display.update()

pygame.quit()  