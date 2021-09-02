from enum import Enum

class GameState(Enum):
    GAME_NONE = 1
    GAME_INIT = 2
    ROTATE_BLIND = 3
    BETTING = 4
    DEALING_FLOP = 5
    DEALING_TURN = 6
    DEALING_RIVER = 7


class Game():


