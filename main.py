import pygame
import sys
import functools
import operator

import const
from gamestatus import Status
import gameroutine
import gamescreen

def main():
    pygame.init()
    pygame.key.set_repeat(100, 100)
    screen = pygame.display.set_mode((600, 400))
    clock = pygame.time.Clock()
    
    routine = gameroutine.Routine()
    game_screen = gamescreen.GameScreen(screen)
    input_keys = None

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                game_quit()
            elif e.type == pygame.KEYDOWN:
                input_keys = pygame.key.get_pressed()

        question, primes, answer = routine.step(input_keys)
        if routine.status == Status.QUIT:
            game_quit()
        game_screen.update(question, primes, answer)

        input_keys = None
        pygame.display.update()
        clock.tick(30)

def game_quit():
    pygame.exit()
    sys.exit()

if __name__ == '__main__':
    main()
