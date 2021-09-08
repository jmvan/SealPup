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
        elif self.game.game_state == GameState.WAIT_FOR_PLAYERS_PHASE:
            self.process_new_players(first_command=first_command, message=message)
        elif self.game.game_state == GameState.BETTING_PHASE:
            self.process_betting(first_command=first_command, message=message)
        elif self.game.game_state == GameState.SHOWDOWN_PHASE:
            self.process_showdown(first_command=first_command, message=message)

    def process_new_game(self, first_command: str, message: discord.Message) -> None:
        if first_command == "?poker":
            self.game = Game()
            self.game.game_state = GameState.WAIT_FOR_PLAYERS_PHASE
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
            self.game.game_state = GameState.BETTING_PHASE
            self.game.deal_hole_cards()
            # TODO: send message on who is currently big blind and small blind and whose turn it is

    def process_betting(self, first_command: str, message: discord.Message) -> None:
        current_player = self.game.get_current_player()
        if current_player.user != message.author:
            await message.channel.send('It is not {} turn to play'.format(message.author.name))
        elif first_command == "?check":
            self.process_player_check(message=message)
        elif first_command == "?call":
            self.process_player_call(message=message)
        elif first_command == "?raise":
            self.process_player_raise(message=message)
        elif first_command == "?fold":
            self.process_player_fold(message=message)
        elif first_command == "?allin":
            self.process_player_all_in(message=message)
        elif first_command == "?help":
        elif first_command == "?exit":
        else:

    def process_showdown(self, first_command: str, message: discord.Message) -> None:




    def process_player_check(self, message: discord.Message) -> None:
        # check if the current player is able to make the check
        # if so, then increment the pot and balance
        # move the player to the end of the players queue
        current_player = self.game.get_current_player()
        if self.game.verify_check():
            await
        else:
            # remove player from queue

    def process_player_call(self, message: discord.Message) -> None:

    def process_player_raise(self, message: discord.Message) -> None:
    def process_player_fold(self, message: discord.Message) -> None:
    def process_player_all_in(self, message: discord.Message) -> None:




