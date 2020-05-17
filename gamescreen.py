import pygame

import const

class GameScreen():
    def __init__(self, screen):
        self.screen = screen

        self.font_1 = pygame.font.SysFont(None, 72)
        self.font_2 = pygame.font.SysFont(None, 36)

        self.bs_label = self.font_2.render("BS", True, const.COLOR_CHAR)
        self.enter_label = self.font_2.render("ENTER", True, const.COLOR_CHAR)
    
    def update(self, question, primes, answer):
        # 表示用ラベルの生成
        question_label = self.font_1.render(str(question), True, const.COLOR_CHAR)
        answer_str = " * ".join(map(str, answer))
        answer_label = self.font_2.render(answer_str, True, const.COLOR_CHAR)
        primes_labels = [self.font_2.render(str(p), True, const.COLOR_CHAR) for p in primes]

        # 描画
        self.screen.fill(const.COLOR_SCREEN_BG)
        self.screen.blit(question_label, (50, 50))
        self.screen.blit(answer_label, (50, 130))
        for i, p_l in enumerate(primes_labels):
            self.screen.blit(p_l, (50 * (i + 1), 200))
        self.screen.blit(self.bs_label, (400, 250))
        self.screen.blit(self.enter_label, (450, 250))
