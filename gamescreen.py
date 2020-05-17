import pygame

import const

class GameScren():
    def __init__(self, screen):
        self.screen = screen

        self.font_1 = pygame.font.SysFont(None, 72)
        self.font_2 = pygame.font.SysFont(None, 36)

        self.bs_label = font_2.render("BS", True, const.WHITE)
        self.enter_label = font_2.render("ENTER", True, const.WHITE)
    
    def update(self, question, primes, answer):
        # 表示用ラベルの生成
        question_label = font_1.render(str(question), True, const.WHITE)
        answer_str = " * ".join(map(str, answer))
        answer_label = font_2.render(answer_str, True, const.WHITE)
        primes_labels = [font_2.render(str(p), True, const.WHITE) for p in primes]

        # 描画
        self.screen.fill(const.BLACK)
        self.screen.blit(question_label, (50, 50))
        self.screen.blit(answer_label, (50, 130))
        for i, p_l in enumerate(primes_labels):
            self.screen.blit(p_l, (50 * (i + 1), 200))
        self.screen.blit(bs_label, (400, 250))
        self.screen.blit(enter_label, (450, 250))
