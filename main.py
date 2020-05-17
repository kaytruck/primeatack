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
    game_screen = gamescreen.GameScreen(screen)
    keycode = None

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif e.type == pygame.KEYDOWN:
                keycode = e.key

        # input_keys = pygame.key.get_pressed()
        question, primes, answer = routine.step(keycode)
        game_screen.update(question, primes, answer)

        keycode = None
        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()
