from game import Game

class GameState(Enum):
    EXIT_GAME = 0
    NO_GAME = 1
    GAME_INIT = 2
    WAIT_FOR_PLAYERS = 2
    ROTATE_BLIND = 3
    BETTING = 4
    DEALING_FLOP = 5
    DEALING_TURN = 6
    DEALING_RIVER = 7
    WAITING_FOR_DEALING =

class State():
    """
    The State class determines the game state based off user commands in discord
    """
    def __init__(self):
        self.game = None
        self.game_state = GameState.NO_GAME


    def

def new_game():

def waiting_for_players():

def start_game():








