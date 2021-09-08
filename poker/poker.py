import discord
from game import GameState
from game import Game

class Poker:
    """
    The GameState class represents a finite state machine that determines the state of the poker game
    """
    def __init__(self):
        self.game = None

    def process_game_state(self, message: discord.Message) -> None:
        first_command = message.content.split()[0]
        if self.game is None:
            self.process_new_game(first_command=first_command, message=message)
        elif self.game.game_state == GameState.WAIT_FOR_PLAYERS:
            self.process_new_players(first_command=first_command, message=message)
        elif self.game.game_state == GameState.BETTING_PRE_FLOP:
            self.process_betting_pre_flop(first_command=first_command, message=message)

    def process_new_game(self, first_command: str, message: discord.Message) -> None:
        if first_command == "?poker":
            self.game = Game()
            self.game.game_state = GameState.WAIT_FOR_PLAYERS
            await message.channel.send("The poker game is currently looking for players\n" +
                                       "Type `?join` to join the game\n" +
                                       "Type '?deal` to start the game")

    def process_new_players(self, first_command: str, message: discord.Message) -> None:
        if first_command == "?poker":
            await message.channel.send("The poker game has already been initiated\n" +
                                       "Type `?join` to join the game\n" +
                                       "Type '?deal` to start the game")
        elif first_command == "?join":
            self.game.add_player(message.author)
            await message.channel.send('{} has joined the poker game.'.format(message.author.name))
        elif first_command == "?deal":
            self.game.game_state = GameState.BETTING_PRE_FLOP
            self.game.deal_hole_cards()
            # TODO: send message on who is currently big blind and small blind and whose turn it is

    def process_betting_pre_flop(self, first_command: str, message: discord.Message) -> None:
        if not self.game.check_current_player(message.author):

            await message.channel.send("")
        elif first_command == "?check":
            self.game.player_check()
        elif first_command == "?call":
            self.game.player_call()
        elif first_command == "?raise":
            self.game.player_raise()
        elif first_command == "?fold":
            self.game.player_fold()
        elif first_command == "?allin":
            self.game.player.
        elif first_command == "?help":
        elif first_command == "?exit":
        else:



    def process_player_check(self):
    def process_player_call(self):
    def process_player_raise(self):
    def process_player_fold(self):
    def process_player_all_in(self):




