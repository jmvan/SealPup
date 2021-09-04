import discord
from enum import Enum
from game import Game

class State(Enum):
    NO_GAME = 1
    GAME_INIT = 2
    WAIT_FOR_PLAYERS = 2
    ROTATE_BLIND = 3
    BETTING = 4
    DEALING_FLOP = 5
    DEALING_TURN = 6
    DEALING_RIVER = 7
    WAITING_FOR_DEALING =

class GameState():
    """
    The State class determines the game state based off user commands in discord
    """
    def __init__(self):
        self.game = None
        self.game_state = State.NO_GAME

    def process_command(self, message: discord.Message, command: str) -> None:
        if (command == "!poker"):
            self.process_new_game()
        elif (command == "!join"):
            self.process_new_player()
        elif (command == "!deal"):
            self.process_dealing()
        elif (command == "!call"):
            self.process_player_call()
        elif (command == "!raise"):
            self.process_player_raise()
        elif (command == "!fold"):
            self.process_player_fold()
        elif (command == "!allin"):
            self.process_player_all_in()
        elif (command == "!help"):
            await message.channel.send("help command")
        elif (command == "!exit"):
            game = None
            await message.channel.send("The game has ended, thanks for playing!")

    def process_new_game(self):
        game = Game()

    def process_new_player(self):

    def process_dealing(self):

    def process_player_call(self):

    def process_player_raise(self):

    def process_player_raise(self):

    def process_player_fold(self):

    def process_player_all_in(self):

