import pygame
import sys
import functools
import operator

class Routine:
    def __init__(self):
        self.question = 90
        self.primes = [2, 3, 5]
        self.primes_labels = []
        self.answer = []

    def step(self, input_keys):
        if input_keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if input_keys[pygame.K_2]:
            self.answer.append(2)
        if input_keys[pygame.K_3]:
            self.answer.append(3)
        if input_keys[pygame.K_5]:
            self.answer.append(5)
        if input_keys[pygame.K_BACKSPACE]:
            self.answer.pop()
        if input_keys[pygame.K_RETURN]:
            if len(self.answer) > 0:
                a = functools.reduce(operator.mul, self.answer)
                if self.question % a == 0:
                    self.question /= a
                    self.question = int(self.question)
                    self.answer = []

        return self.question, self.primes, self.answer