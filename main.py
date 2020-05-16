import pygame
import sys

import const

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    clock = pygame.time.Clock()
    
    font_1 = pygame.font.SysFont(None, 72)
    font_2 = pygame.font.SysFont(None, 36)

    bs_label = font_2.render("BS", True, const.WHITE)
    enter_label = font_2.render("ENTER", True, const.WHITE)

    primes = [2, 3, 5]
    primes_labels = []
    answer = [2, 3, 3, 5]

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        answer_str = " * ".join(map(str, answer))

        question_label = font_1.render(str(90), True, const.WHITE)
        answer_label = font_2.render(answer_str, True, const.WHITE)
        primes_labels = [font_2.render(str(p), True, const.WHITE) for p in primes]

        screen.fill(const.BLACK)
        screen.blit(question_label, (50, 50))
        screen.blit(answer_label, (50, 130))
        for i, p_l in enumerate(primes_labels):
            screen.blit(p_l, (50 * (i + 1), 200))
        screen.blit(bs_label, (400, 250))
        screen.blit(enter_label, (450, 250))

        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()
