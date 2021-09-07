import discord
from typing import List
from player import Player


class RoundState(Enum):
    NO_GAME = 1
    WAIT_FOR_PLAYERS = 2
    DEALING = 3
    BETTING_PREFLOP = 4
    BETTING_FLOP = 5
    BETTING_TURN = 6
    BETTING_RIVER = 7

class Poker():
    """
    The GameState class represents a finite state machine that determines the state of the poker game
    """
    def __init__(self):
        self.round = None
        self.num_round = 0
        self.players: List[Player] = []

    def process_round(self, message: discord.Message) -> None:
        if self.round.round_state

    def process_




    def process_command(self, message: discord.Message) -> None:
        first_command = message.content.split()[0]
        if first_command == "?poker":
            self.process_new_game(message)
        elif first_command == "?join":
            self.process_new_player(message=message)
        elif first_command == "?deal":
            self.process_dealing(message=message)
        elif first_command == "?check":
            self.process_player_check()
        elif first_command == "?call":
            self.process_player_call()
        elif first_command == "?raise":
            self.process_player_raise()
        elif first_command == "?fold":
            self.process_player_fold()
        elif first_command == "?allin":
            self.process_player_all_in()
        elif first_command == "?help":
            await message.channel.send("help command")
        elif first_command == "?exit":
            self.game = None
            self.game.game_state = GameState.NO_GAME
            await message.channel.send("The game has ended, thanks for playing!")
        else:
            await message.channel.send("Command not recognized, please type `?help` to see the list of commands.")

    def process_new_game(self, message: discord.Message):
        if self.game.game_state == GameState.NO_GAME:
            self.game = Game()
            self.game.game_state = GameState.WAIT_FOR_PLAYERS
            await message.channel.send("The poker game is currently looking for players\n" +
                                       "Type `?join` to join the game\n" +
                                       "Type '?deal` to start the game")
        elif self.game.game_state == GameState.WAIT_FOR_PLAYERS:
            await message.channel.send("The poker game is currently looking for players\n" +
                                       "Type `?join` to join the game\n" +
                                       "Type '?deal` to start the game")
        else:
            await message.channel.send("The poker game has already started.")

    def process_new_player(self, message: discord.Message):
        if self.game.game_state == GameState.NO_GAME:
            await message.channel.send("The poker game has not started yet\n" +
                                       "Type `?poker` to start looking for players")
        elif self.game.game_state == GameState.WAIT_FOR_PLAYERS:
            self.game.add_player(message.author)
            await message.channel.send('{} has joined the poker game.'.format(message.author.name))
        else:
            # add the player, but wait for next round





    def process_dealing(self, message: discord.Message):
        if self.game.game_state == GameState.NO_GAME:
            await message.channel.send("The poker game has not started yet\n" +
                                       "Type `?poker` to start looking for players")
        elif self.game.game_state == GameState.WAIT_FOR_PLAYERS:
            self.game.game_state = GameState.BETTING_PREFLOP
            self.game.deal_hole_cards() # send two cards to players
        else:
            await message.channel.send("The poker game has already started and the cards have been dealt.")

    def process_preflop(self):
        if self.game.game_state == GameState.NO_GAME:
            await message.channel.send("The poker game has not started yet\n" +
                                       "Type `?poker` to start looking for players")
        elif self.game.game_state == GameState.WAIT_FOR_PLAYERS:



    def process_

    def process_player_check(self):
        if self.game.game_state == GameState.BETTING_PREFLOP:
        elif self.game.game_state == GameState.BETTING


    def process_player_call(self):

    def process_player_raise(self):


    def process_player_fold(self):

    def process_player_all_in(self):
        # check if the player is still in


