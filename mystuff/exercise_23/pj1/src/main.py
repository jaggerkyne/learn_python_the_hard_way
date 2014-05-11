#! /bin/env python

import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

SCREEN = pygame.display.set_mode((1600, 900))

pygame.display.set_caption('RPG !')


# Files loading
bow = pygame.image.load('res/sprites/bow.png')

def draw(x, y):
    SCREEN.fill(( 33, 33, 33))
    SCREEN.blit(bow, (x, y))

# Main loop
def run():
    posx, posy = 0, 0
    while True:
        keyDown = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if keyDown[K_RIGHT]:
            posx += 2
        if keyDown[K_LEFT]:
            posx -= 2
        if keyDown[K_UP]:
            posy -= 2
        if keyDown[K_DOWN]:
            posy += 2

        draw(posx, posy)
        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == "__main__":
    run()