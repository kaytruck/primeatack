import pygame

import const
from gamestatus import Status


class GameScreen():
    def __init__(self, screen):
        self.screen = screen

        self.font_1 = pygame.font.SysFont(None, 72)
        self.font_2 = pygame.font.SysFont(None, 36)

        # ラベル
        self.esc_label = self.font_2.render("ESC", True, const.COLOR_CHAR)
        self.bs_label = self.font_2.render("BS", True, const.COLOR_CHAR)
        self.enter_label = self.font_2.render("ENTER", True, const.COLOR_CHAR)
        self.right_label = self.font_2.render("Right !", True,
                                              const.COLOR_RIGHT)

    def update(self, question, primes, answer, status, time_r_or_w):
        """画面描画

        Args:
            status (Status): ステータス(勝敗)
            time_r_or_w (Number): 勝敗ラベルを表示する時間
        """
        # 表示用ラベルの生成
        question_label = self.font_1.render(str(question), True,
                                            const.COLOR_CHAR)
        answer_str = " * ".join(map(str, answer))
        answer_label = self.font_2.render(answer_str, True, const.COLOR_CHAR)
        primes_labels = [
            self.font_2.render(str(p), True, const.COLOR_CHAR) for p in primes
        ]

        # 描画
        self.screen.fill(const.COLOR_SCREEN_BG)
        if time_r_or_w == 0:
            self.screen.blit(question_label, (50, 50))
        self.screen.blit(answer_label, (50, 130))
        for i, p_l in enumerate(primes_labels):
            self.screen.blit(p_l, (50 * (i + 1), 200))
        self.screen.blit(self.esc_label, (260, 250))
        self.screen.blit(self.bs_label, (330, 250))
        self.screen.blit(self.enter_label, (380, 250))

        if status == Status.GAMING_RIGHT and time_r_or_w > 0:
            right_label_rect = self.right_label.get_rect()
            right_label_rect.center = (const.WINDOW_WIDTH / 2,
                                       const.WINDOW_HEIGHT / 2)
            self.screen.blit(self.right_label, right_label_rect)
