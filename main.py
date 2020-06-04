import pygame
import sys
import const
from gamestatus import Status
import gameroutine
import gamescreen


def main():
    pygame.init()
    pygame.key.set_repeat(100, 100)
    screen = pygame.display.set_mode((const.WINDOW_WIDTH, const.WINDOW_HEIGHT))
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

        question, primes, answer, status = routine.step(input_keys)
        if status == Status.QUIT:
            game_quit()
        game_screen.update(question, primes, answer, status,
                           routine.time_r_or_w)

        input_keys = None
        pygame.display.update()
        clock.tick(20)


def game_quit():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
