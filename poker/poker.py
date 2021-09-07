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

    def process_betting_pre_flop(self, first_command: str, message: discord.Message) -> None:
        if
        if first_command == "?check":


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

    def process_new_player(self, message: discord.Message):
        if self.game.game_state == GameState.NO_GAME:
            await message.channel.send("The poker game has not started yet\n" +
                                       "Type `?poker` to start looking for players")
        elif self.game.game_state == GameState.WAIT_FOR_PLAYERS:
            self.game.add_player(message.author)
            await message.channel.send('{} has joined the poker game.'.format(message.author.name))
        else:
            await message.channel.send('{} cannot join the poker game.'.format(message.author.name))
            # TODO: add the player, but wait for next round

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


    def process_player_check(self):
        if self.game.game_state == GameState.BETTING_PREFLOP:
        elif self.game.game_state == GameState.BETTING


    def process_player_call(self):

    def process_player_raise(self):


    def process_player_fold(self):

    def process_player_all_in(self):
        # check if the player is still in


