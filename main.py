import pygame
import sys
import functools
import operator

import const
import gameroutine
import gamescreen

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    clock = pygame.time.Clock()
    
    routine = gameroutine.Routine()
    game_screen = gamescreen.GameScren(screen)

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        input_keys = pygame.key.get_pressed()
        question, primes, answer = routine.step(input_keys)
        game_screen.update(question, primes, answer)

        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()
