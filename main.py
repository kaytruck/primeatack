import pygame
import sys
import functools
import operator

import const
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
                pygame.quit()
                sys.exit()
            elif e.type == pygame.KEYDOWN:
                input_keys = pygame.key.get_pressed()

        question, primes, answer = routine.step(input_keys)
        game_screen.update(question, primes, answer)

        input_keys = None
        pygame.display.update()
        clock.tick(30)

if __name__ == '__main__':
    main()
