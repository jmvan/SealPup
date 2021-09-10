import discord
from game import GameState
from game import Game

class Poker:
    """
    The Poker class represents a finite state machine that determines the state of the poker game.
    """
    def __init__(self):
        self.game = None

    def process_game_state(self, message: discord.Message) -> None:
        first_command = message.content.split()[0]
        if self.game is None:
            self.process_new_game(first_command=first_command, message=message)
        elif self.game.game_state == GameState.WAITING_PHASE:
            self.process_new_players(first_command=first_command, message=message)
        elif self.game.game_state == GameState.PRE_FLOP_PHASE:
            self.process_pre_flop_phase(first_command=first_command, message=message)
        elif self.game.game_state == GameState.FLOP_PHASE:
            self.process_flop_phase(first_command=first_command, message=message)
        elif self.game.game_state == GameState.TURN_PHASE:
            self.process_turn_phase(first_command=first_command, message=message)
        elif self.game.game_state == GameState.RIVER_PHASE:
            self.process_river_phase(first_command=first_command, message=message)
        elif self.game.game_state == GameState.SHOWDOWN_PHASE:
            self.process_showdown(first_command=first_command, message=message)

    def process_new_game(self, first_command: str, message: discord.Message) -> None:
        if first_command == "?poker":
            self.game = Game()
            self.game.game_state = GameState.WAITING_PHASE
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
            # TODO: limit players to 2 and 12
        elif first_command == "?deal":
            self.game.game_state = GameState.BETTING_PHASE
            self.game.deal_hole_cards()
            self.game.
            for better in self.game.betters:
                await better.user.send('Round {}: {}, {}'.format(self.game.round,
                                                                 better.first_card,
                                                                 better.second_card))

    def process_pre_flop_phase(self, first_command: str, message: discord.Message) -> None:
        current_better = self.game.get_current_better()
        if current_better.user != message.author:
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
            self.
        # TOOD: process the round

    def process_flop_phase(self, first_command: str, message: discord.Message) -> None:

        # Show the flop for the board
        if self.game.board

        current_better = self.game.get_current_better()
        if current_better.user != message.author:
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
            self.
        # TOOD: process the round

    def process_turn_phase(self, first_command: str, message: discord.Message) -> None:
        current_better = self.game.get_current_better()
        if current_better.user != message.author:
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
            self.
        # TOOD: process the round

    def process_river_phase(self, first_command: str, message: discord.Message) -> None:
        current_better = self.game.get_current_better()
        if current_better.user != message.author:
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
            self.
        # TOOD: process the round



    def process_showdown(self, first_command: str, message: discord.Message) -> None:




    def process_player_check(self, message: discord.Message) -> None:
        # check if the current player is able to make the check
        # if so, then increment the pot and balance
        # move the player to the end of the players queue
        if self.game.verify_check():


            # move the player to the end of the players queue
        else:
            # remove player from queue
        # check the queue if you're last

    def process_player_call(self, message: discord.Message) -> None:


    def process_player_raise(self, message: discord.Message) -> None:


    def process_player_fold(self, message: discord.Message) -> None:
        # remove the player from the betters queue


    def process_player_all_in(self, message: discord.Message) -> None:




