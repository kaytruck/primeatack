from enum import Enum


class Status(Enum):
    WAIT_FOR_START = 0
    GAMING = 10
    GAMING_RIGHT = 11
    GAMING_WRONG = 12
    GAME_OVER = 20
    QUIT = 33
