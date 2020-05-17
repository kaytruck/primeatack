from enum import Enum

class Status(Enum):
    WAIT_FOR_START = 0
    GAMING = 1
    GAME_OVER = 2
    QUIT = 3