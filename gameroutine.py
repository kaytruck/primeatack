import pygame
import sys
import functools
import operator
import random

class Routine:
    def __init__(self):
        self.primes = [2, 3, 5]
        self.primes_labels = []
        self.answer = []
        self.level = 1

        # 問題を生成する
        self.question = self.gen_question()

    def step(self, keycode):
        if keycode == pygame.K_ESCAPE:
            self.answer = []
        if keycode == pygame.K_2:
            self.answer.append(2)
        if keycode == pygame.K_3:
            self.answer.append(3)
        if keycode == pygame.K_5:
            self.answer.append(5)
        if keycode == pygame.K_BACKSPACE:
            self.answer.pop()
        if keycode == pygame.K_RETURN:
            self.atack()

        return self.question, self.primes, self.answer
    
    def atack(self):
        if len(self.answer) > 0:
            a = functools.reduce(operator.mul, self.answer)
            if self.question % a == 0:
                self.question /= a
                self.question = int(self.question)
                self.answer = []
        
        if self.question == 1:
            self.question = self.gen_question()
    
    def gen_question(self):
        max_c = random.randint(1, self.level + 4)
        q = 1
        for _ in range(max_c):
            q *= random.choice(self.primes)
        return q