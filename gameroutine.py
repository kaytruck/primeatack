import pygame
import sys
import functools
import operator
import random
from gamestatus import Status

class Routine:
    def __init__(self):
        self.primes = [2, 3, 5]
        self.primes_labels = []
        self.answer = []
        self.level = 1
        self.status = Status.WAIT_FOR_START
        self.time_r_or_w = 0

        # 問題を生成する
        self.question = self.gen_question()

    def step(self, keys):
        if self.time_r_or_w > 0:
            self.time_r_or_w -= 20
        else:
            self.time_r_or_w = 0

        if not keys == None:
            if keys[pygame.K_ESCAPE]:
                self.answer = []
            if keys[pygame.K_BACKSPACE]:
                if len(self.answer) > 0:
                    self.answer.pop()
            if keys[pygame.K_RETURN]:
                self.atack()
            if keys[pygame.K_q] and (keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]):
                # Ctrl + q でゲーム終了
                self.status = Status.QUIT
            if keys[pygame.K_2]:
                self.answer.append(2)
            if keys[pygame.K_3]:
                self.answer.append(3)
            if keys[pygame.K_5]:
                self.answer.append(5)

        return self.question, self.primes, self.answer, self.status
    
    def atack(self):
        """
        素因数の場合、商を求める
        """
        if len(self.answer) > 0:
            # リストの全要素の積を求める
            a = functools.reduce(operator.mul, self.answer)
            if self.question % a == 0:
                # 割り切れた場合
                self.question /= a
                self.question = int(self.question)
                self.answer = []
        
        if self.question == 1:
            # 1まで割り切ったら正解とし、次の問題を表示
            self.status = Status.GAMING_RIGHT
            self.time_r_or_w = 500
            self.question = self.gen_question()
    
    def gen_question(self):
        """
        次の問題を生成する
        """
        max_c = random.randint(1, self.level + 4)
        q = 1
        for _ in range(max_c):
            q *= random.choice(self.primes)
        return q